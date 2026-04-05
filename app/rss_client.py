import feedparser
import re
from datetime import datetime
from .config import settings

CLASS_REGEX = re.compile(r"(ASO\d|SOG[A-C]|HP\d|VN\d|PO\d)", re.IGNORECASE)

def parse_classification(title: str) -> str | None:
    m = CLASS_REGEX.search(title)
    return m.group(1).upper() if m else None

def fetch_jobs():
    feed = feedparser.parse(settings.ACT_RSS_URL)
    jobs = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        pub_date = getattr(entry, "published", None)
        job_id = getattr(entry, "id", link)

        classification = parse_classification(title)

        jobs.append({
            "job_id": job_id,
            "title": title,
            "classification": classification,
            "directorate": None,  # can parse from description later
            "closing_date": None, # can parse from description later
            "link": link,
            "pub_date": pub_date,
        })
    return jobs