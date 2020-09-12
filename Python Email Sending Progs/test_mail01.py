

import smtplib
import os
from email.message import EmailMessage

Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

msg = EmailMessage()
msg['Subject'] ='Had an event this weekend!'
msg ['From'] =Email_address
msg['To'] = 'nishika.verma@live.com'
msg.set_content('organizing my painting exhibition this week at Bharat bhavan, will soon tell you mare about that')

# Setting up SMTP connection for Gmil server:-
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Email_address,Email_password) # logging in to mail server

    #Sending the message 
    smtp.send_message(msg)