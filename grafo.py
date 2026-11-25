from collections import defaultdict
from modelo import *
from itertools import pairwise
import math


def construir_red():
    Lineas = [Linea1, Linea2, Linea3]
    Estaciones = NodosLinea1 + NodosLinea2 + NodosLinea3
    Conexiones = AristasLinea1 + AristasLinea2 + AristasLinea3 + Transbordos
    return RedMetro(lineas=Lineas, estaciones=Estaciones, conexiones=Conexiones)

Linea1=Linea(1,8,5.5)
Linea2=Linea(2,8,5)
Linea3=Linea(3,8,5)

NodosLinea1 = [
    Estacion("TAL", "Talleres",Linea1,25.7594371, -100.3684252, ascensor=False, mecanicas=False),
    Estacion("SBE", "San Bernabé",Linea1,25.7483612, -100.3616663, ascensor=False),
    Estacion("UMO", "Unidad Modelo",Linea1,25.7418611, -100.3549599, ascensor=False, mecanicas=False),
    Estacion("AZT", "Aztlán",Linea1 , 25.7321135, -100.3472684, ascensor=False, mecanicas=False),
    Estacion("PEN", "Penitenciaría",Linea1,25.7231259, -100.3425060, ascensor=False, mecanicas=False),
    Estacion("ALR", "Alfonso Reyes",Linea1,25.7158777, -100.3424665, ascensor=False, mecanicas=False),
    Estacion("MIT", "Mitras",Linea1,25.7058122, -100.3424008, ascensor=False, mecanicas=False),
    Estacion("SIB", "Simón Bolívar",Linea1,25.6986161, -100.3432248, ascensor=False, mecanicas=False),
    Estacion("HOS", "Hospital",Linea1,25.6918388, -100.3440744, ascensor=False, mecanicas=False),
    Estacion("EDI", "Edison",Linea1,25.6868900, -100.3336400, ascensor=False, mecanicas=False),
    Estacion("CEN", "Central",Linea1,25.6870015, -100.3243787, ascensor=False, mecanicas=False),
    Estacion("CUA-L1", "Cuauhtémoc",Linea1,25.6860024, -100.3169483),
    Estacion("DEG", "Del Golfo",Linea1,25.6848561, -100.3065260, ascensor=False, mecanicas=False),
    Estacion("FUG-L1", "Félix U. Gómez",Linea1,25.6839381, -100.2968826),
    Estacion("PAF", "Parque Fundidora",Linea1,25.6837882, -100.2881463, ascensor=False, mecanicas=False), # Revisar nombre
    Estacion("YGR", "Y Griega",Linea1,25.6832673, -100.2795402, ascensor=False, mecanicas=False),
    Estacion("ELC", "Eloy Cavazos",Linea1,25.6800469, -100.2641466, mecanicas=False),
    Estacion("LET", "Lerdo de Tejada",Linea1,25.6798419, -100.2522278, ascensor=False, mecanicas=False),
    Estacion("EXP", "Exposición (Terminal)",Linea1,25.6794983, -100.2453933, ascensor=False, mecanicas=False)
]

NodosLinea2 = [
    Estacion("SEN", "Sendero", Linea2, 25.7687489, -100.2928649),
    Estacion("TAP", "Tapia", Linea2, 25.7593298, -100.2956965),
    Estacion("SIN", "San Nicolás", Linea2, 25.7526552, -100.2980113),
    Estacion("ANA", "Anáhuac", Linea2, 25.7396433, -100.3027244),
    Estacion("UNI", "Universidad", Linea2, 25.7243261, -100.3082467),
    Estacion("NIH","Niños Héroes", Linea2, 25.7169554, -100.3108405),
    Estacion("REG", "Regina", Linea2, 25.7081815, -100.3139667, subterraneo=True),
    Estacion("GEA", "General Anaya", Linea2, 25.6968998, -100.3167862, subterraneo=True, ascensor=False, mecanicas=False),
    Estacion("CUA-L2", "Cuauhtémoc", Linea2, 25.6861734, -100.3167239, subterraneo=True),
    Estacion("ALA", "Alameda", Linea2, 25.6770074, -100.3181712, subterraneo=True, ascensor=False, mecanicas=False),
    Estacion("FUN", "Fundadores", Linea2, 25.6722598, -100.3187969, subterraneo=True, ascensor=False),
    Estacion("PAM", "Padre Mier", Linea2, 25.6686187, -100.3154985, subterraneo=True, ascensor=False),
    Estacion("GIZ-L2", "General I. Zaragoza", Linea2, 25.6677549, -100.3102203, subterraneo=True, ascensor=False)
]

