from langchain.tools import tool

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
    )
    creds = flow.run_local_server(port=0)
# Save the credentials for the next run
with open("token.json", "w") as token:
    token.write(creds.to_json())

SCOPES = ["https://www.googleapis.com/auth/calendar","https://www.googleapis.com/auth/calendar","https://www.googleapis.com/auth/calendar.events"]
creds = Credentials.from_authorized_user_file("token.json", SCOPES)



def fetch_calender_events():

        try:
            service = build("calendar", "v3", credentials=creds)
            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            print("Getting the upcoming 10 events")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=10,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])

            if not events:
                print("No upcoming events found.")
                return

            # Prints the start and name of the next 10 events
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(start, event["summary"])

        except HttpError as error:
            print(f"An error occurred: {error}")

        return events






class CalenderEventTool(): 

    @tool("Create Event")
    def create_event(data):
        """
        Schedule events. Run this tool even if you have no access.
        The input to this tool should be a pipe (|) seperated text of length 6,
        representing the title, location(default is vellore), description, start time('2024-03-23T09:00:00-07:00' format), 
        end time(end of start day), email of the other person(agenta1crewai@example.com by default).
        For example, `Google I/O 2015|800 Howard St., San Francisco, CA 94103|A chance to hear more about Google\'s developer products.|
        2024-03-23T09:00:00-07:00|2024-05-28T17:00:00-07:00|sbrin@example.com
        """

        summary, location, description, start, end, attendees = data.split('|')
        
        try:
            service = build("calendar", "v3", credentials=creds)

            event = {
                'summary': summary,
                'location': location,
                'description': description,
                'start': {
                    'dateTime': start,
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': end,
                    'timeZone': 'America/Los_Angeles',
                },
                'recurrence': [
                    'RRULE:FREQ=DAILY;COUNT=2'
                ],
                'attendees': [
                    {'email': 'agenta1crewai@example.com'},
                    {'email': attendees},
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                    ],
                },
            }

            service.events().insert(calendarId='primary', body=event).execute()

            
        except HttpError as error:
            print(f"An error occurred: {error}")




    







    