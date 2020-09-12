# Sending email with HTML 

import smtplib
import os
import imghdr
from email.message import EmailMessage

Email_address = 'vermanishika122@gmail.com' # Sender's mail
Email_password = 'gqfhtjhppakdwjjn'  # Generated App password

#contacts = ['nishika.verma@live.com', 'akhilverma1643@gmail.com', 'samarthverma1882gmail.com']

msg = EmailMessage()
msg['Subject'] ='Html MAIL'
msg ['From'] =Email_address
msg['To'] = 'nishika.verma@live.com'
msg.set_content('This is a plain text email')

msg.add_alternative('''\
<!DOCTYPE html>
<html lang="en">
<body>
    <h1 style="color:aqua"> This is the Html emil I am sending to you through python </h1>    
</body>
</html>

''', subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Email_address,Email_password) # logging in to mail server

    #Sending the message 
    smtp.send_message(msg)
    