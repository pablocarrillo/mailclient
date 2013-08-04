# -*- coding: utf-8 -*-

"""
Mail client module
"""

import smtplib
import os
import magic
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from mail_exceptions import ConnectionRefused, DataError, InvalidPath


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


class Message(object):
    """
    Message class
    """

    def __init__(self, subject=None, text=None, sender=None, recipients=None):
        self.subject = subject
        self.text = text
        self.sender = sender
        self._recipients_list = ""
        self.recipients = recipients
        self._attachment = False

    def _build_mime(self):
        """
        Build MIMEText()
        """
        self.mime = MIMEMultipart()
        self.mime.attach(MIMEText(self.text))
        self.mime['Subject'] = self.subject
        self.mime['From'] = self.sender
        self.mime['To'] = self.recipients

        if self._attachment:
            self.mime.attach(self._attachment)

        return self.mime

    def _check_message_properties(self):
        if not self.subject:
            self.subject = ""
        if not self.text:
            self.text = ""
        if not self.sender:
            self.sender = ""

        if self.recipients:
            self._recipients_list = self.recipients.replace(' ', '').split(',')
        else:
            self._recipients_list = ""

    def attach(self, attachment):
        if isinstance(attachment, str):
            if os.path.exists(attachment):
                fp = open(attachment)
            else:
                raise InvalidPath("File path is not valid.")
        elif isinstance(attachment, file):
            fp = attachment
        else:
            raise DataError("Argument must be a string (file path) or a file"
                            " object.")
        magic_mime = magic.Magic(mime=True)
        mime = None
        if 'application' in magic_mime.from_file(fp.name):
            mime = MIMEApplication(fp.read())
        elif 'audio' in magic_mime.from_file(fp.name):
            mime = MIMEAudio(fp.read())
        elif 'image' in magic_mime.from_file(fp.name):
            mime = MIMEImage(fp.read())
        #elif 'text' in magic_mime.from_file(fp.name):
        #    mime = MIMEText(fp.read())
        if mime:
            mime.add_header('Content-Disposition', 'attachment',
                            filename=os.path.split(fp.name)[-1])
        self._attachment = mime
        fp.close()

    def __repr__(self):
        """
        Pretty printing!
        """
        return "Message (<{0} to {1} from {2}>)".format(self.subject,
                                                        self.recipients,
                                                        self.sender)
