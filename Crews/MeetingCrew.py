#                                           Student Meeting Planner 


# Student Meeting Planner is the next Crew. It consists of 4 agents:
# -researcher_agent: This agent is responsible for conducting research, browsing through online sources, and gathering relevant information based on the given context and participants.
# -industry_analyst_agent: The industry_analyst_agent specializes in analyzing industry trends, market data, and relevant reports to provide insights and perspectives tailored to the participants and context.
#- meeting_strategy_agent: this agent focuses on devising effective meeting strategies, considering the given context and objective. It may suggest agenda items, discussion topics, and approaches to ensure productive meetings.
# -summary_and_briefing_agent: The summary_and_briefing_agent compiles and synthesizes the collected information, research findings, and meeting strategies into concise summaries and briefings for the participants, facilitating effective communication and decision-making.

from Agents.MeetingAgents.MeetingAgents import MeetingPreparationAgents

#initialize the agents
researcher_agent = MeetingPreparationAgents.research_agent()
industry_analyst_agent = MeetingPreparationAgents.industry_analysis_agent()
meeting_strategy_agent = MeetingPreparationAgents.meeting_strategy_agent()
summary_and_briefing_agent = MeetingPreparationAgents.summary_and_briefing_agent()

from Tasks.MeetingTasks.MeetingTasks import MeetingPreparationTasks

participants = input("What are the emails for the participants (other than you) in the meeting?\n")
emails_array = participants.split(',')
emails_array = [email.strip() for email in emails_array]

##context
context = input("What is the context of the meeting?\n")

#objective
objective = input("What is your objective for this meeting?\n")

#intialize the tasks
research = MeetingPreparationTasks.research_task(researcher_agent, participants, context)
industry_analysis = MeetingPreparationTasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = MeetingPreparationTasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = MeetingPreparationTasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

from crewai import Crew

#Here we're creating a Crew to coordinate the agents and tasks involved in the research, analysis, and briefing process.
Meeting = Crew(

    # List of agents participating in the Crew
    agents=[
        researcher_agent,  
        industry_analyst_agent, 
        meeting_strategy_agent,  
        summary_and_briefing_agent 
    ],

    # List of tasks assigned to the Crew:
    tasks=[
        research,  # Task assigning the researcher_agent to conduct research.
        industry_analysis,  # Task assigning the industry_analyst_agent to perform industry analysis.
        meeting_strategy,  # Task involving the meeting_strategy_agent in developing meeting strategies.
        summary_and_briefing  # Task assigning the summary_and_briefing_agent to create summaries and briefings.
    ]
)


result = Meeting.kickoff()
print(result)