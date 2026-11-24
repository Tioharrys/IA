from dataclasses import dataclass

@dataclass
class Estacion:
    id: str         # id interno
    nombre: str     # Nombre literal que se muestra al usuario
    linea: int      # Número de la linea
    lat: float      # Latitud
    lon: float      # Longitud
    aire_libre: bool
    ascensor: bool

@dataclass
class Conexion:
    origen: str     # id
    destino: str    # id
    tipo: str       # "tramo" o "transbordo"
    minutos: float  # coste base, antes de aplicar hora, clima, etc.
    distancia: int  # en km.

