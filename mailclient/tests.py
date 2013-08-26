# -*- coding: utf-8 -*-

"""
Tests for mail client
"""

import server
import message
import unittest
from mail_exceptions import ConnectionRefused, DataError, InvalidPath


class MailClientTestCase(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_connection_refused(self):
        with self.assertRaises(ConnectionRefused):
            server.Server('localhost_fake')

    def test_connection_ok(self):
        s = server.Server('smtp.gmail.com', 587)
        self.assertIsInstance(s, server.Server)

    def test_send_string(self):
        s = server.Server('localhost')
        with self.assertRaises(DataError):
            s.send("This is a string")

    def test_send_ok(self):
        s = server.Server('localhost')
        msg = message.Message('This is my subject', 'And this is the body',
                           'iamthe@sender.com', 'iamthe@recipient1.com, '
                                                'iamthe@recipient2.com')
        s.send(msg)

    def test_file_int(self):
        msg = message.Message()
        with self.assertRaises(DataError):
            msg.attach(1234)

    def test_file_file(self):
        fp = open('mail_exceptions.py')
        msg = message.Message()
        msg.attach(fp)

    def test_file_string(self):
        msg = message.Message()
        msg.attach('mail_exceptions.py')

    def test_file_path_bad(self):
        msg = message.Message()
        with self.assertRaises(InvalidPath):
            msg.attach('/this/does/not/exist/')

    def test_file_path_ok(self):
        msg = message.Message()
        msg.attach('mail_exceptions.py')

    def test_adding_name(self):
        msg = message.Message(sender="'Adrian Espinosa' me@me.com")
        s = server.Server('localhost')
        s.send(msg)


def main():
    unittest.main()

if __name__ == '__main__':
    main()