import time
import datetime
tiempo = [0, 0, 0]
tiempot = [0, 0, 0]

def get_time(tiempo):
    filetempo = open("data/Registrodata.txt", "a")
    fecha_actual = datetime.now()
    mes = fecha_actual.month
    dia = fecha_actual.day
    filetempo.write(f"{dia}/{mes} {tiempo[2]}:{tiempo[1]}:{tiempo[0]}\n")
    filetempo.close()

def semana():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    fecha_actual = datetime.datetime.now()
    dia_semana = fecha_actual.weekday()
    print (dias [dia_semana])
    print (fecha_actual.isocalendar()[1])

def read_time():
    tiempot = [0, 0, 0]
    with open("data/Registrodata.txt", "r") as file:
        contenido = file.readlines()
    lineas = len(contenido)

    for i in range(lineas):
        z = contenido[i].split()
        print(z[0], z[1], z[2], z[3], z[4])
        tiempo = [int(z[2]), int(z[3]), int(z[4])]
        print("Tiempo registrado:", tiempo[2], "segundos,", tiempo[1], "minutos,", tiempo[0], "horas")
        Sumo(tiempot, tiempo)
    while tiempot[0] >= 60:
        tiempot[0] -= 60
        tiempot[1] += 1
    while tiempot[1] >= 60:
        tiempot[1] -= 60
        tiempot[2] += 1
    print("Tiempo total acumulado:", tiempot[0], "segundos,", tiempot[1], "minutos,", tiempot[2], "horas")
    

def Sumo(tiempot, tiempo):
    tiempot[0] = tiempot[0] + tiempo[0]
    tiempot[1] = tiempot[1] + tiempo[1]
    tiempot[2] = tiempot[2] + tiempo[2]
    
