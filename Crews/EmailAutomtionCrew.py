# Use any llm of choice

manager_llm = " "

#                                                   The Email Automation Crew

# We will first start with the Email automation crew. This crew has 3 agents:
# - The filter agent scans the inbox for spams and notifications and pass along the Thread id and a gist of the mail to the next agent. 
# - The action_required agent receives the thread ids of important mails and goes through them to check if any response or action is needed.
# - The draft agent creates a draft mail as responses and stores them in the draft folder.


from Tools.GoogleTools.GmailTools import fetch_mails

# Using the gmail api, we fetch all the mails and store it in a variable.
emails = fetch_mails()

from Agents.EmailAgents.GmailAgents import GmailAgents

#Initialize the three agents
filter_agent = GmailAgents.email_filter_agent()
action_agent = GmailAgents.email_action_agent()
drafter_agent = GmailAgents.email_response_writer()

from Tasks.EmailTasks.GmailTasks import GmailTasks

#Initialize the tasks for each agent
filter_task = GmailTasks.filter_emails_task(filter_agent, emails) # Here we pass on the emails as a named parameter.
action_required_task = GmailTasks.action_required_emails_task(action_agent)
draft_response_task = GmailTasks.draft_response_task(drafter_agent)

from crewai import Crew, Process

# Form the crew. The crew consists of the three agents and a manager to oversee the work. For small and straight forward tasks like this a manager is 
# not needed. The manger will oversee if process = hierarchical
email_automation_crew = Crew(
    agents=[filter_agent, action_agent, drafter_agent],
    tasks=[filter_task, action_required_task, draft_response_task],
    process=Process.hierarchical,
    manager_llm= manager_llm
)

# Kickoff the crew
result = email_automation_crew.kickoff()
print(result)



# This automates the email filtering and response process. But what if a response is not needed? Most of the mails we receive are for events 
# saying so and so happening on so and so date. But amongst all this junk we also receive important dates such as for Internals schedule which we probaly 
# might miss. So to take it up a notch we are going to integrate mail with the calender. So here we introduce our new agents Scheduler and Retriver:
# - scheduler schedules events based on user query or from `action agent` ie from the mails
# - retreiver retreives the top 10 upcoming events from our calender. We can pass on a query to filter the outcome

from Tools.GoogleTools.CalenderTools import fetch_calender_events

# Using the calender api, we fetch all the events and store it in a variable.
events = fetch_calender_events()

from Agents.EmailAgents.CalenderAgents import CalendarAgents

#Initialize the two agents
scheduler_agent = CalendarAgents.calender_scheduler_agent()
retreiver_agent = CalendarAgents.calender_fetch_agent()

from Tasks.EmailTasks.CalenderTasks import CalenderTasks

#Initialize the tasks for the agent
retreive_task = CalenderTasks.fetch_events_task(retreiver_agent, events) # Here we pass on the events as a named parameter.
schedule_task = CalenderTasks.schedule_events_task(scheduler_agent)

email_automation_crew = Crew(
    agents=[filter_agent, action_agent, scheduler_agent, drafter_agent, retreiver_agent],
    tasks=[filter_task, action_required_task, schedule_task, draft_response_task, retreive_task],
    process=Process.hierarchical,
    manager_llm= manager_llm
)

# Kickoff the crew
result = email_automation_crew.kickoff()
print(result)


# This concludes one portion of the project.