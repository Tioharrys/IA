from collections import defaultdict

def construir_grafo(conexiones):
    grafo = defaultdict(list)
    for a, b, distancia, tiempo in conexiones:
        grafo[a].append((b, distancia, tiempo))
        grafo[b].append((a, distancia, tiempo))
    return grafo

Linea1={("Talleres"),
        ("San Bernabé"),
        ( "Unidad Modelo"),
        ("Aztlán"),
        ("Penitenciaría"),
        ("Alfonso Reyes"),
        ("Mitras"),
        ("Simón Bolívar"),
        ("Hospital"),
        ("Edison"),
        ("Central"),
        ("Cuauhtémoc"),
        ("Del Golfo"),
        ("Félix U. Gómez"),
        ("Parque Fundidora"),
        ("Y Griega"),
        ("Eloy Cavazos"),
        ("Lerdo de Tejada"),
        ("Exposición (Terminal)")}

Linea2={("Sendero"),
        ("Tapia"),
        ("San Nicolás"),
        ("Anáhuac"),
        ("Universidad"),
        ("Niños Héroes"),
        ("Regina"),
        ("General Anaya"),
        ("Cuauhtémoc"),
        ("Alameda"),
        ("Fundadores"),
        ("Padre Mier"),
        ("General I. Zaragoza")}

Linea3={ ("General I. Zaragoza"),
        ("Santa Lucía"),
        ("Colonia Obrera"),
        ("Félix U. Gómez"),
        ("Metalúrgicos"),
        ("Colonia Moderna"),
        ("Adolfo Ruiz Cortines"),
        ("Los Ángeles"),
        ("Hospital Metropolitano")}
