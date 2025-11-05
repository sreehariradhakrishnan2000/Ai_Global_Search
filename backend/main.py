from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI(title="Global AI Search API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data for demonstration
mock_data = [
    {"id": 1, "title": "User Profile", "description": "View user details", "type": "user", "keywords": ["user", "profile", "details"]},
    {"id": 2, "title": "Settings", "description": "Application settings", "type": "page", "keywords": ["settings", "config", "preferences"]},
    {"id": 3, "title": "Messages", "description": "Recent messages", "type": "message", "keywords": ["messages", "chat", "communication"]},
    {"id": 4, "title": "Appointments", "description": "Today's appointments", "type": "appointment", "keywords": ["appointments", "schedule", "calendar"]},
    {"id": 5, "title": "Sreehari User", "description": "User named Sreehari", "type": "user", "keywords": ["sreehari", "user"]},
]

def simple_ai_interpret(query: str) -> list:
    """
    Simple AI interpretation: extract keywords and match against mock data.
    In a real implementation, this would use NLP models like spaCy or GPT.
    """
    query_lower = query.lower()
    results = []

    # Basic keyword matching
    for item in mock_data:
        if any(keyword in query_lower for keyword in item["keywords"]):
            results.append(item)

    # If no matches, try fuzzy matching or return general results
    if not results:
        # For queries like "show me today's appointments"
        if "appointment" in query_lower or "today" in query_lower:
            results = [item for item in mock_data if "appointment" in item["keywords"]]
        elif "setting" in query_lower or "open setting" in query_lower:
            results = [item for item in mock_data if "settings" in item["keywords"]]
        elif "user" in query_lower:
            results = [item for item in mock_data if "user" in item["keywords"]]

    return results

@app.get("/search")
async def search(q: str):
    """
    Search endpoint that interprets natural language queries.
    """
    if not q:
        return {"results": []}

    # Use AI interpretation to get results
    results = simple_ai_interpret(q)

    return {"results": results}

@app.get("/")
async def root():
    return {"message": "Global AI Search API"}
