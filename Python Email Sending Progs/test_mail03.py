# Attachng multiple Images as attachments with email

import smtplib
import os
import imghdr
from email.message import EmailMessage


Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

msg = EmailMessage()
msg['Subject'] ='My new Pic!'
msg ['From'] =Email_address
msg['To'] = 'nishika.verma@live.com'
msg.set_content('Checkout my new picture !!!!!!!')

files = ['g1.jpg','g2.jpg','g3.jpg','g4.jpg','g5.jpg']
for file in files:
    with open(file, 'rb') as f :
        file_data = f.read() # reading the image
        file_type = imghdr.what(f.name) #We need to tell which type of image it is (jpg, png , etc.)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename= file_name)  #finally adding the image in the form of attachment
   

# Setting up SMTP connection for Gmil server:-
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Email_address,Email_password) # logging in to mail server

    #Sending the message 
    smtp.send_message(msg)
    