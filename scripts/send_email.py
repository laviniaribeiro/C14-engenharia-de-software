import os
import smtplib
from email.message import EmailMessage

def send(subject: str, body: str, to: str):
    smtp_host = os.environ.get("SMTP_HOST")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASS")

    if not to:
        print("RECIPIENT_EMAIL não configurado. Pulando envio.")
        return

    if not (smtp_host and smtp_user and smtp_pass):
        print("Credenciais não configuradas. Pulando envio.")
        return

    msg = EmailMessage()
    msg["From"] = smtp_user
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    print(f"Conectando em {smtp_host}:{smtp_port} para enviar e-mail para {to}...")
    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    print("Email enviado com sucesso para", to)

if __name__ == "__main__":
    recipient = os.environ.get("RECIPIENT_EMAIL") or os.environ.get("EMAIL_RECIPIENT")
    subject = os.environ.get("EMAIL_SUBJECT", "Relatório do pipeline")
    body = os.environ.get("EMAIL_BODY", "O pipeline foi executado!")
    send(subject, body, recipient)
