import os
import re
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

API_KEY = os.getenv("HINDSIGHT_API_KEY")
BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)
BANK_ID = os.getenv(
    "HINDSIGHT_BANK_ID",
    "incidentmind"
)

if not API_KEY:
    raise ValueError("HINDSIGHT_API_KEY is missing from .env")

client = Hindsight(
    base_url=BASE_URL,
    api_key=API_KEY
)


def get_field(obj, name, default=None):
    if obj is None:
        return default

    if isinstance(obj, dict):
        return obj.get(name, default)

    return getattr(obj, name, default)


def extract_from_text(text, labels):
    """Find a field such as Root Cause: ... inside memory text."""

    if not text:
        return None

    for label in labels:

        pattern = rf"{re.escape(label)}\s*:\s*(.+)"

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            value = match.group(1).strip()

            # Stop at another known field
            value = re.split(
                r"\n(?:Incident|Root Cause|Fix|Resolution Time|Service|When)\s*:",
                value,
                flags=re.IGNORECASE
            )[0].strip()

            if value:
                return value

    return None


def store_incident(content, metadata=None):

    try:

        if metadata is None:
            metadata = {}

        client.retain(
            bank_id=BANK_ID,
            content=content,
            metadata=metadata
        )

        print("Incident stored successfully.")

        return True

    except Exception as e:

        print(
            "Hindsight retain error:",
            repr(e)
        )

        return False


def recall_incidents(query):

    try:

        result = client.recall(
            bank_id=BANK_ID,
            query=query
        )

        print("\nRAW HINDSIGHT RESPONSE:")
        print(result)

        results = get_field(
            result,
            "results",
            []
        )

        memories = []

        for memory in results[:5]:

            text = get_field(
                memory,
                "text",
                ""
            ) or ""

            metadata = get_field(
                memory,
                "metadata",
                {}
            ) or {}

            scores = get_field(
                memory,
                "scores",
                None
            )

            semantic_score = get_field(
                scores,
                "semantic",
                None
            )

            final_score = get_field(
                scores,
                "final",
                None
            )

            # -------------------------
            # SERVICE
            # -------------------------

            service = (
                metadata.get("service")
                or get_field(
                    memory,
                    "service",
                    None
                )
                or extract_from_text(
                    text,
                    ["Service"]
                )
                or "Unknown Service"
            )

            # -------------------------
            # TIMESTAMP
            # -------------------------

            timestamp = (
                metadata.get("timestamp")
                or get_field(
                    memory,
                    "timestamp",
                    None
                )
                or get_field(
                    memory,
                    "mentioned_at",
                    None
                )
            )

            # -------------------------
            # ROOT CAUSE
            # -------------------------

            root_cause = (
                metadata.get("root_cause")
                or get_field(
                    memory,
                    "root_cause",
                    None
                )
                or extract_from_text(
                    text,
                    [
                        "Root Cause",
                        "Root cause"
                    ]
                )
            )

            # -------------------------
            # FIX
            # -------------------------

            fix = (
                metadata.get("fix")
                or get_field(
                    memory,
                    "fix",
                    None
                )
                or extract_from_text(
                    text,
                    [
                        "Fix",
                        "Resolution",
                        "Remediation"
                    ]
                )
            )

            memories.append({

                "id": get_field(
                    memory,
                    "id"
                ),

                "text": text,

                "type": get_field(
                    memory,
                    "type"
                ),

                "mentioned_at": get_field(
                    memory,
                    "mentioned_at"
                ),

                "timestamp": timestamp,

                "service": service,

                "root_cause": (
                    root_cause
                    or "Not available"
                ),

                "fix": (
                    fix
                    or "Not available"
                ),

                "metadata": metadata,

                "semantic_score": semantic_score,

                "final_score": final_score
            })

        print(
            "\nHindsight returned",
            len(memories),
            "memories."
        )

        return memories

    except Exception as e:

        print(
            "Hindsight recall error:",
            repr(e)
        )

        raise