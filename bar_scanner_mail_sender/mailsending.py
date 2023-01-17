import smtplib
from email.message import EmailMessage
def send_mail(mailid):
    msg = EmailMessage()
    msg.set_content('Thankyou for visiting SAIRAM Library ,Hope you have some good time.')

    msg['Subject'] = 'Greetings...!'
    msg['From'] = "#mailID#"
    msg['To'] = mailid

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("#mailid#", "#passwor#")
    server.send_message(msg)
    server.quit()
