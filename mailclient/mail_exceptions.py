# -*- coding: utf-8 -*-


class ConnectionRefused(Exception):
    """
    The connection was refused.
    """


class DataError(Exception):
    """
    Error in data.
    """


class InvalidPath(Exception):
    """
    Attachment path is invalid.
    """

