# Clase del algoritmo A*.
# Algoritmo A*
import heapq
from itertools import count
import modelo
from heuristica import *
class AEstrella:
    def a_estrella(origen: Estacion, destino: Estacion):
        contador= count()
        abierta=[(heuristica(origen,destino) , next(contador),origen)] # Lista abierta(nodos no evaluados) ordenado por f(n)
        cerrada=set()# Lista cerrada vacia (nodos evaluados)
        if modelo.CONDICIONES.hora_punta:
            tiempo_subida=origen.linea.frecuencia_punta/2 # tiempo de espera de subida en hora punta
        else:
            tiempo_subida=origen.linea.frecuencia/2
        if origen.mecanicas or origen.ascensor:
            tiempo_subida-=0.5
        
        g={origen:tiempo_subida}

        padre = {origen: None}#padres de los nodos
        camino= [] #camino optimo

        while abierta:
            _,_,actual=heapq.heappop(abierta)#Extraemos el nodo con menor f(n)

            if actual in cerrada: # Si el nodo actual ya lo hemos evaluado nos lo saltamos
                continue

            if actual == destino:#Si hemos llegado al destino generamos el camino
                while actual is not None:
                    camino.append(actual) #Añadimos el nodo actual
                    actual=padre[actual] #Saltamos a su padre
                return camino[::-1], g[destino] #Invertimos orden
            
            cerrada.add(actual) #Añadimos nodo a lista cerrada porque lo vamos a evaluar
            for adyacente, coste in AEstrella.lista_adyacentes(actual): #Recorremos los adyacentes del nodo actual
                nuevo_g = g[actual] + coste #Coste con vecino actual
                if nuevo_g < g.get(adyacente, float("inf")): #Si es menor que el que ya teniamos, lo actualizamos
                    g[adyacente] = nuevo_g
                    padre[adyacente] = actual 
                    f=nuevo_g + heuristica(adyacente,destino)#calculamos su f(n)
                    heapq.heappush(abierta,(f,next(contador),adyacente))#Lo añadimos en el monticulo en la posicion que le corresponde en base a su f(n)
        return None
    
    def lista_adyacentes(actual: Estacion):
        adyacentes=[]
        for conexion in modelo.GRAFO.conexiones:# Por cada conexion buscamos adyacentes al nodo
            if conexion.nodo2.id == actual.id:
                vecino=conexion.nodo1
            elif conexion.nodo1.id == actual.id:
                vecino=conexion.nodo2
            else:
                continue
            tiempo_real=conexion.minutos * AEstrella.retraso(actual,vecino)#Si es vecino añadimos su tiempo real a la lista adyacentes
            if conexion.tipo =="transbordo": #Si es tranbordo le sumamos su tiempo de espera correspondiente
                if modelo.CONDICIONES.accesibilidad:
                    if not (actual.ascensor and vecino.ascensor):
                        continue
                if modelo.CONDICIONES.hora_punta:
                    tiempo_real+=vecino.linea.frecuencia_punta/2
                else:
                    tiempo_real+=vecino.linea.frecuencia/2
                if vecino.mecanicas or vecino.ascensor:
                    tiempo_real-=0.5
            
            adyacentes.append((vecino,tiempo_real))
        return adyacentes # Lista de adyacentes
    
    def retraso(nodo1: Estacion,nodo2: Estacion):
        factor=1.0
        if modelo.CONDICIONES.clima_adverso:
            factor *=1.10
        if modelo.CONDICIONES.hora_punta:
            factor*=1.25
        if modelo.CONDICIONES.incidencia== (nodo1,nodo2):
            factor*=3.0
        return factor

