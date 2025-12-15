# sub_agents/property_agent.py
from google.adk.agents import LlmAgent
import json

def get_property_data(property_address: str) -> str:
    """
    Retrieves the full details (price, beds, baths) for a specific property address.
    
    Args:
        property_address: The address (e.g., '123 Main St') of the property.
        
    Returns:
        A JSON string containing property details.
    """
    if "123 main st" in property_address.lower():
        data = {"address": "123 Main St, Anytown", "price": 550000, "beds": 3, "baths": 2, "sqft": 1800}
    else:
        data = {"error": f"Property details for {property_address} not found in the database."}
    return json.dumps(data)

PropertyDetailsAgent = LlmAgent(
    model="gemini-2.0-flash",
    name="PropertyDetailsAgent",
    description="An expert agent for fetching specific details, prices, and features of a known property.",
    instruction="""
        You are the Property Details Specialist. Your task is to use the 'get_property_data' tool
        to retrieve and summarize information about a property based on its address.
    """,
    tools=[get_property_data]
)