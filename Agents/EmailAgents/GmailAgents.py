# Use your llm of choice.
llm = ""

# import Agent class from crew ai.
from crewai import Agent

# Styling
from textwrap import dedent

from Tools.Search import ExaSearchTool
from Tools.GoogleTools.GmailTools import CreateDraftTool, api_resource
from langchain_community.tools.gmail.get_thread import GmailGetThread



class GmailAgents():
       
# This agent filters mail
       
       def email_filter_agent(): 

        return Agent(
            role='Senior Email Analyst',
            goal='Filter out non-essential emails like newsletters and promotional content',
            backstory=dedent("""\
				As a Senior Email Analyst, you have extensive experience in email content analysis.
				You are adept at distinguishing important emails from spam, newsletters, and other
				irrelevant content. Your expertise lies in identifying key patterns and markers that
				signify the importance of an email."""),
            verbose=True,
            llm = llm
        )
       
# This agent filters mail
       
       def email_action_agent(): 

        return Agent(
            role='Email Action Specialist',
            goal='Identify action-required emails and compile a list of their IDs',
            backstory=dedent("""\
            With a keen eye for detail and a knack for understanding context, you specialize
            in identifying emails that require immediate action. 
            Your skill set includes interpret the urgency and importance of an email based on its content and context."""),
            tools=[
                GmailGetThread(api_resource=api_resource()), # This tool gets mail using thread ids from inbox
                
            ],
            verhose=True,
            llm = llm
        )
       
# This agent drafts mail
       
       def email_response_writer():

        return Agent(

            role='Email Response Writer',
            goal='Draft responses to action-required emails',
            backstory=dedent("""\
            You are a skilled writer, adept at crafting clear, concise, and effective email responses. 
            Your strength lies in your ability to communicate effectively, 
            ensuring that each response is tailored to address the specific needs and context of the email."""),

            tools=[
                ExaSearchTool.search,
                GmailGetThread(api_resource=api_resource()),    # This tool gets mail using thread ids from inbox
                CreateDraftTool.create_draft                    # Custom tool to send draft mail using gmail api
            ],
            verbose = True,
            allow_delegation=False,    # does not pass task to other agents
            llm = llm
        )
       
       