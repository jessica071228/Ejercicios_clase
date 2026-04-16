#Jessica Maria Martinez Monterrosa
#Ingenieria en animacion digital
#ID: 00606503
#Reino del dragon
import random
print("Bienvenido al reino del dragon, querido jugador")
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}! Estás a punto de embarcarte en una gran aventura.")
print("Vas a tener que pasar tres niveles antes de llegar al tesoro.")
op = input("¿Quieres empezar la aventura? (si/no) ")

if op == "si":
    print("Perfecto!, vamos a empezar.")
    print("Primer nivel:", "hay dos cuevas, una con un dragon bueno y una con un dragon malo")
    print("Tu destino esta en tus manos, yo tampoco se cual es la cueva correcta, así que elige sabiamente.", "\n1. cueva izquierda\n2. cueva derecha")
    cueva = random.randint(1, 2)
    op1 = int(input("¿Cuál cueva eliges? "))
    if cueva != op1:
        print("Es que sos un gran chistoso, te salio el dragon malo, perdiste")
        quit()
    else:
         print("Vamos broder!, te salio el dragon bueno!")
         print("Segundo nivel:", "hay dos cuevas, una con un dragon bueno y una con un dragon malo")
         print("Tu destino esta en tus manos, yo tampoco se cual es la cueva correcta, así que elige sabiamente.", "\n1. cueva izquierda\n2. cueva derecha")
         cueva = random.randint(1, 2)
         op2= int(input("¿Cuál cueva eliges? "))
         if cueva != op2:
            print("Es que sos un gran chistoso, te salio el dragon malo, perdiste")
            quit()
         else:
            print("Vamos broder!, te salio el dragon bueno!")
            print("Tercer nivel:", "hay dos cuevas, una con un dragon bueno y una con un dragon malo")
            print("Tu destino esta en tus manos, yo tampoco se cual es la cueva correcta, así que elige sabiamente.", "\n1. cueva izquierda\n2. cueva derecha")
            cueva = random.randint(1, 2)
            op3= int(input("¿Cuál cueva eliges? "))
            if cueva != op3:
                print("Es que sos un gran chistoso, ya ibas bien, te salio el dragon malo, perdiste")
                quit()
            else:
              print("Felicidades!, te salio el dragon bueno y encontraste el tesoro!")

else:
    print("Bueno, espero que te animes a jugar pronto. ¡Hasta luego!")
