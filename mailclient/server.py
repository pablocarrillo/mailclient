# -*- coding: utf-8 -*-

"""
Mail client module
"""

import smtplib
from message import Message
from mail_exceptions import ConnectionRefused, DataError


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
        try:
            self.smtp = smtplib.SMTP(self.host)
        except Exception as ex:
            raise ConnectionRefused("Connection failed, "
                                    "please check data. {0}".format(ex))

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
        if not isinstance(message, Message):
            raise DataError("You have to send a mail.Message object.")
        message._check_message_properties()
        mime = message._build_mime()
        self.smtp.sendmail(message.sender, message._recipients_list,
                           mime.as_string())



