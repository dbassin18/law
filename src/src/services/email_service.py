# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import base64
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(from_email, to_emails, subject, content):
    f = open('my_file.txt', 'rb')
    thing = f.readline()
    other_thing = base64.b64decode(thing, altchars=None, validate=False).decode()
    f.close()
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(other_thing)
        response = sg.send(message)
        logging.info(response.status_code)
        logging.info(response.body)
        logging.info(response.headers)
    except Exception as e:
        logging.error(e)
