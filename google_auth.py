client_id="233931312133-tnolfdh6j0afc1ci92kagqaiiq430qa2.apps.googleusercontent.com"
client_secret="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"

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import google.oauth2.credentials
import google_auth_oauthlib.flow


CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
#SCOPES = ['https://www.googleapis.com/auth/youtube']

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)