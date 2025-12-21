from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    """Payload schema for message echo requests."""

    text: str = Field(..., description="Message submitted by the client")


class MessageResponse(BaseModel):
    """Response schema returning the echoed message back to the client."""

    echo: str = Field(..., description="Echoed message for confirmation")
