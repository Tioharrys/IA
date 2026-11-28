from modelo import *
def estaciones_clave (camino):
    claves=[]
    i=0
    destino=len(camino)-1#destino

    while(i<=destino):
        estacion=camino[i]
        if i==0:#estacion origen
            claves.append(("Origen",estacion))
        elif i== destino:
            claves.append(("Destino",estacion))
        else:
            if camino[i+1].linea.id != estacion.linea.id:#Si linea de estacion actual y la siguiente no son iguales es transbordo de bajada
                claves.append(("Transbordo (bajada)",estacion))
            if camino[i-1].linea.id != estacion.linea.id:
                claves.append(("Transbordo (subida)",estacion))#Si linea actual y la anterior no son iguales es transbordo de subida
        i+=1
    return claves#Lista de origen, destino y transbordos

def accesibilidad_camino(camino):
    claves=estaciones_clave(camino)
    informe=[]
    sin_ascensor=[]
    camino_acces = True

    for tipo, estacion in claves:
        if not estacion.ascensor:
            estado="Sin Ascensor"
            camino_acces=False#Si alguna estacion clave no cuenta con ascensor el camino deja de ser accesible
            sin_ascensor.append(f"{tipo}: {estacion.nombre} (Línea {estacion.linea.id}) - {estado}")
        else:#Si cuenta con ascensor es estacion accesible
            estado="Con Ascensor"
        informe.append(f"{tipo}: {estacion.nombre} (Línea {estacion.linea.id}) - {estado}")
    return sin_ascensor, camino_acces, informe




