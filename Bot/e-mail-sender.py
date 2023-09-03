import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email sender and receiver information
sender_email = "sender@gmail.com"
receiver_email = "recipient@gmail.com"
password = "sender_password"

# Email subject and content
subject = "Subject Line"
message = "This email was sent using Python."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending error: {e}")
finally:
    server.quit()