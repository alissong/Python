import os

#Variaveis
p = 'path01'
d = 'path01'
a = 'path01'

#Verifica se PATH existe
if os.path.exists(p):
    print(p, 'existe!')
else:
    print(p, 'Não existe!')

#Verifica se PATH é um diretório
if os.path.isdir(d):
    print(d, 'É um diretório!')
else:
    print(d, 'Não é um diretório!')

#Verifica se PATH é um arquivo
if os.path.isfile(a):
   print(d, 'É um arquivo!')
else:
    print(d, 'Não é um arquivo!')