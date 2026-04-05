from fastapi import FastAPI
from .rss_client import fetch_jobs
from .sheets_client import upsert_jobs
from .filters import filter_suitable
from .notifier import notify_new_suitable_jobs

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
def run_job():
    jobs = fetch_jobs()
    new_rows = upsert_jobs(jobs)

    # Map back to job dicts for suitability filter
    new_jobs = [j for j in jobs if any(j["job_id"] == r[0] for r in new_rows)]
    suitable = filter_suitable(new_jobs)
    notify_new_suitable_jobs(suitable)

    return {
        "fetched": len(jobs),
        "new": len(new_rows),
        "suitable_new": len(suitable),
    }