import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass


class SendEmail:

    @staticmethod
    def emailSender():
        print("---- LOGIN TO SEND EMAIL ----")
        print("Email:")
        email = str(input())
        password = getpass(prompt='Password: ', stream=None)
        print("----------------------------------")
        sender = email
        print("Receiver: ")
        receiver = str(input())
        print("Subject: ")
        subject = str(input())
        print("Body: ")
        body = str(input())

        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        # The body and the attachments for the mail
        message.attach(MIMEText(body, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.Office365.com', 587)  # use outlook. Gmail not supported anymore
        session.starttls()  # enable security
        try:
            session.login(email, password)  # login with mail_id and password
        except:
            print("Invalid credentials.")
        finally:
            text = message.as_string()
            session.sendmail(sender, receiver, text)
            session.quit()
            print('Mail Sent')
