import random

def casilleros_serpientes_y_escaleras(escaleras:dict,serpientes:dict,tipo_de_casillero:dict) ->None:
    """
    Pre: Recibe diccionarios donde estan las serpientes y escaleras.
    Post: Crea llaves segun el numero de casillero y les asigna un tipo de casillero.
    """
    lista_de_escaleras = escaleras.keys()
    for i in lista_de_escaleras:
        tipo_de_casillero.update({i:"ESCALERA"})
    lista_de_serpientes = serpientes.keys()
    for i in lista_de_serpientes:
        tipo_de_casillero.update({i:"SERPIENTE"})    
    

def casillero_rushero(tipo_de_casillero:dict, casilleros_tweaks:dict) -> None:
    """
    Pre: Recibe diccionarios donde se chequea que no se repitan valores.
    Post: Crea llaves y valores y los agrega a tipo_de_csillero para el casillero rushero.
    """
    numero_valido = 0

    while numero_valido == 0:
        casillero_rushero= random.randint(1,100)
        
        if casillero_rushero%10!=0  and casillero_rushero!=1 and casillero_rushero not in casilleros_tweaks or casillero_rushero not in casilleros_tweaks.values():
            numero_valido+=1

    movimientos_rushero = casillero_rushero

    while movimientos_rushero%10!=0:
        movimientos_rushero= movimientos_rushero + 1
    casilleros_tweaks.update({casillero_rushero:movimientos_rushero})
    tipo_de_casillero.update({casillero_rushero:"RUSHERO"})
    
def casillero_hongos_locos(tipo_de_casillero:dict, casilleros_tweaks:dict) ->None :
    """
    Pre: Recibe diccionarios donde se chequea que no se repitan valores.
    Post: Crea llaves y valores y los agrega a tipo_de_casilleros segun condiciones para el casillero hongos locos.
    """
    
    numero_valido = 0
    
    while numero_valido == 0:
        casillero_hongos_locos = random.randint(1,100)
        if casillero_hongos_locos%10!=0 and casillero_hongos_locos%10!=1 and casillero_hongos_locos!=1  and casillero_hongos_locos not in casilleros_tweaks or casillero_hongos_locos not in casilleros_tweaks.values():
            numero_valido+=1
    
    movimientos_hongos_locos = casillero_hongos_locos
    while movimientos_hongos_locos%10!=1:
        movimientos_hongos_locos= movimientos_hongos_locos - 1
    
    casilleros_tweaks.update({casillero_hongos_locos : movimientos_hongos_locos})
    tipo_de_casillero.update({casillero_hongos_locos:"HONGOS LOCOS"})
    
def casillero_cascara_de_banana(tipo_de_casillero:dict, casilleros_tweaks:dict)-> None:
    """
    Pre: Recibe diccionarios donde se chequea que no se repitan valores.
    Post: Crea llaves y valores y los agrega a tipo_de_casilleros segun condiciones para el casillero cascara de banana.
    """
    for i in range(5):
        n_cascara_de_banana= random.randint(1,100)
        movimiento_cascara_de_banana = n_cascara_de_banana-20
        while n_cascara_de_banana <=20  or n_cascara_de_banana in casilleros_tweaks or n_cascara_de_banana in casilleros_tweaks.values() or casillero_cascara_de_banana==100 or movimiento_cascara_de_banana in casilleros_tweaks.values() or movimiento_cascara_de_banana in casilleros_tweaks.keys(): 
            n_cascara_de_banana= random.randint(1,100)
            movimiento_cascara_de_banana = n_cascara_de_banana-20
        tipo_de_casillero.update({n_cascara_de_banana:"CASCARA DE BANANA"})
        casilleros_tweaks.update({n_cascara_de_banana:movimiento_cascara_de_banana})

def casillero_magico(tipo_de_casillero:dict, casilleros_tweaks:dict)->None:
    """
    Pre: Recibe diccionarios donde se chequea que no se repitan valores.
    Post: Crea llaves y valores y los agrega a tipo_de_casilleros segun condiciones para el casillero cascara de banana.
    """
    for i in range (3):
        n_casillero_magico= random.randint(2,99)
        movimiento_casillero_magico = random.randint(2,99)
        while n_casillero_magico  in casilleros_tweaks.keys() or n_casillero_magico in casilleros_tweaks.values() or movimiento_casillero_magico in casilleros_tweaks.keys() or movimiento_casillero_magico in casilleros_tweaks.values():
            n_casillero_magico = random.randint(2,99)
            movimiento_casillero_magico = random.randint(2,99)
        casilleros_tweaks.update({n_casillero_magico:movimiento_casillero_magico})
        tipo_de_casillero.update({n_casillero_magico:"MAGICO"})
        
def arma_diccionario_de_tweaks(serpientes, escaleras, tipo_de_casillero,casilleros_tweaks) -> dict:
    """
    Pre:Llama a las funciones de los casilleros especiales.
    Post: Devuelve un diccionario con todos los valores de los casilleros especiales.
    """
    casilleros_serpientes_y_escaleras(serpientes, escaleras, tipo_de_casillero)
    casillero_rushero(tipo_de_casillero, casilleros_tweaks)
    casillero_hongos_locos(tipo_de_casillero, casilleros_tweaks)
    casillero_cascara_de_banana(tipo_de_casillero, casilleros_tweaks)
    casillero_magico(tipo_de_casillero, casilleros_tweaks)
    return casilleros_tweaks,tipo_de_casillero

def num_dado() -> int:
    """
    Pre: Elije un numero al azar entre 1 y 6.
    Post: Devuelve un numero.
    """
    numero_dado= random.randint(1, 6)
    return numero_dado

