import os
import time
import threading
import datetime
import psutil

<<<<<<< HEAD
from VerifyBri import *
=======
from check_bricap import *
>>>>>>> desenvolvimento

import cfg 
from logger import logger

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2019, Brascontrol"
__status__ = "Development"

<<<<<<< HEAD
TEMPO_MAX = 10 #Tempo em segundos
=======
>>>>>>> desenvolvimento

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
<<<<<<< HEAD
        ctempo= str(datetime.timedelta(seconds=TEMPO_MAX))    
        tempo = datetime.datetime.now()
        logger.info('\033[36m'+str(tempo)+' >>>> Vericando a cada ' + ctempo +'\033[0;0m\n')
        teste = verificaTempo()
        if not teste:
            logger.info('\n\033[36m'+str(tempo)+' >>>> REINICIANDO TXI (pid=%d)'+'\033[0;0m\n', os.getpid() )
=======
        ctempo= str(datetime.timedelta(seconds=cfg.TEMPO_MAX_TXI))    
        logger.info('  >>>>  Vericando a cada ' + ctempo )
        teste = verificaTempo()
        if not teste:
            logger.info('  >>>>  REINICIANDO TXI (pid=%d)\n', os.getpid() )
>>>>>>> desenvolvimento
            os.system('killall txi')
        
if __name__ == "__main__":
    main()
    
    


