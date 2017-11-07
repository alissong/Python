import psutil, time
import subprocess

#Executa calculadora
subprocess.Popen("calc")

#Recebe nome do processo
procname = "calc.exe"

#Inicio da função
def pidstat():
    for proc in psutil.process_iter(): #Repetição retorna lista de processos
     if proc.name() == procname:       #Verifica a variavel que recebe o processo
         print("Status Processo:",proc,                               #Info basica do processo
               "\nProprietário:", proc.username(),                    #Propietario do processo
               "\nTempo de criação", time.ctime(proc.create_time()),  #Tempo de criação
               "\nMemória:", proc.memory_info().rss/1024 ,"KB"        #Exibe memória utilizada
              )
#Fim da função
pidstat()
