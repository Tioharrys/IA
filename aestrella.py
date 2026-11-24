# Clase del algoritmo A*.
# Algoritmo A*
import heapq
class AEstrella:
    def a_estrella(origen: str, destino: str, adyacentes, h, grafo):
        abierta=[(origen, h(origen))] # Lista abierta(nodos no evaluados)
        cerrada=set()# Lista cerrada vacia (nodos evaluados)
        g = {origen: 0} # peso de nodos
        padre = {origen: None}#padres de los nodos
        camino= [] #camino optimo

        while abierta:
            _,actual=heapq.heappop(abierta)#Extraemos el nodo con menor f

            if actual in cerrada: # Si el nodo actual ya lo hemos evaluado nos lo saltamos
                continue

            if actual == destino:#Si hemos llegado al destino generamos el camino
                while actual is not None:
                    camino.append(actual) #Añadimos el nodo actual
                    actual=padre(actual) #Saltamos a su padre
                return camino[::-1] #Invertimos orden
            
            cerrada.add(actual) #Añadimos nodo a lista cerrada porque lo vamos a evaluar
            for adyacente, coste in adyacentes(actual, grafo): #Recorremos los adyacentes del nodo actual
                nuevo_g =g[actual] + coste
                if nuevo_g < g.get(adyacente, float("inf")):
                    g[adyacente]=nuevo_g
                    padre[adyacente]= actual
                    f=nuevo_g+ h(adyacente)
                    heapq.heappush(abierta,f,adyacente)
        return None
    
    def adyacencia(actual,grafo,condiciones):
        adyacentes=[]
        for vecino, distancia ,tiempo_ideal in grafo[actual]:
            tiempo_real=tiempo_ideal* retraso(condiciones,actual,vecino)
            adyacentes.append((vecino,distancia,tiempo_real))
        return adyacentes
    
    def retraso(condiciones ,a ,b):
        factor=1.0
        if condiciones.get("lluvia"):
            factor *=1.10
        if condiciones.get("hora punta"):
            factor*=1.25
        if condiciones.get("incidencia") == (a,b):
            factor*=3.0
        return factor

    

