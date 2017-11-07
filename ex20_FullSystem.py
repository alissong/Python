import psutil

#Variaveis
dps = psutil.disk_partitions(all=True)           #Retorna info dos discos
fmt_str = "{:<8}"                                #Formata string
livre = psutil.disk_usage(path='c:').free        #Retorna espaco disponivel
espacototal = psutil.disk_usage(path='c:').total #Retorna espaco total

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


for i in (0,):
    dp = dps [i]
    print("Drive:",fmt_str.format(dp.device),
          "\nSistema de arquivo:", dp.fstype,
          "\nArmazenamento total:", byteformat(espacototal),
          "\nArmazenamento disponivel:", byteformat(livre)
          )