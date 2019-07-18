import os
import sys
import time
import fnmatch
import datetime
import glob
import threading

__author__ = "Paulo/Giovanne"
__copyright__ = "Copyright 2019, Brascontrol"
__status__ = "Development"

class SecondClass(threading.Thread):
    def __init__(self):
        self.die = False
        threading.Thread.__init__(self)
        self.conta = 0
        self.lock = threading.Lock()

    def contador(self):
        with self.lock:
            self.conta += 1
        
    def recebeContador(self):
        with self.lock:
            return self.conta


    #Retorna o tamanho do arquivo
    def convert_bytes(self,num):
        for x in ['bytes', 'kb', 'MB', 'GB']:
            if num < 1024.0:
                return "%3.1f %s" % (num,x)
            num /= 1024.0

    #Mede tamanho do arquivo
    def file_size(self,file_path):
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            return self.convert_bytes(file_info.st_size)

    #Retorna data no formato AAAAMMDD
    def data(self):
        data = datetime.datetime.now()
        datanow = ('{}{}{}'.format(data.strftime('%Y'),data.strftime('%m'),data.strftime('%d')))
        return datanow

    #Compara o tamanho dos dois arquivos
    def compara(self,a,b):
        tamanhoUm = a
        tamanhoDois = b

        if tamanhoUm != tamanhoDois:
            return True
        else:
            return False

    #Abre bricap.conf e retorna a linha que contem o caminho do brib
    def caminho(self):
        path = open('/etc/bricap/bricap.conf')
        local = path.readlines()[11][8:28]+'b/'
        path.close()
        return local

    #Retorna lista de arquivos dentro da pasta
    def listaArquivos(self):
        path = self.caminho()+self.data()+'/'
        arquivos = os.listdir(path)
        return arquivos

    #Mede tamanho do nome do arquivo, para verificar sua versão
    def verificaVersao(self,arquivo):
        if len(arquivo[0]) == 22:
            return 0
        if len(arquivo[0]) == 24:
            return 1

    def recebeEncode(self):
        path = open('/etc/bricap/bricap.conf')
        encode = int(path.readlines()[5][3:7])
        path.close()
        return 'BRI'+('%05d' % encode)
        

    #Retorna nome do arquivo de acordo com sua versão
    def nomeArquivo(self,versao):
        hora = str(datetime.datetime.now().strftime('%H'))
        minuto = str(datetime.datetime.now().minute)

        if versao == 0:
            filename = self.recebeEncode()+self.data()+hora+'.txt'
            return filename
        elif versao == 1:
            filename = self.recebeEncode()+self.data()+hora+minuto+'.txt'

    def verificaBricap(self):
        path = self.caminho()
        nome = self.nomeArquivo(self.verificaVersao(self.listaArquivos()))
        arquivo = path+self.data()+'/'+nome

        print('\033[37m'+'VERIFICANDO ARQUIVO: '+arquivo+'\033[0;0m')

        a = self.file_size(file_path = arquivo)
        time.sleep(4)
        b = self.file_size(file_path = arquivo)

        if self.compara(a,b):
            print('\033[32m'+'O arquivo está alterando'+'\033[0;0m')
            self.conta = 0

        else:
            print('\033[31m'+'O arquivo não está alterando'+'\033[0;0m')
            self.contador()
            if self.recebeContador() == 5:
                print('REINICIANDO BRICAPD')
                os.system('/home/bri7000/bricap/bricapd -n&')
                self.conta = 0
                time.sleep(30)


    def run(self):
        while not self.die:
            self.verificaBricap()
            time.sleep(20)

    def join(self):
        super().join()
                                
