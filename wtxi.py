import os
import time
import threading
import datetime

import cfg 
from logger import logger

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2019, Brascontrol"
__status__ = "Development"

TEMPO_MAX = 3650 #Tempo em segundos

class MainClass(threading.Thread):
    def __init__(self)
        self.die = False
        threading.Thread.__init__(self)

    def verificaSeRodaProcesso(self,nomeProcesso):
        for proc in psutil.process_iter():
            try:
                if nomeProcesso.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess,psutil.AcessDenied,psutil.ZombieProcess):
                pass
        return False

    def verifica(self):  
        file = os.path.exists("/var/run/txi/txi.pid")
        if  not file:. 
            os.system('/home/bri7000/bricap/txi &')

    def run(self):
        while not self.die:
            self.verifica()
            logger.debug('bricapd está rodando agora')
            if self.verificaSeRodaProcesso('bricapd'):
                logger.debug('bricapd está rodando agora')
            else:
                logger.debug('bricapd não está rodando')
                os.system('/home/bri7000/bricap/bricapd &')

    def join(self):
        self.die = True
        super().join()
        logger.info('Houve uma FALHA ao executar Thread')

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
    verificaTxi = MainClass()
    verificaTxi.start()
    while True:
        ctempo= str(datetime.timedelta(seconds=TEMPO_MAX))    
        tempo = datetime.datetime.now()
        logger.info(str(tempo)+' >>>> Verificando a cada ' + ctempo +' (hh:mm:ss) \n')
        teste = verificaTempo()
        if not teste:
            logger.info(str(tempo)+' >>>> REINICIANDO TXI (pid=%d) \n', os.getpid() )
            os.system('killall txi')
        
if __name__ == "__main__":  
    main()
    
    


