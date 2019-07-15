# -*- coding: utf-8 -*-

""" WTXI configuration file"""

import logging

__author__ = "Paulo/Giovane"
__copyright__ = "Copyright 2018, Brascontrol"
__status__ = "Development"

LOG_PATH = '/var/log/wtxi/'
LOG_LEVEL = logging.INFO
LOG_MAX_BYTES = 40 * (2 ** 20)
LOG_COUNT = 25


