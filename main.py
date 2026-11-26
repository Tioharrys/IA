from heuristica import heuristica
from aestrella import AEstrella
from grafo import *
import modelo
from accesibilidad import accesibilidad_camino
def getEstacion(id: str) -> Estacion:
    estacion = [a for a in modelo.GRAFO.estaciones if a.id == id]
    if estacion:
        return estacion[0]
    return None

def main():
    modelo.GRAFO = construir_red()
    origen = getEstacion("GIZ-L2")
    destino = getEstacion("FUG-L1")
    if origen is None and destino is None:
            print("Estacion origen y destino no existentes")
            return None
    elif origen is None:
        print("Estacion origen no existente")
        return None
    elif destino is None:
         print("Estacion destino no existente")
         return None
   
    else:
        res= AEstrella.a_estrella(origen,destino)
        
        
    if res is not None:
        camino,tiempo=res
        minutos,segundos=divmod(round(tiempo*60),60)

        for estacion in camino:
            print(estacion.nombre,estacion.linea.id)

        print("Tiempo total:",minutos,"minutos" ,segundos, "segundos\n")

        sin_ascensor,camino_accesible,_=accesibilidad_camino(camino)
        print ("Accesiblidad (movilidad reducida):\n")
        """for linea in informe:
            print(" ",linea)"""
        if camino_accesible:
            print("Camino accesible: todas las estaciones claves tienen ascensores")
        else:
            print("Camnino no accesible:")
            for linea in sin_ascensor:
                print(" ",linea)



if __name__ == "__main__":
    main()
