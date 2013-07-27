# -*- coding: utf-8 -*-

"""
Mail client module
"""

import smtplib
from email.mime.text import MIMEText


class Server(object):

    """
    Server class.
    Inits the connection, build the mime object and send
    """
    def __init__(self, server, port=25, username=None, password=None,
                 use_tls=False):
        """
        Connection
        """
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.host = '{0}:{1}'.format(server, port)
        self.use_tls = use_tls
        self.smtp = smtplib.SMTP(self.host)
        self.smtp.ehlo()
        if self.use_tls:
            self.smtp.starttls()
        if username and password:
            try:
                self.smtp.login(self.username, self.password)
            except Exception as ex:
                print ex
                print "Login not needed"

    def __repr__(self):
        """
        Pretty printing!
        """

        return "{0}({1}:{2}@{3}:{4})".format(self.__class__, self.username,
                                             self.password, self.server,
                                             self.port)

    def send(self, message):
        """
        Build the mime object, and send the message.
        """
        message.check_message_properties()
        mime = message.build_mime()
        self.smtp.sendmail(message.sender, message.recipients_list,
                           mime.as_string())


class Message(object):
    """
    Message class
    """

    def __init__(self, subject=None, text=None, sender=None, recipients=None):
        self.subject = subject
        self.text = text
        self.sender = sender
        self.recipients_list = ""
        self.recipients = recipients

    def build_mime(self):
        """
        Build MIMEText()
        """
        self.mime = MIMEText(self.text)
        self.mime['Subject'] = self.subject
        self.mime['From'] = self.sender
        self.mime['To'] = self.recipients

        return self.mime

    def check_message_properties(self):
        if not self.subject:
            self.subject = ""
        if not self.text:
            self.text = ""
        if not self.sender:
            self.sender = ""

        if self.recipients:
            self.recipients_list = self.recipients.replace(' ', '').split(',')
        else:
            self.recipients_list = ""



    def __repr__(self):
        """
        Pretty printing!
        """
        return "Message (<{0} to {1} from {2}>)".format(self.subject,
                                                        self.recipients,
                                                        self.sender)
