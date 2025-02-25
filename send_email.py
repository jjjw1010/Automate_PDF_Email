import time
from datetime import datetime
from dotenv import load_dotenv
import os

###############################################################
# Load env variables 
load_dotenv()
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PW = os.getenv("EMAIL_PW")
RECEIVER_ID = os.getenv("RECEIVER_ID")
SEARCH_DIRECTORY = os.getenv("SEARCH_DIRECTORY")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
###############################################################

 # Extract the full month name
full_month_name = datetime.now().strftime("%B")
filename_pattern = f"{full_month_name}_Armstrong_Statement.pdf"

# Initialize a variable to store the full file path
file_path = None

# Walk through the directory
for root, dirs, files in os.walk(SEARCH_DIRECTORY):
    for file in files:
        if file.endswith(filename_pattern):
            file_path = os.path.join(root, file)
            break
    if file_path:
        break

if not file_path:
    print("File not found.")
else:
    print(f"File found: {file_path}")

###############################################################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

# Email Content
subject = f"{full_month_name} Monthly Armstrong Statement"
body = "Please find attached your monthly Armstrong statement."

# Create the email message
msg = MIMEMultipart()
msg['From'] = EMAIL_ID
msg['To'] = RECEIVER_ID
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the PDF file
if file_path:
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(file_path)}',
        )
        msg.attach(part)

# Send the email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(EMAIL_ID, EMAIL_PW)
        server.sendmail(EMAIL_ID, RECEIVER_ID, msg.as_string())
    print('Email sent successfully.')
except Exception as e:
    print(f'Failed to send email: {e}')