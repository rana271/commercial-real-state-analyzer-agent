# sub_agents/trends_agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

trends_analyst_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="trends_analyst_agent",
    description="A specialist agent for researching and summarizing current real estate market trends, news, and financial forecasts using up-to-date web search.",
    instruction="""
        You are the Market Trends Analyst. You MUST use the 'google_search' tool to find the 
        latest trends and synthesize them into a concise, numbered list for the user.
    """,
    tools=[google_search] 
)