import os
import time
import threading
import datetime

import cfg 
from logger import logger

__author__ = "Paulo/Giovane"
__copyright__ = "Copyright 2018, Brascontrol"
__status__ = "Development"

TEMPO_MAX = 3650 #Tempo em segundos

class MainClass(threading.Thread):
    def __init__(self,name):
        self.die = False
        threading.Thread.__init__(self)
        self.name = name

    def verificaRun(self):  
        file = os.path.exists("/var/run/txi/txi.pid")
        if  not file:. 
            os.system('/home/bri7000/bricap/txi &')

    def run(self):
        while not self.die:
            self.verificaRun()
            time.sleep(10)
            logger.info(' >>>> Thead Executada')

    def join(self):
        self.die = True
        super().join()
        logger.info(' >>>> Falha ao executar Thread' )

def leArquivo():
    f = open('/var/run/txi/tx.txi','r')
    arquivo = int(f.read())
    f.close()
    return arquivo

def verificaTempo():
    arquivoAntigo = leArquivo()
    time.sleep(TEMPO_MAX)
    arquivoNovo = leArquivo()
    if arquivoAntigo == arquivoNovo:
        return False
    else:
        return True

def main():
    m = MainClass('MainThread')
    m.start()
    while True:
        ctempo= str(datetime.timedelta(seconds=TEMPO_MAX))    
        tempo = datetime.datetime.now()
        logger.info(str(tempo)+' >>>> Verificando a cada ' + ctempo +' (hh:mm:ss)')
        teste = verificaTempo()
        if not teste:
            logger.info(str(tempo)+' >>>> REINICIANDO TXI (pid=%d) ', os.getpid() )
            os.system('killall txi')
        
if __name__ == "__main__":  
    main()
    
    


