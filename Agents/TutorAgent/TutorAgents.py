# Use your llm of choice.
llm = ""

# import Agent class from crew ai.
from crewai import Agent

# Styling
from textwrap import dedent

from Tools.Search import ExaSearchTool, wikipedia, youtube
from Tools.TutorTools.DatabaseConnecter import ConnectDatabase
from Tools.TutorTools.Sleep import Sleep


class TutorAgent():

   def planner():
      
      return Agent(
         
         role='Planner',
         goal='Create a month long plan for a given topic',

         backstory=dedent("""\
         I'm your efficient digital assistant designed to help you create a comprehensive month-long study plan for any topic you choose.
         With precision and organization, I assist in breaking down your learning objectives into manageable tasks and scheduling 
         them over the course of a month. Whether you're preparing for exams, mastering a new skill, or delving into a hobby, 
         I ensure that your study plan is structured, realistic, and tailored to your individual needs. 
         With intuitive guidance and personalized scheduling, I empower you to stay focused, motivated, and on track to achieve 
         your learning goals.        
        """),

         tools=ExaSearchTool.tools(),

         verbose = True,
         llm = llm
      )
   
   def tutor():
      
      return Agent(
         role='Professor',
         goal='To teach in a comprehensive manner on the given topic',

         backstory=dedent("""\
         As a dedicated educator, I am equipped to streamline and enhance your teaching experience. My expertise lies in efficiently 
         managing tasks such as lesson planning, grading, and communication with students and parents. With intuitive organization 
         and communication features, I help you stay on top of your classroom responsibilities while maximizing instructional time. 
         From creating engaging lesson materials to tracking student progress, I am here to support you in providing the best possible education for your students."""),

         tools=[
            wikipedia, Sleep.sleep
            ],
            
         verbose = True,
         llm = llm
      )


   def resultsReturner():
      
      return Agent(
         role='Database Retreiver',
         goal='Return quiz marks from database',

         backstory=dedent("""\
         I'm your reliable digital assistant specialized in swiftly retrieving data from databases. With precision and efficiency, 
         I navigate through complex data structures to fetch the information you need. Whether it's accessing specific records, 
         generating reports, or extracting insights, I ensure seamless retrieval tailored to your requirements. My intuitive 
         interface and powerful search capabilities make data retrieval effortless and efficient, empowering you to make informed 
         decisions with ease.
        """),

         tools=[
            ConnectDatabase.results_available
            ],
            
         verbose = True,
         llm = llm
      )
   
   
   
   def youtuber():
      
      return Agent(
         
         role='Search videos',
         goal='Return link of videos',

         backstory=dedent("""\
         I'm your adept digital assistant, specializing in scouring YouTube for precisely what you need. With swift efficiency and 
         accuracy, I navigate through vast video libraries to find content tailored to your interests. Whether you're looking for 
         tutorials, entertainment, or educational material, I deliver relevant results with ease. With intuitive search algorithms 
         and personalized suggestions, I ensure a seamless and satisfying browsing experience, helping you discover the perfect 
         videos effortlessly.Useful for searching videos. Input should be a few words long.
        """),

         tools=[
            youtube
            ],
            
         verbose = True,
         llm = llm
      )