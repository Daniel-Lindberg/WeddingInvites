# -*- coding: utf-8 -*-
"""
Author: Daniel Lindberg
Description: Going to send emails to all of my wedding invites that I input into a csv
Format for the CSV is:
John Doe & Mary Jane, jon.doe@gmail.com, mary.jane@gmail.com
Chris OtherPerson, chris.otherperson@gmail.com
"""

import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


image_name = "SaveTheDate.jpeg"
wedding_contacts = "Wedding_Contacts.csv"

image_data = None
with open(image_name, 'rb') as f:
    img_data = f.read()


def send_email(subject, body, sender, recipients, password):
    
    # Content for the Body, subject , and recepients
    msg = MIMEMultipart()
    text = MIMEText(body)
    msg.attach(text)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    # Attach image to the email
    image = MIMEImage(img_data, name=os.path.basename(image_name))
    msg.attach(image)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent to {0}!".format(recipients))



subject = "Save the Date: X + Y Wedding"
sender = "some.person@gmail.com" # Going to fill this with garbage, but you know what to do
password = "1234" # Read README to see how to generate

with open(wedding_contacts) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if row[2] == "":
            recipients = [row[1]]
        else:
            recipients = [row[1], row[2]]
        body = "Dear {0},\n Attached is our save the dates! ".format(row[0])
        send_email(subject, body, sender, recipients, password)