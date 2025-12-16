# sub_agents/risks_agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

risk_analyst_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="risk_analyst_agent",
    description="A compliance and risk specialist focused on identifying potential regulatory changes, zoning risks, and legal compliance issues using Google Search.",
    instruction="""
        You are the Regulatory Risk Analyst. Use the 'google_search' tool to find and summarize 
        current and proposed regulatory risks, zoning restrictions, and compliance issues 
        relevant to the user's query.
    """,
    tools=[google_search]
)