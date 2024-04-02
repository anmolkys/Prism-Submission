from crewai import Task

language = ""

class ResearchTask():
   
   def research_task(self, agent, topic):
      
      return Task(
         
      description=f"""
        Identify the next big trend in {topic}.
        Focus on identifying pros and cons and the overall narrative.

        Your final report should clearly articulate the key points, 
        its market opportunities, and potential risks.
        {self.__tip_section()}
        Return output in {language}
      """,

      expected_output=" A 3 paragraphs long report on the latest AI trends.", 
      max_iter=1,  
      agent=agent
  )

   def write_task(self, agent, topic): 

    return Task(
       
        description=f"""
          Compose an insightful article on {topic}.
          Focus on the latest trends and how it's impacting the industry.
          This article should be easy to understand, engaging and positive.
          {self.__tip_section()}
          Return output in {language}
        """,

        expected_output=f"A 4 paragraph article on {topic} advancements", 
        agent=agent
    )
   
   def save_file(self, agent, file_path_to_write_to):
      
      return Task(
         
        description=f"""
            Save the result from `write_task` in the file {file_path_to_write_to} using the tool.
            {self.__tip_section()}
          """,
        agent=agent
        )
   
   def summarize(self, agent, path):
      
      return Task(
         
        description=f"""
            From the given path {path}, read the file and summarize the txt in about 300 words. The input to the tool must 
            be the path only.
            {self.__tip_section()}
            Return output in {language}
          """,

        agent=agent
        )
   
   def find_paper(self, agent, topic):
      return Task(
        description=f"""
            Find a paper related to {topic}.
            {self.__tip_section()}
          """,
        agent=agent
        )

   
   def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"