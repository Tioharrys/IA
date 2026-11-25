from heuristica import heuristica
from aestrella import AEstrella
from grafo import *
import modelo
def getEstacion(id: str) -> Estacion:
    estacion = [a for a in modelo.GRAFO.estaciones if a.id == id]
    if estacion:
        return estacion[0]
    return None

def main():
    modelo.GRAFO = construir_red()
    origen = getEstacion("SEN")
    destino = getEstacion("HME")
    res= AEstrella.a_estrella(origen,destino)
    if res is not None:
        camino,tiempo=res
        minutos,segundos=divmod(round(tiempo*60),60)

        for estacion in camino:
            print(estacion.nombre,estacion.linea.id)

        print("Tiempo total:",minutos,"minutos" ,segundos, "segundos")



if __name__ == "__main__":
    main()