NodosLinea3 = [
    Estacion("GIZ-L3", "General I. Zaragoza",Linea3, 25.6677549, -100.3102203, ascensor=False),
    Estacion("SLU", "Santa Lucía",Linea3, 25.6715281, -100.2985427),
    Estacion("COB", "Colonia Obrera",Linea3, 25.6767658, -100.2978841),
    Estacion("FUG-L3", "Félix U. Gómez",Linea3, 25.6840577, -100.2966937),
    Estacion("MET", "Metalúrgicos",Linea3, 25.6897793, -100.2959736),
    Estacion("CMO", "Colonia Moderna",Linea3, 25.7004749, -100.2925307),
    Estacion("ARC", "Adolfo Ruiz Cortines",Linea3, 25.7052240, -100.2871937),
    Estacion("LAN", "Los Ángeles",Linea3, 25.7087002, -100.2836520),
    Estacion("HME", "Hospital Metropolitano",Linea3, 25.7138350, -100.2734116)
]

Transbordos = [
    Conexion(NodosLinea1[11], NodosLinea2[8], "transbordo", 0, 3),
    Conexion(NodosLinea1[13], NodosLinea3[3], "transbordo", 0, 3),
    Conexion(NodosLinea2[12], NodosLinea3[0], "transbordo", 0, 4)
]

AristasLinea1 = [
  Conexion(NodosLinea1[0], NodosLinea1[1], "tramo", 1.437, 2.67),
  Conexion(NodosLinea1[1], NodosLinea1[2], "tramo", 1.009, 1.88),
  Conexion(NodosLinea1[2], NodosLinea1[3], "tramo", 1.360, 2.53),
  Conexion(NodosLinea1[3], NodosLinea1[4], "tramo", 1.133, 2.11),
  Conexion(NodosLinea1[4], NodosLinea1[5], "tramo", 0.824, 1.53),
  Conexion(NodosLinea1[5], NodosLinea1[6], "tramo", 1.145, 2.13),
  Conexion(NodosLinea1[6], NodosLinea1[7], "tramo", 0.823, 1.53),
  Conexion(NodosLinea1[7], NodosLinea1[8], "tramo", 0.776, 1.44),
  Conexion(NodosLinea1[8], NodosLinea1[9], "tramo", 1.209, 2.25),
  Conexion(NodosLinea1[9], NodosLinea1[10], "tramo", 0.949, 1.76),
  Conexion(NodosLinea1[10], NodosLinea1[11], "tramo", 0.770, 1.43),
  Conexion(NodosLinea1[11], NodosLinea1[12], "tramo", 1.076, 2.00),
  Conexion(NodosLinea1[12], NodosLinea1[13], "tramo", 0.994, 1.85),
  Conexion(NodosLinea1[13], NodosLinea1[14], "tramo", 0.896, 1.66),
  Conexion(NodosLinea1[14], NodosLinea1[15], "tramo", 0.884, 1.64),
  Conexion(NodosLinea1[15], NodosLinea1[16], "tramo", 1.620, 3.01),
  Conexion(NodosLinea1[16], NodosLinea1[17], "tramo", 1.222, 2.27),
  Conexion(NodosLinea1[17], NodosLinea1[18], "tramo", 0.702, 1.30)
]
AristasLinea2 = [
  Conexion(NodosLinea2[0], NodosLinea2[1], "tramo", 1.163, 2.05),
  Conexion(NodosLinea2[1], NodosLinea2[2], "tramo", 0.834, 1.47),
  Conexion(NodosLinea2[2],NodosLinea2[3], "tramo", 1.632, 2.88),
  Conexion(NodosLinea2[3], NodosLinea2[4], "tramo", 1.920, 3.39),
  Conexion(NodosLinea2[4], NodosLinea2[5], "tramo", 0.922, 1.63),
  Conexion(NodosLinea2[5], NodosLinea2[6], "tramo", 1.098, 1.94),
  Conexion(NodosLinea2[6], NodosLinea2[7], "tramo", 1.379, 2.43),
  Conexion(NodosLinea2[7], NodosLinea2[8], "tramo", 1.279, 2.26),
  Conexion(NodosLinea2[8], NodosLinea2[9], "tramo", 1.104, 1.95),
  Conexion(NodosLinea2[9], NodosLinea2[10], "tramo", 0.570, 1.01),
  Conexion(NodosLinea2[10], NodosLinea2[11], "tramo", 0.560, 0.99),
  Conexion(NodosLinea2[11], NodosLinea2[12], "tramo", 0.576, 1.02)
]
AristasLinea3 = [
  Conexion(NodosLinea3[0], NodosLinea3[1], "tramo", 1.336, 2.49),
  Conexion(NodosLinea3[1], NodosLinea3[2], "tramo", 0.630, 1.18),
  Conexion(NodosLinea3[2], NodosLinea3[3], "tramo", 0.881, 1.64),
  Conexion(NodosLinea3[3], NodosLinea3[4], "tramo", 0.688, 1.28),
  Conexion(NodosLinea3[4], NodosLinea3[5], "tramo", 1.331, 2.48),
  Conexion(NodosLinea3[5], NodosLinea3[6], "tramo", 0.808, 1.51),
  Conexion(NodosLinea3[6], NodosLinea3[7], "tramo", 0.564, 1.05),
  Conexion(NodosLinea3[7], NodosLinea3[8], "tramo", 1.262, 2.36)
]
