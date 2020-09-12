# Sendnig mail through SSL connection

import smtplib
import os

Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

# Setting up SMTP connection using Gmil server:-
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Email_address,Email_password) # logging in to mail server

    subject = 'Had an event this weekend!'
    body =  'organizing my painting exhibition this week at Bharat bhavan, will soon tell you mare about that'

    msg = f'Subject : {subject}\n\n {body}'

    #Sending the mail in the format: (Sender's email, reciver's email, message)
    smtp.sendmail(Email_address,'nishika.verma@live.com', msg)
    