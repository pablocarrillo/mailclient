# -*- coding: utf-8 -*-

"""
Tests for mail client
"""

import mail
import unittest
from mail_exceptions import ConnectionRefused, DataError


class MailClientTestCase(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_connection_refused(self):
        with self.assertRaises(ConnectionRefused):
            mail.Server('localhost_fake')

    def test_connection_ok(self):
        s = mail.Server('smtp.gmail.com', 587)
        self.assertIsInstance(s, mail.Server)

    def test_send_string(self):
        s = mail.Server('localhost')
        with self.assertRaises(DataError):
            s.send("This is a string")

    def test_send_ok(self):
        s = mail.Server('localhost')
        msg = mail.Message('This is my subject', 'And this is the body',
                           'iamthe@sender.com', 'iamthe@recipient1.com, '
                                                'iamthe@recipient2.com')
        s.send(msg)


def main():
    unittest.main()

if __name__ == '__main__':
    main()