import psutil

for i in range(20): #Repetição até 20
    print("Tempo de CPU por núcleo:", psutil.cpu_percent(interval=1, percpu=True))  # Tempo da CPU por núcleos