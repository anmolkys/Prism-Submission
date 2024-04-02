# Use your llm of choice.
llm = ""

# import Agent class from crew ai.
from crewai import Agent

# Styling
from textwrap import dedent

from Tools.GoogleTools.CalenderTools import CalenderEventTool


class CalendarAgents():

    def calender_fetch_agent():
          
          return Agent(
             role='Senior calender retreiver',
             goal='Fetch all upcoming events',

             backstory=dedent("""\
             You're an efficient digital assistant specialized in retrieving calendar events swiftly and accurately. 
             Your knack for understanding scheduling nuances enables you to effortlessly access upcoming appointments, 
             provide reminders for important meetings, and furnish details about scheduled events."""),

             verbose = True,
             allow_delegation=False,
             llm = llm
          )
       
    def calender_scheduler_agent():
          
          return Agent(
             role='Senior calender scheduler',
             goal='Schedule events',

             backstory=dedent("""\
             Efficient and precise, You specialize in seamlessly adding events to calendars. 
             Whether it's scheduling meetings or setting reminders, your expertise ensures accurate and hassle-free event creation. 
             With tailored responses and intuitive assistance, users can effortlessly manage their commitments with ease."""),

            tools = [
               CalenderEventTool.create_event  # Custom tool to schedule events in calender
            ],
            
             verbose = True,
             allow_delegation=False,
             llm = llm
          )