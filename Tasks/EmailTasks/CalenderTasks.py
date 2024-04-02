from crewai import Task

# Styling
from textwrap import dedent

language = ""

class CalenderTasks():

    def schedule_events_task(agent):

        return Task(

            description=dedent(f"""\
                Analyze the message and schedule the events appropriatly. If some action-required emails that need scheduling is identiied schedule those events too.
                Use the tool provided to schedule events. When using the tool pass the following input:
                -summary
                -location if applicabe
                - description
                -start time
                -end time if applicabe
                -attendees
                Your final answer MUST be a confirmation that all schedules have been scheduled.
                Return output in {language}
                """),
                agent = agent,
            ) 
    

    def fetch_events_task(self, agent, events):

        return Task(

            description=dedent(f"""\
            Analyze all the upcoming events.  
            Events
            -------
            {events}

            Your final answer MUST be a list of event. Use bullet point
            For every event give, Sno. The name of the event date(dd-mm-yy format) time(hours:minutes format) Discription
            The output should be neat.
            Return output in {language}
            """),
            agent = agent, 
        ) 