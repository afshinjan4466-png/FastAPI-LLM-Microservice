"""
FastAPI LLM Microservice
Main entry point for the high-performance asynchronous AI backend service.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn


app = FastAPI(
    title="FastAPI LLM Microservice",
    description="Production-ready microservice wrapping LLM capabilities with Pydantic validation.",
    version="1.0.0"
)


class PromptRequest(BaseModel):
    prompt: str = Field(..., description="The input prompt for the LLM pipeline", example="Explain microservices in one sentence.")
    max_tokens: int = Field(default=150, description="Maximum tokens for generation")


class PromptResponse(BaseModel):
    status: str
    original_prompt: str
    generated_response: str


@app.get("/")
def health_check():
    """Health check endpoint to verify service status."""
    return {"status": "healthy", "service": "FastAPI-LLM-Microservice"}


@app.post("/v1/generate", response_model=PromptResponse)
def generate_text(request: PromptRequest):
    """
    Simulates an asynchronous LLM generation endpoint with strict validation.
    """
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    # Simulated response generation
    simulated_output = f"Processed successfully: '{request.prompt}' translated into structured LLM output."
    
    return PromptResponse(
        status="success",
        original_prompt=request.prompt,
        generated_response=simulated_output
    )


if __name__ == "__main__":
    # Run the application locally for testing
    uvicorn.main(["main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])
