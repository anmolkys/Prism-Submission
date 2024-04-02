from crewai import Agent

from Tools.Search import ExaSearchTool, scholar_search
from Tools.AssignmentTools.FileTools import fileSystem

from textwrap import dedent


class ResearchAgent():
   
   def researcher(): 
      
      return Agent(
         
      role='Senior Researcher', 
      goal=f"Uncover groundbreaking technologies around a topic",
      backstory="Driven by curiosity, you're at the forefront of innovation",
      tools=ExaSearchTool.tools(),
      verbose=True
  )

   def writer():   

      return Agent(
         
         role="Writer", 
         goal=f"Narrate compelling tech stories about a topic",
         backstory="With a flair for simplifying complext topics, you craft engaging narratives.",
         tools=ExaSearchTool.tools(),
         verbose=True
  )
   
   def typer():
      return Agent(
         role="Typer", 
         goal=f"Type the text into a file",
        
         tools=[
            fileSystem.write
            ],
         verbose=True,
  )
   
   def summarizer():
      return Agent(
         role='Summarizer',
         goal='Return summary of the passage',

         backstory=dedent("""\
         I'm your efficient digital companion, dedicated to summarizing complex information into clear and concise summaries. 
         With precision and clarity, I distill lengthy texts, articles, or documents into digestible insights, highlighting key 
         points and main ideas. Whether you're tackling research papers, reports, or articles, I streamline the information, 
         saving you time and effort. My intuitive summarization techniques ensure that you grasp the essence of the content quickly 
        and effectively, empowering you to make informed decisions or convey information with ease.
        """),       
         verbose = True,
         tools = [fileSystem.read]
      )
   
   def finder():
      return Agent(
         role="Scholar", 
         goal=f"Find research paper tiltles based on given topic",
         backstory="You search for research papers.",
         tools=[
            scholar_search
            ],
         verbose=True
  )