# sub_agents/demographics_agent.py
from google.adk.agents import LlmAgent
import json

def get_demographics(location: str) -> str:
    """
    Retrieves key demographic statistics (population, income, age) for a city.
    
    Args:
        location: The city or region (e.g., 'Austin', 'Seattle').
        
    Returns:
        A JSON string of key demographic metrics.
    """
    if "austin" in location.lower():
        data = {"city": "Austin, TX", "population": 978000, "median_income": 75000, "avg_age": 34.5}
    else:
        data = {"error": f"Demographic data for {location} not available."}
    return json.dumps(data)

demographics_analyst_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="demographics_analyst_agent",
    description="An expert for retrieving, analyzing, and summarizing detailed demographic data, population figures, and income statistics for specific locations.",
    instruction="""
        You are the Demographics Specialist. Use the 'get_demographics' tool to find the required
        data and provide a clear summary, ensuring you specify the location.
    """,
    tools=[get_demographics]
)