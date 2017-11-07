import os
import time

#Declaracao de variaveis
p = os.getcwd()
f = list(os.listdir(p))
d = dict()

#Calcula tamanho dos arquivos
for i in f:
    stats = os.stat(i)
    d[i] = stats

#Lista arquivo e tamanho
for t in d:
    print("Arquivo: {:30s} Tamanho: {:d} Bytes".format (t, d[t].st_size), #Lista arquivo e tamanho em bytes
          "\t Ultima modificação: %s" % time.ctime(os.path.getmtime(t)), #Ultima modificação
          "\t Criado: %s" % time.ctime(os.path.getctime(t)) #Data de criação
          )

