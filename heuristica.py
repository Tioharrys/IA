from math import radians,sin ,cos ,sqrt, asin # importamos los metodos de math para realizar los calculos
from modelo import *

def distancia(origen: Estacion , destino: Estacion): 
    R = 6371 # radio de la tierra en kilometros

    lat1 = radians(origen.lat) #
    lat2 = radians(destino.lat) #

    Dlat= lat1 - lat2
    Dlon= radians(origen.lon - destino.lon)

    k = sin(Dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(Dlon / 2)**2

    return 2 * R *asin(sqrt(min(1.0, k)))

def heuristica(origen: Estacion , destino : Estacion ):
    return distancia(origen,destino)/ 80 * 60 #80=vmax
