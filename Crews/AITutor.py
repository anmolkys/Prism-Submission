# Use any llm of choice

manager_llm = " "

#                                                          The AI Tutor

# Many students like to study on their own as they prefer control over their schedule but also like a person to explain topics clearly with examples
# and regularly question them to keep track of content. So how about a teacher in the palm of your hands? I mean who else will explain indefinetly and 
# clear doubts at any time?? Here we are going to use the power of transformers to assemble a crew of agents that will accomplish this.
# - A subject usually takes months to complete. So we need an agent to split into topics coverable in a day and schedule them in the calender.
#   The planner agent will create a month long schedule for a given subject and pass to scheduler agent to schedule the topic in the calender.
# - The tutor agent will explain the topic received from retreiver agent for the given grade level.
# - For the given topic after explanation, a quiz will be conducted and the results will be stored in a database. These results can be accesed by the 
#   planner agent if a topic needs to be revised. The reults agent has access to the database.
# - It is easier to learn through video so after explanation, the youtube agent will search through youtube and output an url which can be refered

from Agents.TutorAgent.TutorAgents import TutorAgent
from Agents.EmailAgents.CalenderAgents import CalendarAgents

#Initialize the three agents
planning_agent = TutorAgent.planning_agent()
tutor_agent = TutorAgent.tutor_agent()
results_agent = TutorAgent.results_agent()
youtube_agent = TutorAgent.youtube_agent()

scheduler_agent = CalendarAgents.calender_scheduler_agent()

subject = ""

from Tasks.TutorTasks.TutorTasks import TutorTasks
from Tasks.EmailTasks.CalenderTasks import  CalenderTasks

#Initialize the tasks for each agent
create_plan = TutorTasks.create_plan(planning_agent, subject) # Here we pass on subject as a named parameter.
start_teach = TutorTasks.start_teach(tutor_agent)
get_results = TutorTasks.get_results(results_agent)
get_video = TutorTasks.ref_videos(youtube_agent)

schedule_task = CalenderTasks.schedule_events_task(scheduler_agent)


from crewai import Crew, Process

# Form the crew. The crew consists of the three agents and a manager to oversee the work. The manger will oversee if process = hierarchical.
# The crew will be put to sleep for 15mins between tutor_agent and results_agent inorder to conduct the quiz.
ai_tutor = Crew(
    agents=[planning_agent, scheduler_agent, tutor_agent, results_agent, youtube_agent],
    tasks=[create_plan, schedule_task, start_teach, get_results, get_video],
    process=Process.hierarchical,
    manager_llm= manager_llm
)

# Kickoff the crew
result = ai_tutor.kickoff()
print(result)


from Tools.TutorTools.Quiz import startQuiz

startQuiz()  # This will run streamlit application in the back. Ctrl click the url to launch the quiz. During this time the crew will be put to sleep.


# The above crew will function well if they are theory related subjects but what if coding is involved? So here we integrate our AI coder niicknamed 
#                                                         Tiny Devin.

from Agents.TutorAgent.TinyDevien import CodingAgents

scrapper = CodingAgents.documentationReader()
coder = CodingAgents.coder()

from Tasks.TutorTasks.DevinTasks import CodeTasks

analyse = CodeTasks.analysis()
code = CodeTasks.code()

Devin = Crew(
    agents=[scrapper, coder],
    tasks=[analyse, code],
    process=Process.sequential,
    manager_llm= manager_llm
)