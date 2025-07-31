import asyncio
import GordoGnus

def opcion1():
    print("hola soy la opcion1")
    asyncio.run(GordoGnus.main())

def opcion2():
    print("hola soy la opcion2")
    pressbtn = input("")

def opcion3():
    print("hola soy la opcion3")

def opcion4():
    print("hola soy la opcion4")
    pressbtn = input("")


menu = 0

#que nos cumplas feliz :3 
#tienes

while(menu != 5):
    print("1. opcion1")
    print("2. opcion2")
    print("3. opcion3")
    print("4. opcion4")
    print("5. salir")
    menu = int(input(""))
    print("")
    match menu:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            opcion4()
