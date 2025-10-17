import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- Import our crew's factory function ---
from multi_agent_pattern_agent.blog_crew import create_blog_writing_crew

# --- Load Environment Variables ---
load_dotenv()

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- API Contract (Pydantic Models) ---
class CrewRequest(BaseModel):
    topic: str = Field(
        ...,
        description="The topic for the blog post the crew should write.",
        example="The future of AI agents"
    )

class CrewResponse(BaseModel):
    final_result: str

# --- FastAPI Application Setup ---
app = FastAPI(
    title="Multi-Agent Crew Service",
    description="An API to orchestrate a crew of AI agents for writing blog posts.",
    version="1.0.0"
)

# --- API Endpoints ---
@app.get("/health", tags=["Monitoring"])
def health_check():
    """Checks if the service is running."""
    return {"status": "ok"}

@app.post("/run-crew", response_model=CrewResponse, tags=["Agent Crew"])
def execute_crew_run(request: CrewRequest):
    """
    Assembles and runs the blog writing crew for a given topic.
    """
    try:
        logger.info(f"Received request to run crew for topic: '{request.topic}'")
        
        # Engineering Mindset: We use our factory function to assemble the crew.
        crew = create_blog_writing_crew(request.topic)
        
        final_result = crew.run()

        logger.info("Successfully completed crew run.")
        return CrewResponse(final_result=final_result)
        
    except Exception as e:
        logger.exception("An unhandled exception occurred during crew run.")
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")