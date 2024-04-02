from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.tools.gmail.utils import (build_resource_service, get_gmail_credentials,)

from langchain.tools import tool
from langchain_community.tools.gmail.create_draft import GmailCreateDraft


# Gets credentions from json file. Change to your file location

credentials = get_gmail_credentials(
    token_file= "token.json",
    scopes=["https://mail.google.com/", ], 
    client_secrets_file= "credentials.json"
)


# Connects with gmail using the api

def api_resource():
   return build_resource_service(credentials=credentials)


# Fetches mail from the inbox

def fetch_mails():
  search = GmailSearch(api_resource=api_resource())
  emails = search("in:inbox")

  mails = []

  for email in emails: 
      mails.append(
          {
              "id": email["id"],
              "threadId": email["threadId"],
              "snippet": email["snippet"],
              "sender": email["sender"],
          }
      )

  return mails


# Draft mail using by manually passing the parameters

class CreateDraftTool(): 

    @tool("Create Draft")
    def create_draft(data):

        """
        Useful to create an email draft.
        The input to this tool should be a pipe (|) separated text of length 3 (three), 
        representing who to send the email to, the subject of the email and the actual message.
        For example, `lorem@ipsum.com|Nice To Meet You |Hey it was great to meet you.`.
        """

        email, subject, message = data.split('|')
        draft = GmailCreateDraft(api_resource=api_resource())

        result = draft({
            'to': [email],
            'subject': subject,
            'message': message
        })