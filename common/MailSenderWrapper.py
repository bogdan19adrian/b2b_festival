from django.core.mail import send_mail

from b2b_festival import settings


class MailSenderWrapper:

    def __init__(self, subject, message,  recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list

    def send_email(self):
        email_from = settings.EMAIL_HOST_USER
        send_mail(self.subject, self.message, email_from, self.recipient_list)
