import subprocess

p = subprocess.Popen("calc") # Cria o processo
print("PID do processo: ", p.pid) # Imprime PID do processo criado