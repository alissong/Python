import os

#Variaveis
p = os.path.abspath('teste01.txt') #Path absoluto
s = os.path.split(p) #Splita path
p = s[0] #Recebe primeira parte do split

print('Path: ', p) #Exibe path do arquivo