def quien_empieza() ->int:
    """
    Pre: Elije un numero al azar entre 1 y 2.
    Post: Devuelve un numero.
    """
    comienza = random.randint(1,2)
    return comienza
def posiciones_en_el_tablero(posicion_a,posicion_b) -> None:
    """
    Pre: Recibe el valor de las posiciones para cambiarlas en la matriz
    Post: Crea una matriz donde se indica la posiciones de los jugadores
    """
    matriz=[]
    fila=[]
    cont= 101
    
    for i in range(0,10):
        for j in range(0,10):
            cont-=1
            fila.append(cont)
        if i % 2 != 0:
            fila.reverse()
        matriz.append(fila)
        fila=[]

    for i in range(0,10):
        for j in range(0,10):
            valor = matriz[i][j]
            if valor == posicion_a:
                matriz[i][j] = '[A]'
            if valor == posicion_b :
                matriz[i][j] = '[B]'
            if valor == posicion_a and valor == posicion_b:
                matriz[i][j] = '[X]'
            print('\t',matriz[i][j], end='')
        print('')

        
def tablero(jugador,posicion,casilleros_tweaks,tipo_de_casillero, estadisticas) -> int:
    """
    Pre: Jugabilidad
    Post: Posicion del jugador
    """
    meta=100
    print(f"Es el turno del jugador :{jugador}")
    print(f"la posicion actual de {jugador} es {posicion}")
    
    if posicion < meta:            
        tirar_dado = input ("Ingrese un numero para tirar el dado: ")
        while not tirar_dado.isdigit():
            print("El valor ingresado no es un numero, ingrese un numero para tirar el dado: ")                
            tirar_dado = input ("Ingrese un numero para tirar el dado: ")                
        contador_dado = num_dado()            
        posicion += contador_dado            
        print("El dado cayo en el: ", contador_dado)     
                
        if posicion in tipo_de_casillero:  
            print(f"{jugador} esta en el casillero {posicion}")          
            print("Caiste en un casillero", tipo_de_casillero[posicion])
            estadisticas[tipo_de_casillero[posicion]] += 1         
            posicion = casilleros_tweaks[posicion]   
        print (f" {jugador} esta en el casillero {posicion}")
    return posicion 

def jugar(jugador_1,jugador_2,casilleros_tweaks, tipo_de_casillero, estadisticas)-> None:
    """
    Pre: Segun quien_empieza() se elije los turnos
    Post: Sistema de turnos
    """
    turno = quien_empieza()
    posicion_a=0
    posicion_b=0
    matriz = []
    fila = []
    cont=101
    
    while posicion_a<100 and posicion_b <100:
        if turno==1 and posicion_b <100:
            posicion_a = tablero(jugador_1,posicion_a,casilleros_tweaks,tipo_de_casillero, estadisticas)
        
            if posicion_a>=100:
                print(f"Gano {jugador_1}")
            turno =2
        posiciones_en_el_tablero(posicion_a,posicion_b)
            
            
        if turno==2 and posicion_a<100:
            posicion_b = tablero(jugador_2,posicion_b,casilleros_tweaks,tipo_de_casillero, estadisticas)
            
            if posicion_b>=100:
                print(f"Gano {jugador_2}")
            turno=1
        posiciones_en_el_tablero(posicion_a,posicion_b)

    print('Se termino el juego')

def estadistica_vacia(estadistica):
    
    if estadistica:
        print(estadistica)
        return False
    else:
        print("Está vacía, todavía no se jugo ninguna partida")
        return True
    
                 
def main() -> None:
    '''
    Pre: Imprime un menú con opciones para el usuario. 
    Post: Según las opciones elegidas llama a las funciones indicadas, y el programa finaliza cuando se elige la opción de salir.
    '''
    escaleras = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96}
    serpientes = {86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
    tipo_de_casillero = {}
    estadisticas = {"ESCALERA" : 0,"SERPIENTE" : 0, "RUSHERO": 0 ,"HONGOS LOCOS": 0, "CASCARA DE BANANA": 0 ,"MAGICO":0}
    lista = []
    casilleros_tweaks = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
    lista = arma_diccionario_de_tweaks(escaleras,serpientes,tipo_de_casillero,casilleros_tweaks)  
    casilleros_tweaks = lista[0]
    tipo_de_casillero = lista[1]
    opciones=0
    salir = 0
    
    
    while salir !=1:
        opciones=int(input('Bienvenido a Serpientes y Escaleras, Ingrese:\n[1]Para jugar\n[2]Para ver estadistica de tweaks\n[3]Reiniciar estadisticas\n[4]Salir\n'))
        
        if opciones == 1:
            print()
            jugador_1 = input ("Ingrese su nombre jugador A: ")
            jugador_2 = input ("Ingrese su nombre jugador B: ")
            jugar(jugador_1,jugador_2,casilleros_tweaks,tipo_de_casillero, estadisticas)
        elif opciones == 2:
            if estadisticas["ESCALERA"] == 0 and estadisticas["SERPIENTE"] == 0 and estadisticas["RUSHERO"] == 0 and estadisticas["HONGOS LOCOS"] == 0 and estadisticas["CASCARA DE BANANA"] == 0 and estadisticas["MAGICO"] ==0:
                print("No hay estadisticas")
            else:
                print(estadisticas)
        elif opciones == 3:
            estadisticas = {"ESCALERA" : 0,"SERPIENTE" : 0, "RUSHERO": 0 ,"HONGOS LOCOS": 0, "CASCARA DE BANANA": 0 ,"MAGICO":0}
            print("Se reiniciaron las estadisticas")
            print(estadisticas)
        elif opciones == 4:
            salir = 1
              
  
main()




