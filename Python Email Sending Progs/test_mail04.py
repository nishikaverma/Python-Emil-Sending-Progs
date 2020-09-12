# Attachng other files(pdf, word etc) as attachments with email

import smtplib
import os
import imghdr
from email.message import EmailMessage


Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

msg = EmailMessage()
msg['Subject'] ='Test pdf'
msg ['From'] =Email_address
msg['To'] = 'nishika.verma@live.com'
msg.set_content('I am sending the test  pdf, Check it out')

files = ['test_pdf.pdf']
for file in files:
    with open(file, 'rb') as f :
        file_data = f.read() # reading the image
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename= file_name)  #finally adding the image in the form of attachment
   

# Setting up SMTP connection for Gmil server:-
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Email_address,Email_password) # logging in to mail server

    #Sending the message 
    smtp.send_message(msg)
    