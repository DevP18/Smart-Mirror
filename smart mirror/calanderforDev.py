from __future__ import print_function
from msilib.schema import ServiceInstall
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import dateutil.parser
import datetime
import configparser
import datetime
import pandas as pd
import pytz

config = configparser.RawConfigParser()
config.read('C://Users//ashish//AppData//Local//Programs//Python//Python39//Doc//smart mirror//config.ini')
Client_Secret_file = config['Calander']['Client_File']
Api_Name = config['Calander']['Api_Version']
Api_Version = config['Calander']['Api_Name']
Scopes = config['Calander']['Scopes']
global service
SCOPES = ['https://www.googleapis.com/auth/calendar']




creds = None
if os.path.exists('token1.json'):
    creds = Credentials.from_authorized_user_file('token1.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token1.json', 'w') as token:
            token.write(creds.to_json())
service = build('calendar', 'v3', credentials=creds)


def get_events():
    global service
    maxcount = 10
    count = 0
    events_Begin = []
    events_End = []
    events_Description = []
    page_token = None
    results = service.calendarList().list(pageToken=page_token).execute()
    Cal_Id = results['items'][0]['id']
    get_all_events = service.events().list(calendarId=Cal_Id).execute()
    Now_Time = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    the_Time = Now_Time.replace(microsecond=0)


    try:
        while maxcount > count:
            get_all_events['items'][0]['start']['dateTime']
            parsed1 = dateutil.parser.parse(str(the_Time))
            parsed2 = dateutil.parser.parse(get_all_events['items'][1]['end']['dateTime'])


            format = '%Y-%m-%dT%H:%M:%S%z'
            dt_object = datetime.datetime.strptime(get_all_events['items'][count]['start']['dateTime'], format)
            events_Begin.append(datetime.datetime.strftime(dt_object, '%I:%M:%p %B-%d-%Y'))
            dt_object = datetime.datetime.strptime(get_all_events['items'][count]['end']['dateTime'], format)
            events_End.append(datetime.datetime.strftime(dt_object, '%I:%M:%p %B-%d-%Y'))
            try:
                events_Description.append(get_all_events['items'][count]['summary'])
            except KeyError:
                events_Description.append("None")

            count = count + 1
    except IndexError:
        return events_Begin, events_End, events_Description
    return events_Begin, events_End, events_Description

get_events()