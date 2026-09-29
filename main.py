from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import traceback

from backend.hindsight_service import recall_incidents, store_incident
from backend.agent import analyze_incident


app = FastAPI(
    title="IncidentMind API",
    description="AI-powered incident memory and analysis system",
    version="0.1.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Request Models
# --------------------------------------------------

class Incident(BaseModel):
    description: str
    use_memory: bool = True


class Feedback(BaseModel):
    incident: str
    feedback: str
    actual_root_cause: str = ""
    actual_fix: str = ""
    resolution_time: str = ""


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "IncidentMind API is running"
    }


# --------------------------------------------------
# Analyze Incident
# --------------------------------------------------

@app.post("/analyze")
def analyze(data: Incident):

    try:

        # ------------------------------------------
        # Recall historical incidents
        # ------------------------------------------

        if data.use_memory:
            memories = recall_incidents(
                data.description
            )
        else:
            memories = []


        # ------------------------------------------
        # AI Analysis
        # ------------------------------------------

        answer = analyze_incident(
            data.description,
            memories
        )


        # ------------------------------------------
        # Response
        # ------------------------------------------

        return {
            "incident": data.description,
            "memory_used": data.use_memory,
            "memory_count": len(memories),
            "matched_incidents": memories,
            "analysis": answer
        }


    except Exception as e:

        print("\n================================")
        print("ERROR IN /analyze")
        print("================================")

        traceback.print_exc()

        print("================================\n")

        return {
            "error": str(e),
            "type": type(e).__name__
        }


# --------------------------------------------------
# Feedback / Learning
# --------------------------------------------------

@app.post("/feedback")
def save_feedback(data: Feedback):

    try:

        memory = f"""
Resolved Incident

Incident:
{data.incident}

Engineer Feedback:
{data.feedback}

Actual Root Cause:
{data.actual_root_cause}

Actual Fix:
{data.actual_fix}

Resolution Time:
{data.resolution_time}
"""

        success = store_incident(
            memory,
            metadata={
                "source": "engineer_feedback",
                "feedback": data.feedback,
                "actual_root_cause": data.actual_root_cause,
                "actual_fix": data.actual_fix,
                "resolution_time": data.resolution_time
            }
        )

        return {
            "message": "Feedback saved to Hindsight",
            "status": "learning",
            "stored": success
        }


    except Exception as e:

        print("\n================================")
        print("ERROR IN /feedback")
        print("================================")

        traceback.print_exc()

        print("================================\n")

        return {
            "error": str(e),
            "type": type(e).__name__
        }