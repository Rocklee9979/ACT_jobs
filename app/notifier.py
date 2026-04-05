import smtplib
from email.message import EmailMessage
from .config import settings

def send_email(subject: str, body: str):
    if not settings.ALERT_EMAIL_TO:
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.ALERT_EMAIL_FROM
    msg["To"] = settings.ALERT_EMAIL_TO
    msg.set_content(body)

    with smtplib.SMTP_SSL(settings.ALERT_EMAIL_SMTP, 465) as smtp:
        smtp.login(settings.ALERT_EMAIL_USER, settings.ALERT_EMAIL_PASS)
        smtp.send_message(msg)

def notify_new_suitable_jobs(jobs):
    if not jobs:
        return
    lines = []
    for j in jobs:
        lines.append(f"{j['title']} ({j['classification']})\n{j['link']}\n")
    body = "\n\n".join(lines)
    send_email(f"{len(jobs)} new suitable ACT jobs", body)