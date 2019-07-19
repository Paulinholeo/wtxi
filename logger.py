# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler
import logging

from cfg import LOG_PATH, LOG_LEVEL, LOG_MAX_BYTES, LOG_COUNT

""" WTXI centralized logger"""

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2019, Brascontrol"
__status__ = "Development"


def logger_init(logger_name: str, log_path: str, max_bytes: int=10*(2**20), count: int=5):
    """Init logger system"""
    _logger = logging.getLogger(logger_name)
    _logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s %(message)s')
    # file_handler = TimedRotatingFileHandler(logger_name + '.log', when='D',
    #                                         interval=1, encoding='utf8')
    file_handler = RotatingFileHandler(log_path + logger_name + '.log', maxBytes=max_bytes,
                                       backupCount=count, encoding='utf8', delay=True)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)
    _logger.addHandler(console_handler)

    return _logger


logger = logger_init('wtxi', LOG_PATH, max_bytes=LOG_MAX_BYTES, count=LOG_COUNT)