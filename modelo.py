from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Linea:
    id: int
    frecuencia: float
    frecuencia_punta:float

    
@dataclass(frozen=True)
class Estacion:
    id: str         # id interno
    nombre: str     # Nombre literal que se muestra al usuario
    linea: Linea      # Número de la linea
    lat: float      # Latitud
    lon: float      # Longitud
    subterraneo: bool = False
    ascensor: bool = True
    mecanicas: bool = True


    


@dataclass
class Conexion:
    nodo1: Estacion        # estacion 1
    nodo2: Estacion        # estacion 2
    tipo: str           # "tramo" o "transbordo"
    distancia: float    # En km.
    minutos: float      # Coste base, antes de aplicar hora, clima, etc.

@dataclass
class Condiciones:
    clima_adverso: bool = False
    hora_punta: bool = False
    incidencia: bool = False

@dataclass
class RedMetro:
    lineas: List[Linea] = field(default_factory=list)
    estaciones: List[Estacion] = field(default_factory=list)
    conexiones: List[Conexion] = field(default_factory=list)

GRAFO = RedMetro()
CONDICIONES = Condiciones()
