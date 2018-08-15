import smtplib
import os
import struct
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from itsdangerous import URLSafeTimedSerializer
from string import Template
from application.modules.core.exc.failed import ConfirmationTimeError
from application.modules.core.exc.invalid import InvalidValueError


class ConfirmationNotification():

    def __init__(self, to_add=None, username=None, subject=None, from_add=None):
        self.sender_address = from_add
        self.reciever_address = to_add
        self.subject = subject
        self.username = username
        self.msg = MIMEMultipart('alternative')
        self.GATOR_EMAIL = os.environ['GATOR_EMAIL']
        self.GATOR_PASSWORD = os.environ['GATOR_PASSWORD']
        self.GATOR = os.environ['GATOR']
        self.SMS_GATOR_URL = os.environ['SMS_GATOR_URL']

    def send_otp(self, phone, otp):
        url = SMS_GATOR_URL
        params = {"email":GATOR_EMAIL, "password":GATOR_PASSWORD,"type":"0", 
                "dlr":"0", "destination":phone, "sender":GATOR, "message":otp}
        try:
            requests.post(url, params=params)
        except ConnectionError:
            message = 'We been unable to send you your otp. Please retry'
            raise InteralServerError(message)

    def code_generator(self):
        return str(struct.unpack("I", os.urandom(4))[0])[:5]    

    @staticmethod
    def generate_confirmation_token(email, username):
        serializer = URLSafeTimedSerializer(os.environ['CONFIRMATION_SECRET_KEY'])
        data = dict(email=email, username=username)
        return serializer.dumps(data, salt=os.environ['CONFIRMATION_SALT_KEY'])

    @staticmethod
    def deserialize_token(token, expiration=(3600*6)):
        serializer = URLSafeTimedSerializer(os.environ['CONFIRMATION_SECRET_KEY'])
        try:
            data = serializer.loads(
                token, salt=os.environ['CONFIRMATION_SALT_KEY'],
                max_age=expiration)
        except itsdangerous.SignatureExpired:
            message = 'Confirmation token has expired.'
            raise ConfirmationTimeError(message)
        except itsdangerous.BadSignature as e:
            message = str(e)
            raise InvalidValueError(e)
        return data

    def build_message(self, email_body=None, token=None):
        html_template = email_body
        if not html_template:
            with open("application/modules/core/utils/email_notification.html", "r") as f:
                html_template = f.read()
        if not token:
            token = EmailConfirmationNotification.generate_confirmation_token(self.reciever_address, self.username)
        s = Template(str(html_template))
        url = 'api.entree.com.ng/v1/tutor/confirmatio?token='+token
        d =  dict(account_name=self.username, token=url)
        new_template = s.safe_substitute(d)
        return new_template

    def send_email(self):
        self.msg['From'] = 'no-reply@entree.com.ng'
        self.msg['To'] = self.reciever_address
        self.msg['Subject'] = self.subject

        message_body = self.build_message()
        self.msg.attach(MIMEText(message_body, 'html'))
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        text = self.msg.as_string()
        server.login('no-reply@entree.com.ng', 'Admin@1234')
        server.sendmail(self.sender_address, self.reciever_address, text)
        server.quit()