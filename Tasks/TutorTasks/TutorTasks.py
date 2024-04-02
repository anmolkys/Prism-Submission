from crewai import Task

# Styling
from textwrap import dedent

from datetime import datetime


language = ""

class TutorTasks():
  
   def create_plan(self, agent, context):
      
      date = datetime.now() 

      date_str = date.strftime('%Y-%m-%d')

      return Task(
         
        description=dedent(f"""\
                           
        Based on the given {context}, create a month long plan by dividing topics in order and assign it to a day everyday other than 
        weekend from

        {date_str}

        Make a plan in the perfect order for the user to understand easily. These topics are to be scheduled.
        Your final answer MUST be a list of topics along with the corresponding dates. Use bullet points in heirarichal manner. The final list must include:
        - Topic
        - Date
        - a small discription on the topic

        {self.__tip_section()}

        """),

        agent = agent, 
    ) 
   
   def start_teach(self, agent):
      
      return Task(
         
       description=dedent(f"""\
                          
       Based on the topic from `fetch_events_task`, use the tool to explain the topic in a detailed manner.
      The input to the tool must be only the name of the topic. For example: Eigenvectors and eigenvalues.
      Your final answer MUST be multiple passage with subheadings explaing every part of the topic clearly.
      {self.__tip_section()}
      Return output in {language} 
      After the reuslts are displayed put the code to sleep using the tool.

      """),
      
      agent = agent, 
      tools = []
    ) 


   def get_result(agent):
      
      return Task(
         
       description=dedent(f"""\
                          
        Get results stored in the database.
        Your final answer MUST be a list of bullet points.
        - Topic
        - Score
        Return output in {language}

      """),
      agent = agent, 
    ) 
   
   def ref_video(agent):
      
      return Task(
         
        description=dedent(f"""\
        Based on the topic from `startTeach`, search videos on youtube using the given tool. The input to the tool must be only 
        the topic name.
        """),
        agent = agent, 
    ) 


   def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"
