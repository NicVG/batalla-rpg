import random
from numpy.random import choice

class Personaje:
    def __init__(self,n,ab,mb,db,dmb,v):
        self.nombre = n
        self.ataque_base = ab
        self.magia_base = mb
        self.defensa_base = db
        self.defensa_magica_base=dmb
        self.velocidad = v
        
class Jugador(Personaje):
    def __init__(self,n,ab,mb,db,dmb,v):
        super().__init__(n,ab,mb,db,dmb,v)
        self.arma = ("",0,0)
        self.equipo = ("",0,0)
        self.item_activo = []
        self.item_pasivo = []
        self.vida_total = 20
        self.vida_actual = self.vida_total
        self.magia_total = 10
        self.magia_actual = self.magia_total
        
    def daño_total(self,extra):
        return self.ataque_base + extra + self.arma[1]
        
    def daño_magia_total(self,extra):
        return self.magia_base + extra + self.arma[2] + 2

class Enemigo(Personaje):
    def __init__(self,n,ab,mb,db,dmb,v,vt):
        super().__init__(n,ab,mb,db,dmb,v)
        self.vida_total = vt
        self.vida_actual = self.vida_total

nombre_jugador=input("Ingresa tu nombre.\n")
print("\n")
        
jugador=Jugador(nombre_jugador,random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))
        
enemigos=((25,"Conejo malvado",7,7,5,5,2,10),(20,"Goblin",8,7,6,5,3,15),
          (20,"Mago oscuro",7,9,5,7,3,15),(15,"Orco",9,8,7,6,4,20),
          (15,"Demonio",9,9,7,7,4,20),(5,"Dios",11,11,9,9,6,50))

probabilidades_enemigos = []

for enemigo in enemigos:
    probabilidades_enemigos.append(enemigo[0] / 100)

armas={"1":("Cuchillo",3,1),"2":("Baston",2,2),"3":("Amuleto",1,3)}

print(jugador.nombre+" despierta en medio de un bosque y se encuentra frente a 3 objetos.\n")
print("1) Cuchillo")
print("2) Baston")
print("3) Amuleto")
print("\n")

seleccion=-1

while seleccion not in ("1","2","3"):
    seleccion=input("Selecciona uno de los 3.\n")
    if seleccion not in ("1","2","3"):
        print("Debes seleccionar 1, 2 o 3.\n")
    else:
        jugador.arma=armas[seleccion]
        print(jugador.nombre+" ha tomado el "+jugador.arma[0]+".\n")

seleccion=-1
esc=False
        
input("Tras elegir un objeto "+jugador.nombre+" escucha algo acercarse por la espalda.")

enemigo_elegido = int(choice(range(0,len(enemigos)),p=probabilidades_enemigos))

enemigo_actual=Enemigo(*enemigos[enemigo_elegido][1:])

input("Al girar se encuentra con un "+enemigo_actual.nombre+"!")
print("\n")
print("HA COMENZADO UNA BATALLA!")

