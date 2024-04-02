# Use any llm of choice

manager_llm = " "

#                           The Researching and Writing Crew

# We will Now talk about the Researching and Writting Crew. This crew has 4 agents 
# - Research agent - researchs online and browses information and retreives it to writer agent
# - Writer agents formats and the information and organizes the and filters out the nessassary information 


#Google Scholar Agents is being used 
# -help researchers find and manage scholarly articles more efficiently
# -searching, analyzing, and organizing academic literature 

#File Writer Agent is also being used
# -This agent is responsible for writing data or information to files
#- facilitating data storage and management operations

# The summarizer can read any file provided the path and summarizr its contents

from Agents.AssignmentAgents.AssignmentAgents import ResearchAgent

writer = ResearchAgent.writer_agent()
researcher = ResearchAgent.researcher_agent()
typer = ResearchAgent.typer()
summarizer = ResearchAgent.summarizer()
finder = ResearchAgent.finder()

from Tasks.AssignmentTasks.AssignmentTask import ResearchTask

file_path_to_summarize = ""
file_path_to_write_to = ""
topic = ''

write_task = ResearchTask.write_task(writer, topic)
research_task = ResearchTask.write_task(researcher, topic)
type_task = ResearchTask.save_file(typer, file_path_to_write_to)
summarize_task = ResearchTask.write_task(summarizer, file_path_to_summarize)
find_task = ResearchTask.write_task(finder, topic)

from crewai import Crew, Process
  
ResearchCrew =  Crew(
      
      agents=[researcher, writer, typer, summarizer, finder],
      tasks=[research_task, write_task, type_task, summarize_task, find_task],
      process=Process.sequential
  )

result = ResearchCrew.run()
print(result)