# -*- coding: utf-8 -*-
import datetime
import logging


# Metaclass that define the Singleton class
class SingletonType(type):
    _instances = {}

    # __call__ is fist method called on the metaclass for creating an instance of the class.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# python 3 style
class ZdmLogger(object, metaclass=SingletonType):
    """ A singleton containing the logging settings """
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        streamHandler = logging.StreamHandler()

        # fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        # self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    def get_logger(self):
        return self._logger


