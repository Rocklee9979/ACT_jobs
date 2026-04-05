from .config import settings

def _split(s: str) -> list[str]:
    return [x.strip().lower() for x in s.split(",") if x.strip()]

TARGET_CLASSES = set(_split(settings.TARGET_CLASSIFICATIONS))
INCLUDE_KEYWORDS = _split(settings.INCLUDE_KEYWORDS)
EXCLUDE_KEYWORDS = _split(settings.EXCLUDE_KEYWORDS)

def is_suitable(job: dict) -> bool:
    title = job["title"].lower()
    classification = (job["classification"] or "").upper()

    if TARGET_CLASSES and classification and classification not in TARGET_CLASSES:
        return False

    if any(word in title for word in EXCLUDE_KEYWORDS):
        return False

    if INCLUDE_KEYWORDS and not any(word in title for word in INCLUDE_KEYWORDS):
        return False

    return True

def filter_suitable(jobs: list[dict]) -> list[dict]:
    return [j for j in jobs if is_suitable(j)]