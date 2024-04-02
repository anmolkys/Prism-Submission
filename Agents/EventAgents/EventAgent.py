llm = ""

from crewai import Agent

from Tools.Search import ExaSearchTool

class TripPlannerAgents:
  
  def city_selection_agent(self):

    return Agent(
      role="City Selection Expert",
      goal="Select the best city based on wather, season, and prices",
      backstory="An expert in analyzing travel data to pick ideal destination",
      tools=ExaSearchTool.tools,
      verbose=True,
      llm=llm
    )

  def local_expert(self):

    return Agent(
      
      role="Local Expert at this city",
      goal="Provide the best insights about the selected city",
      backstory=""" 
        A knowledgeable local guide with extensive information about the city, it's attractions and customs
      """,
      tools=ExaSearchTool.tools,
      verbose=True,
      llm=llm
    )

  def travel_concierge(self):

    return Agent(
      
      role="Amazing travel concierge",
      goal="""
        Create the most amazing travel itineraries with budget and packing suggestions for the city
      """,
      backstory="Specialist in travel planning and logistics",
      tools=ExaSearchTool.tools,
      verbose=True,
      llm=llm
    )