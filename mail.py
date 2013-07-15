# -*- coding: utf-8 -*-

"""
Mail client module
"""

import smtplib
from email.mime.text import MIMEText


class Server(object):
    def __init__(self, server, port=25, username=None, password=None,
                 use_tls=False):
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
            except Exception, ex:
                print ex
                print "Login not needed"


    def __repr__(self):
        return "{0}({1}:{2}@{3}:{4})".format(self.__class__, self.username,
                                             self.password, self.server,
                                             self.port)

    def send(self, message):
        print "Sending to {0}".format(message.recipients_list)
        print "From {0}".format(message.sender)
        print "Msg {0}".format(message.message)
        print "msg 2 {0}".format(message.message.as_string())
        self.smtp.sendmail(message.sender, message.recipients_list,
                           message.message.as_string())


class Message(object):
    def __init__(self, subject=None, text=None, sender=None, recipients=None):
        self.subject = subject
        self.text = text
        self.sender = sender
        self.recipients_list = recipients.replace(' ' , '').split(',')
        self.recipients = recipients

        self.message = MIMEText(self.text)
        self.message['Subject'] = self.subject
        self.message['From'] = self.sender
        self.message['To'] = self.recipients

    def __repr__(self):
        return "Message (<{0} to {1} from {2}>)".format(self.subject,
                                                      self.recipients,
                                                      self.sender)








