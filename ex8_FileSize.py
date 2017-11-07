import os

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
    print("Arquivo: {:30s} Tamanho: {:d} Bytes".format(t, d[t].st_size))