while (jugador.vida_actual and enemigo_actual.vida_actual)!=0 and esc==False:
    
    print("\n")
    seleccion=-1
    
    while seleccion not in ("1","2","3","4"):
        print("Selecciona una acción!")
        print("1) Ataque fisico")
        print("2) Ataque magico (coste 2 MP)")
        print("3) Usar item")
        print("4) Intentar huir")
        seleccion=input("\n")
    if seleccion not in ("1","2","3","4"):
        print("Debes seleccionar 1, 2, 3 o 4.\n")
        
    print("\n")
    
    if seleccion=="1":
        if jugador.velocidad >= enemigo_actual.velocidad:
            input(jugador.nombre+" ha atacado a su oponente.")
            dado=random.randint(1,6)
            input("Para atacar has tirado el dado y ha salido "+str(dado)+".")
            ataque_final=jugador.daño_total(dado)
            daño = ataque_final - enemigo_actual.defensa_base
            if daño < 0:
                daño = 0
            input("Con lo que "+jugador.nombre+" le ha hecho "+str(daño)+" de daño a "+enemigo_actual.nombre+".")
            enemigo_actual.vida_actual = enemigo_actual.vida_actual - daño
            if enemigo_actual.vida_actual < 0:
                enemigo_actual.vida_actual = 0
            input(enemigo_actual.nombre+" ahora tiene ["+str(enemigo_actual.vida_actual)+"/"+str(enemigo_actual.vida_total)+"] de HP.")
            if enemigo_actual.vida_actual==0:
                input("Has derrotado a "+enemigo_actual.nombre+"!")
                break
            print("\n")
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_base + jugador.equipo[1])
            else:
                daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_magica_base + jugador.equipo[2])
            if daño_enemigo < 0:
                daño_enemigo = 0
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                input(enemigo_actual.nombre+" ha atacado de vuelta y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            else:
                input(enemigo_actual.nombre+" ha atacado de vuelta con un hechizo y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            jugador.vida_actual = jugador.vida_actual - daño_enemigo
            if jugador.vida_actual < 0:
                jugador.vida_actual = 0
            input(jugador.nombre+" ahora tiene ["+str(jugador.vida_actual)+"/"+str(jugador.vida_total)+"] de HP.")
            if jugador.vida_actual==0:
                input("Has sido derrotado...")
        else:
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_base + jugador.equipo[1])
            else:
                daño_enemigo = enemigo_actual.magia_base - (jugador.defensa_magica_base + jugador.equipo[2])
            if daño_enemigo < 0:
                daño_enemigo = 0
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            else:
                input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" con un hechizo y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            jugador.vida_actual = jugador.vida_actual - daño_enemigo
            if jugador.vida_actual < 0:
                jugador.vida_actual = 0
            input(jugador.nombre+" ahora tiene ["+str(jugador.vida_actual)+"/"+str(jugador.vida_total)+"] de HP.")
            if jugador.vida_actual==0:
                input("Has sido derrotado...")
                break
            input(jugador.nombre+" ataca de vuelta a su oponente.")
            dado=random.randint(1,6)
            input("Para atacar has tirado el dado y ha salido "+str(dado)+".")
            ataque_final=jugador.daño_total(dado)
            daño = ataque_final - enemigo_actual.defensa_base
            if daño < 0:
                daño = 0
            input("Con lo que "+jugador.nombre+" le ha hecho "+str(daño)+" de daño a "+enemigo_actual.nombre+".")
            enemigo_actual.vida_actual = enemigo_actual.vida_actual - daño
            if enemigo_actual.vida_actual < 0:
                enemigo_actual.vida_actual = 0
            input(enemigo_actual.nombre+" ahora tiene ["+str(enemigo_actual.vida_actual)+"/"+str(enemigo_actual.vida_total)+"] de HP.")
            if enemigo_actual.vida_actual==0:
                input("Has derrotado a "+enemigo_actual.nombre+"!")
    
    
    elif seleccion=="2" and jugador.magia_actual<2:
        input("No tienes suficiente magia.")
        input("Magia actual: ["+jugador.magia_actual+"/"+jugador.magia_total+".")
    
    
    elif seleccion=="2" and jugador.magia_actual>2:
        jugador.magia_actual -= 2
        if jugador.velocidad >= enemigo_actual.velocidad:
            input(jugador.nombre+" ha lanzado un hechizo.")
            dado=random.randint(1,6)
            input("Para realizar el hechizo has tirado el dado y ha salido "+str(dado)+".")
            ataque_final=jugador.daño_magia_total(dado)
            daño = ataque_final - enemigo_actual.defensa_magica_base
            if daño < 0:
                daño = 0
            input("Con lo que "+jugador.nombre+" le ha hecho "+str(daño)+" de daño a "+enemigo_actual.nombre+".")
            enemigo_actual.vida_actual = enemigo_actual.vida_actual - daño
            if enemigo_actual.vida_actual < 0:
                enemigo_actual.vida_actual = 0
            input(enemigo_actual.nombre+" ahora tiene ["+str(enemigo_actual.vida_actual)+"/"+str(enemigo_actual.vida_total)+"] de HP.")
            if enemigo_actual.vida_actual==0:
                input("Has derrotado a "+enemigo_actual.nombre+"!")
                break
            print("\n")
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_base + jugador.equipo[1])
            else:
                daño_enemigo = enemigo_actual.magia_base - (jugador.defensa_magica_base + jugador.equipo[2])
            if daño_enemigo < 0:
                daño_enemigo = 0
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                input(enemigo_actual.nombre+" ha atacado de vuelta y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            else:
                input(enemigo_actual.nombre+" ha atacado de vuelta con un hechizo y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            jugador.vida_actual = jugador.vida_actual - daño_enemigo
            if jugador.vida_actual < 0:
                jugador.vida_actual = 0
            input(jugador.nombre+" ahora tiene ["+str(jugador.vida_actual)+"/"+str(jugador.vida_total)+"] de HP.")
            if jugador.vida_actual==0:
                input("Has sido derrotado...")
        else:
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_base + jugador.equipo[1])
            else:
                daño_enemigo = enemigo_actual.magia_base - (jugador.defensa_magica_base + jugador.equipo[2])
            if daño_enemigo < 0:
                daño_enemigo = 0
            if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            else:
                input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" con un hechizo y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
            jugador.vida_actual = jugador.vida_actual - daño_enemigo
            if jugador.vida_actual < 0:
                jugador.vida_actual = 0
            input(jugador.nombre+" ahora tiene ["+str(jugador.vida_actual)+"/"+str(jugador.vida_total)+"] de HP.")
            if jugador.vida_actual==0:
                input("Has sido derrotado...")
                break
            input(jugador.nombre+" contraataca lanzando un hechizo.")
            dado=random.randint(1,6)
            input("Para atacar has tirado el dado y ha salido "+str(dado)+".")
            ataque_final=jugador.daño_magia_total(dado)
            daño = ataque_final - enemigo_actual.defensa_magica_base
            if daño < 0:
                daño = 0
            input("Con lo que "+jugador.nombre+" le ha hecho "+str(daño)+" de daño a "+enemigo_actual.nombre+".")
            enemigo_actual.vida_actual = enemigo_actual.vida_actual - daño
            if enemigo_actual.vida_actual < 0:
                enemigo_actual.vida_actual = 0
            input(enemigo_actual.nombre+" ahora tiene ["+str(enemigo_actual.vida_actual)+"/"+str(enemigo_actual.vida_total)+"] de HP.")
            if enemigo_actual.vida_actual==0:
                input("Has derrotado a "+enemigo_actual.nombre+"!")
            
            
    elif seleccion=="3":
        if jugador.item_activo==[]:
            print("El inventario esta vacio.")
        else:
            for objeto in jugador.item_activo:
                print(objeto)
                ##Pendiente: programar objetos activos y pasivos
    
    
    elif seleccion=="4":
        probabilidad_escape = int((1-(enemigo_actual.vida_actual)/enemigo_actual.vida_total)*100//1)
        if probabilidad_escape < 0:
            probabilidad_escape = 0
        seleccion2 = -1
        while seleccion2 not in ("1","2"):
            print("La probabilidad de escape es de "+str(probabilidad_escape)+"% (aumenta al dañar al enemigo), deseas intentar huir?")
            print("1) Si")
            print("2) No")
            seleccion2=input("")
            if seleccion2 not in ("1","2"):
                print("Debes ingresar 1 o 2")
            else:
                escape=random.randint(1,100)
                if seleccion2=="1":
                    if escape<=probabilidad_escape:
                        input("Has escapado con exito.")
                        esc = True
                    else:
                        input("No has logrado escapar")
                        if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                            daño_enemigo = enemigo_actual.ataque_base - (jugador.defensa_base + jugador.equipo[1])
                        else:
                            daño_enemigo = enemigo_actual.magia_base - (jugador.defensa_magica_base + jugador.equipo[2])
                        if daño_enemigo < 0:
                            daño_enemigo = 0
                        if enemigo_actual.ataque_base > enemigo_actual.magia_base:
                            input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
                        else:
                            input(enemigo_actual.nombre+" ha atacado a "+jugador.nombre+" con un hechizo y ha hecho "+str(daño_enemigo)+" de daño a "+jugador.nombre+".")
                        jugador.vida_actual = jugador.vida_actual - daño_enemigo
                        if jugador.vida_actual < 0:
                            jugador.vida_actual = 0
                        input(jugador.nombre+" ahora tiene ["+str(jugador.vida_actual)+"/"+str(jugador.vida_total)+"] de HP.")
                        if jugador.vida_actual==0:
                            input("Has sido derrotado...")
                        
                    

esc = False

print("\n")         
input("FIN DEL DEMO")            
