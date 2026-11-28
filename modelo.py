from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Linea:
    id: int                 #numero linea
    frecuencia: float       #frecuencia de trenes
    frecuencia_punta:float  #frecuencia de trenes en hora punta

    
@dataclass(frozen=True)
class Estacion:
    id: str           # id interno
    nombre: str       # Nombre de la Estacion
    linea: Linea      # Número de la linea
    lat: float        # Latitud
    lon: float        # Longitud
    subterraneo: bool = False #Estacion subterranea
    ascensor: bool = True #Estacion con ascensor
    mecanicas: bool = True #Estacion con escaleras mecanicas
 
@dataclass
class Conexion:
    nodo1: Estacion        # estacion 1
    nodo2: Estacion        # estacion 2
    tipo: str           # "tramo" o "transbordo"
    distancia: float    # En km.
    minutos: float      # tiempo base, antes de aplicar condiciones

@dataclass(frozen=True)
class Clima:
    normal:str="normal" #Clima que no afecta al metro
    lluvia: str="lluvia" #lluvia
    tormenta: str="tormenta" #tormenta

@dataclass(frozen=True)
class Incidencia:
    sin:str="sin incidencias" 
    leve:str="leve" #Retrasos leves
    grave: str="grave" #Retrasos impotantes
    suspendido: str="suspendido" #Tramos inaccesible

@dataclass(frozen=True)
class Tramo:
    tipo: Incidencia #leve, grave, suspendido
    estaciones: frozenset #Estaciones afectadas (solo id)

@dataclass
class Condiciones:
    clima: Clima=Clima.normal #Clima
    hora_punta: bool = False  #Hora punta
    incidencias: List[Tramo] = field(default_factory=list) #Lista de tramos con incidencias
    accesibilidad: bool =False #Camino accesible (ascensores en tranbordos)

@dataclass
class RedMetro:
    lineas: List[Linea] = field(default_factory=list) #Lineas del metro
    estaciones: List[Estacion] = field(default_factory=list) #Lista de todas las estaciones
    conexiones: List[Conexion] = field(default_factory=list) #Lista de todas las conexiones

GRAFO = RedMetro()
CONDICIONES = Condiciones()
FACTOR_CLIMA={Clima.normal:1.0,Clima.lluvia:1.05, Clima.tormenta:1.1}
FACTOR_PUNTA=1.05
RETRASO_INCIDENCIAS={Incidencia.sin:0.0,Incidencia.leve:10.0,Incidencia.grave:30.0,Incidencia.suspendido:0.0}
