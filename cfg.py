# -*- coding: utf-8 -*-

""" WTXI configuration file"""

import logging

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2018, Brascontrol"
__status__ = "Development"

LOG_PATH = '/var/log/wtxi/'
LOG_LEVEL = logging.INFO
LOG_MAX_BYTES = 40 * (2 ** 20)
LOG_COUNT = 25

#TEMPOS DE MONITORAMENTO DOS SERVIÇOS

TEMPO_MAX_TXI=10 #Em segundos
TEMPO_MAX_BRICAP=30 #Em segundos
