import os
import time
import threading
import datetime
import psutil

from check_bricap import *

import cfg 
from logger import logger

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2019, Brascontrol"
__status__ = "Development"


#Cria thread
class MainClass(threading.Thread):
    def __init__(self):
        self.die = False
        threading.Thread.__init__(self)

    def verificaSeRodaProcesso(self,nomeProcesso):
        for proc in psutil.process_iter():
            try:
                if nomeProcesso.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def verificaRun(self):
        file = os.path.exists("/var/run/txi/txi.pid")
        if  not file:
            os.system('/home/bri7000/bricap/txi &')

    def run(self):
        while not self.die:
            self.verificaRun()
            time.sleep(11)


    def join(self):
        logger.debug("\nOcorreu falha ao executar Thread")
        super().join()

def leArquivo():
    f = open('/var/run/txi/tx.txi','r')
    arquivo = int(f.read())
    f.close()
    return arquivo

def verificaTempo():
    arquivoAntigo = leArquivo()
    time.sleep(cfg.TEMPO_MAX_TXI)
    arquivoNovo = leArquivo()
    if arquivoAntigo == arquivoNovo:
        return False
    else:
        return True

def main():
    verificaTxi= MainClass()
    verificaBri = SecondClass()
    verificaBri.start()
    verificaTxi.start()
    while True:
        ctempo= str(datetime.timedelta(seconds=cfg.TEMPO_MAX_TXI))    
        logger.info('  >>>>  Vericando a cada ' + ctempo )
        teste = verificaTempo()
        if not teste:
            logger.info('  >>>>  REINICIANDO TXI (pid=%d)\n', os.getpid() )
            os.system('killall txi')
        
if __name__ == "__main__":
    main()
    
    


