from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
from .config import settings

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheets_client():
    creds = Credentials.from_authorized_user_info(
        json.loads(settings.GOOGLE_OAUTH_TOKEN),
        SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    return service.spreadsheets()