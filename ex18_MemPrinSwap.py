import psutil

#Variaveis
memototal = psutil.virtual_memory().total #Insere total de memória
memoswap = psutil.swap_memory().total     #Insere total de memória swap

'''
Ajuda do stack overflow
https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778#37423778
'''
#Inicio da função
def byteformat(B):
       'Return the given bytes as a human friendly KB, MB, GB, or TB string'
       B = float(B)
       KB = float(1024)
       MB = float(KB ** 2) # 1,048,576
       GB = float(KB ** 3) # 1,073,741,824
       TB = float(KB ** 4) # 1,099,511,627,776

       if B < KB:
          return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
       elif KB <= B < MB:
          return '{0:.2f} KB'.format(B/KB)
       elif MB <= B < GB:
          return '{0:.2f} MB'.format(B/MB)
       elif GB <= B < TB:
          return '{0:.2f} GB'.format(B/GB)
       elif TB <= B:
          return '{0:.2f} TB'.format(B/TB)
#Fim da função
'''
Fim ajuda do stack overflow
'''


#Print das informações de memória e memória swap
print("Memória total:", byteformat(memototal), "\nTotal memória swap:", byteformat(memoswap))


