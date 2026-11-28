# Clase del algoritmo A*.
# Algoritmo A*
import heapq
from itertools import count
import modelo
from heuristica import *
class AEstrella:
    def a_estrella(origen: Estacion, destino: Estacion):
        if modelo.CONDICIONES.hora_punta:#Si es hora punta
            tiempo_subida=origen.linea.frecuencia_punta/2 # tiempo de espera de subida en hora punta
        else:#Si es hora valle
            tiempo_subida=origen.linea.frecuencia/2#tiempo de espera de subida en hora valle
                
        g={origen:tiempo_subida}#diccionario con los pesos acumulados
        
        padre = {origen: None}#padres de los nodos
        camino= [] #camino optimo
        contador= count()#contador para ordenar en heap en caso de empate
        abierta=[(heuristica(origen,destino)+g.get(origen) , next(contador),origen)] # Lista abierta(nodos no evaluados) ordenado por f(n)
        cerrada=set()# Lista cerrada vacia (nodos evaluados)
         
        for tramo in modelo.CONDICIONES.incidencias:#Si la estacion origen esta suspendida, la ruta no esta disponible
            if tramo.tipo==Incidencia.suspendido and origen.id in tramo.estaciones:
                return None

      

        while abierta:#mientras haya nodos en la lista abierta

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
                nuevo_g = g[actual] + coste #tiempo acumulado sumado al vecino actual

                if nuevo_g < g.get(adyacente, float("inf")): #Si es menor que el que ya teniamos, escogemos el vecino actual
                    g[adyacente] = nuevo_g
                    padre[adyacente] = actual 
                    f=nuevo_g + heuristica(adyacente,destino)#calculamos su f(n)

                    heapq.heappush(abierta,(f,next(contador),adyacente))#Lo añadimos al monticulo en la posicion que le corresponde en base a su f(n)
        return None#Si no existe un camino
    
    def lista_adyacentes(actual: Estacion):#Devuelve lista con los nodos adyacentes
        adyacentes=[]
        for conexion in modelo.GRAFO.conexiones:# Por cada conexion buscamos aquellas en las q se encuentre nodo actual y #asignamos vecino al otro nodo en la conexion
            
            if conexion.nodo2.id == actual.id:
                vecino=conexion.nodo1
            
            elif conexion.nodo1.id == actual.id:
                vecino=conexion.nodo2
           
            else:
                continue

            tiempo_real=AEstrella.tiempo_real(conexion,actual, vecino)#Si hemos encontrado conexion valida calculamos su tiempo real

            if tiempo_real is None:#Si pertenece a un tramo cortado
                continue#escogemos otro vecino si es posible

            if conexion.tipo =="transbordo": #Si es tranbordo le sumamos su tiempo de espera correspondiente

                if modelo.CONDICIONES.accesibilidad:#Si modo accesible esta activado
                    if not (actual.ascensor and vecino.ascensor):#escogemos aquellos vecinos transbordos con ascensores
                        continue

                if modelo.CONDICIONES.hora_punta:#si es hora punta
                    tiempo_real+=vecino.linea.frecuencia_punta/2
                
                else:#Si es hora valle
                    tiempo_real+=vecino.linea.frecuencia/2

                if vecino.mecanicas or vecino.ascensor:#Si tiene ascensores o escaleras mecanicas se ahorra 30 segundos aprox.
                    tiempo_real-=0.5
            
            adyacentes.append((vecino,tiempo_real))#añadimos vecino con su tiempo
        return adyacentes # Lista de adyacentes
    
    def tiempo_real(conexion:Conexion,nodo1:Estacion,nodo2:Estacion):#Calculo tiempo de conexion

        cond=modelo.CONDICIONES
        tiempo=conexion.minutos#tiempo ideal o base
        tiempo*=FACTOR_CLIMA[cond.clima]#tiempo cambia dependiendo del clima con un factor por cada estacion
        if modelo.CONDICIONES.hora_punta:#tiempo cambia dependiendo de hora con un factor por cada estacion
            tiempo*=FACTOR_PUNTA
        
    
        for tramo in cond.incidencias:# Si hay alguna incidencia
            actual_dentro=nodo1.id in tramo.estaciones#Comprobamos si los nodos estan implicados en alguna
            vecino_dentro=nodo2.id in tramo.estaciones

            if not actual_dentro and vecino_dentro and conexion.tipo=="tramo":#Si no hemos entrado todavia al tramo con incidencia, lo tratamos

                if tramo.tipo == Incidencia.suspendido:#Comprobamos si es suspension
                    return None#escogemos otro vecino si es posible
                
                else:#Si estan implicados en alguna otra incidencia
                  tiempo+=RETRASO_INCIDENCIAS[tramo.tipo]#Sumamos su tiempo de retraso correspondiente(solo al entrar)

            elif conexion.tipo=="transbordo":#Si es transbordo
                if actual_dentro and not vecino_dentro:#Si salimos de un tramo con incidencia, lo ignoramos
                    continue
                elif not actual_dentro and vecino_dentro:#Si al hacer transbordo vamos a un tramo con incidencia
                    tiempo+=RETRASO_INCIDENCIAS[tramo.tipo]#Sumamos su tiempo de retraso correspondiente
        return tiempo
        

