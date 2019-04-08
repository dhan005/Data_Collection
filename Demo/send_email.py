from email.mime.text import MIMETEXT 
import smtplib 

def send_email(email, height, average_height): 
    from_email="lucidproductdirect@gmail.com"
    from_password="New Application"
    to_email = email 

    subject="Artistree Revolution Tech"
    message ="Hello there, thank you for joining new revolutionary music marketplace"

    msg=MIMETEXT(message, 'html')
    msg['subject']=subject
    msg['To']=to_email 
    msg['From']=from_email 

    gmail=smbplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo() 
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
