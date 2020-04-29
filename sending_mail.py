import smtplib

sender_email = ''
sender_password = ''
receiver_mail = ''

message = 'Subject: Hello there\n\nThis message is from a python program'
with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,receiver_mail,message)
