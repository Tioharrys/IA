from modelo import *
def estaciones_clave (camino):
    claves=[]
    i=0
    ultimo=len(camino)-1
    while(i<=ultimo):
        estacion=camino[i]
        if i==0:
            claves.append(("Origen",estacion))
        elif i== ultimo:
            claves.append(("Destino",estacion))
        else:
            if camino[i+1].linea.id != estacion.linea.id:
                claves.append(("Transbordo (bajada)",estacion))
            if camino[i-1].linea.id != estacion.linea.id:
                claves.append(("Transbordo (subida)",estacion))
        i+=1
    return claves

def accesibilidad_camino(camino):
    claves=estaciones_clave(camino)
    informe=[]
    sin_ascensor=[]
    camino_acces = True
    for tipo, estacion in claves:
        if not estacion.ascensor:
            estado="Sin Ascensor"
            camino_acces=False
            sin_ascensor.append(f"{tipo}: {estacion.nombre} (Línea {estacion.linea.id}) - {estado}")
        else:
            estado="Con Ascensor"
        informe.append(f"{tipo}: {estacion.nombre} (Línea {estacion.linea.id}) - {estado}")
    return sin_ascensor, camino_acces, informe




