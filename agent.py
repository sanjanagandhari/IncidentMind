import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

groq_client = None

if GROQ_API_KEY:
    try:
        groq_client = Groq(
            api_key=GROQ_API_KEY
        )
    except Exception as e:
        print(f"Groq initialization failed: {e}")


def build_memory_context(memories):
    """Convert recalled memories into readable AI context."""

    if not memories:
        return "No historical incidents were found."

    sections = []

    for index, memory in enumerate(memories, start=1):

        text = memory.get("text", "")

        metadata = memory.get(
            "metadata",
            {}
        ) or {}

        semantic_score = memory.get(
            "semantic_score"
        )

        if semantic_score is not None:
            score_text = f"{semantic_score * 100:.1f}%"
        else:
            score_text = "unknown"

        sections.append(
            f"""
Historical Incident {index}

Match score:
{score_text}

Memory:
{text}

Metadata:
{metadata}
"""
        )

    return "\n".join(sections)


def fallback_analysis(incident, memories):
    """Fallback response if Groq is unavailable."""

    if memories:
        first = memories[0]

        return f"""
Probable Root Cause:
A similar historical incident was found in IncidentMind memory.

Recommended Fix:
Review the historical incident below and compare its root cause and fix with the current incident.

Historical Evidence:
{first.get("text", "No historical details available.")}

Post-Incident Investigation:
Check application logs, deployment history, CPU and memory usage, database health, disk usage, and recent configuration changes.

Prevention:
Add monitoring, alert thresholds, health checks, and automated incident detection for this failure pattern.
"""

    return f"""
Probable Root Cause:
The exact root cause cannot be determined yet from the available information.

Recommended Fix:
Inspect application logs, infrastructure metrics, recent deployments, database status, memory usage, CPU usage, disk usage, and network connectivity.

Post-Incident Investigation:
Identify the first timestamp of the failure and correlate it with deployments, configuration changes, resource usage, and service logs.

Prevention:
Add appropriate monitoring, alerting, health checks, and automated recovery procedures.
"""


def analyze_incident(incident, memories):
    """Analyze an incident using Groq and Hindsight memories."""

    memory_context = build_memory_context(memories)

    if not groq_client:
        return fallback_analysis(
            incident,
            memories
        )

    prompt = f"""
You are IncidentMind, an AI assistant for infrastructure
and production incident investigation.

Current Incident:
{incident}

Historical incidents retrieved from organizational memory:
{memory_context}

Analyze the current incident using the historical incidents
when they are relevant.

Give the response in exactly these sections:

Probable Root Cause:
Explain the most likely cause.

Recommended Fix:
Give practical steps to resolve the incident.

Post-Incident Investigation:
Explain what the engineer should investigate after recovery.

Prevention:
Explain how this type of incident can be prevented.

Historical Evidence:
Mention relevant historical incidents and explain how
they relate to the current incident.

Important:
Do not invent historical incidents.
Only use the memories supplied above.
"""

    try:

        response = groq_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a production infrastructure "
                        "incident analysis assistant."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"Groq analysis failed: {e}")

        return fallback_analysis(
            incident,
            memories
        )