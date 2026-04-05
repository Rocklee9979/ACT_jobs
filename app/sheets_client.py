import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
from .config import settings

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_client():
    info = json.loads(settings.GOOGLE_SERVICE_ACCOUNT_JSON)
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet():
    client = get_client()
    sh = client.open_by_key(settings.GOOGLE_SHEETS_KEY)
    return sh.worksheet("jobs")

def get_existing_job_ids(sheet):
    records = sheet.get_all_records()
    return {r["job_id"] for r in records}

def upsert_jobs(jobs):
    sheet = get_sheet()
    existing_ids = get_existing_job_ids(sheet)
    new_rows = []
    now = datetime.utcnow().isoformat()

    for job in jobs:
        if job["job_id"] in existing_ids:
            continue
        new_rows.append([
            job["job_id"],
            job["title"],
            job["classification"],
            job["directorate"],
            job["closing_date"],
            job["link"],
            now,
            "new",
        ])

    if new_rows:
        sheet.append_rows(new_rows, value_input_option="RAW")
    return new_rows