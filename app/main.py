from fastapi import FastAPI
from app.routes import llm


BASE_URL = "/api/v1"
API_VERSION = "1.0.0"

app = FastAPI(prefix=BASE_URL,
              title="AI Debate Trainer API",
              description="API for AI Debate Trainer",
              version=API_VERSION,
              openapi_url=f"{BASE_URL}/openapi.json",
              docs_url=f"{BASE_URL}/docs")

@app.get("/")
def read_root():
    return {"message": "AI Debate Trainer Backend is running."}

app.include_router(llm.router, prefix=f"{BASE_URL}/llm")
