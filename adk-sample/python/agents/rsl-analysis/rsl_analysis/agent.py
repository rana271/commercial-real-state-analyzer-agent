# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Financial coordinator: provide reasonable investment strategies."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.property_agent import get_property_data
from .sub_agents.demographics_agent import get_demographics
from .sub_agents.risk_analyst import risk_analyst_agent
from .sub_agents.trading_analyst import trading_analyst_agent

MODEL = "gemini-2.0-flash"


financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "guide users through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. help them "
        "analyze a market ticker, develop trading strategies, define "
        "execution plans, and evaluate the overall risk."
    ),
   instruction="""
        You are the Main Investment Advisor. Your primary and most important role is to analyze the user's
        query and **delegate** the request to the single most appropriate specialized sub-agent.
        
        1. **Property Details:** Delegate if the user asks for specific property data (price, beds, baths).
        2. **Market Trends:** Delegate if the user asks for market forecasts, news, or general trends.
        3. **Demographics:** Delegate if the user asks for population, income, or age data for a location.
        4. **Regulatory Risks:** Delegate if the user asks about zoning, legal compliance, or new regulations.
        5. **Synthesis:** If a query requires combining multiple pieces of information, delegate to the first relevant agent and then synthesize the final answer yourself.
    """,

    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=get_property_data),
        AgentTool(agent=trading_analyst_agent),
        AgentTool(agent=get_demographics),
        AgentTool(agent=risk_analyst_agent),
    ],
)

root_agent = rsl_analysis
