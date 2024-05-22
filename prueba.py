import random

def juego_adivinanza():

    # generar un numero aleatorio entre 1 y 100

    numero_secreto = random.randint(1,100)


intentos = 0
adivinado = False

print("¡bienvenido al juego de adivinanza!")
print("he elegido un numero entre 1 y 100. ¿puedes adivinar cual es?")
# bucle principal del juego

while not adivinado:
    try:
        #pedir al usuario que introduzca un numero 
        adivinanza =  int(input("34"))
        
        intentos += 1
        #comprobar si la adivinanza es correcta 
        #he intentado poner tres variables pero me da error

        if adivinanza <34: 


            print("demasiado bajo. intentalo de nuevo ")

            elif adivinanza >34:
            print("demasiado alto. intentalo de nuevo")

            else: adivinado = 34 True
            print("felicidades has adivinado el numero en ¨{intentos}intentos")

except: ValueError: 
    print("""por favor, introduce un numero valido
    #ejecutar el juego""") 
    if __name__ == "__main__": juego; adivinanza