"""
Script: new_email.py
Description: Tool for new email
Category: Data_Processing_and_Web
"""
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm  # Import tqdm

# Read the Excel file
data = pd.read_excel('ImportAccounts-updated.xlsx')

# Extract email addresses from column A, contents from column B, and additional contents from column C
emails = data['Personal Email']
contents_b = data['InternalMail']
contents_c = data['Password']
content_a = data['Username']

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'henryquayezee@gmail.com'
SENDER_PASSWORD = 'qxlnolriiargfscd'

# Define the progress bar
progress_bar = tqdm(total=len(emails), desc='Sending Emails')

# Iterate over each row and send emails
for email, content_b, content_c, content_a in zip(emails, contents_b, contents_c, content_a):
    # Create the email
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = email
    message['Subject'] = 'New Email Credentials'

    # Combine contents from columns B and C
    combined_content = f"New Email Address: {content_b}\nUsername: {content_a}\nPassword: {content_c}\nKindly login with these credentials to ayadata.contactoffice.com.\nNB: DO REMEMBER TO CHANGE YOUR PASSWORD\nAlso Login to our slack channel using this link; https://join.slack.com/t/ayadataworkforce/shared_invite/zt-2082ynlph-CfK1_Hf7hXktrTldJi6CCw"

    # Add the content to the email
    message.attach(MIMEText(combined_content, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()

    # Login to the SMTP server
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    # Send the email
    server.sendmail(SENDER_EMAIL, email, message.as_string())

    # Disconnect from the server
    server.quit()

    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

print("Emails sent successfully!")
