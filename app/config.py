import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    ACT_RSS_URL: str
    GOOGLE_SHEETS_KEY: str  # spreadsheet ID
    GOOGLE_SERVICE_ACCOUNT_JSON: str  # JSON string
    ALERT_EMAIL_TO: str | None = None
    ALERT_EMAIL_FROM: str | None = None
    ALERT_EMAIL_SMTP: str | None = None
    ALERT_EMAIL_USER: str | None = None
    ALERT_EMAIL_PASS: str | None = None

    # Your preferences
    TARGET_CLASSIFICATIONS: str = "ASO5,ASO6,SOGC"
    INCLUDE_KEYWORDS: str = "policy,analysis,project"
    EXCLUDE_KEYWORDS: str = "nurse,teacher,legal"

settings = Settings()