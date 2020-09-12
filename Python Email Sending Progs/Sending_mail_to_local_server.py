'''
SETTING UP MAIL SERVER ON YOUR LOCAL MACHINNE :-
python -m  smtpd -c DebuggingServer -n localhost:1025
'''

import smtplib
import os

Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

# Setting up SMTP connection using Gmil server:-

with smtplib.SMTP('localhost',1025) as smtp:
    
    '''DONT NEED THERSE LINES OF CODE NOW 

    smtp.ehlo() # Identifying ourselves
    smtp.starttls() # encrypting our traffic
    smtp.ehlo() # reidentifying ourselves

    smtp.login(Email_address,Email_password) # logging in to mail server
    '''
    
    # Subject and Body of our email
    subject = 'Had an event this weekend!'
    body =  'organizing my painting exhibition this week at Bharat bhavan, will soon tell you mare about that'

    # A simple message with Subject and Body
    msg = f'Subject : {subject}\n\n {body}'

    #Sending the mail in the format: (Sender's email, reciver's email, message)
    smtp.sendmail(Email_address,'nishika.verma@live.com', msg)
    