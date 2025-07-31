import time
import asyncio
import msvcrt

tiempo =[0, 0, 0]
temporizador = True

async def main():
    while(temporizador == True):
        tiempo[0] += 1
        if tiempo[0] >= 60:
            tiempo[0] = 0
            tiempo[1] += 1
        if tiempo[1] >= 60:
            tiempo[1] = 0
            tiempo[2] += 1
        print ("segundos:", tiempo[0], "minutos:", tiempo[1]," horas:", tiempo[2])
        await asyncio.sleep(1)
        if msvcrt.kbhit():
            if msvcrt.getch().decode('utf-8').lower() == 'Esc':
                break



print("puta madre")