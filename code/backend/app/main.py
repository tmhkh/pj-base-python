from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import get_settings
from .schemas import MessageRequest, MessageResponse

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

# Allow local dev origins by default; adjust in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Simple health check endpoint."""

    return {"status": "ok"}


@app.post(f"{settings.api_v1_prefix}/messages/echo", response_model=MessageResponse, tags=["messages"])
def echo_message(payload: MessageRequest) -> MessageResponse:
    """Return the submitted message back to the caller."""

    return MessageResponse(echo=payload.text)


# Serve frontend static files in production (if dist folder exists)
frontend_dist = Path(__file__).parent.parent.parent / "frontend" / "dist"
if frontend_dist.exists() and settings.app_env == "production":
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="frontend")
