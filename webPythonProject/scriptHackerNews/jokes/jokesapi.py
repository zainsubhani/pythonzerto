import requests
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import schedule
import time

# 1. Fetch Joke
def get_joke():
    headers = {'Accept': 'application/json'}
    res = requests.get('https://icanhazdadjoke.com/', headers=headers)
    return res.json()['joke'] if res.status_code == 200 else 'No joke today!'

# 2. Send Email
def send_email(joke):
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient@example.com"
    password = "your_app_password"  # Use App Password if Gmail

    msg = MIMEText(joke)
    msg['Subject'] = 'Your Daily Dad Joke 🤪'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# 3. Send SMS
def send_sms(joke):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=joke,
        from_='+1234567890',  # Your Twilio number
        to='+19876543210'     # Recipient number
    )

    print("SMS sent:", message.sid)

# 4. Combine All
def send_joke_to_all():
    joke = get_joke()
    send_email(joke)
    send_sms(joke)

# 5. Schedule Daily at 9 AM
schedule.every().day.at("09:00").do(send_joke_to_all)

print("Scheduler started... (Ctrl+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(60)
