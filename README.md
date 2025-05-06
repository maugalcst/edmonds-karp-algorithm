# Algoritmo de Edmonds–Karp para Flujo Máximo

Este programa en Python calcula el flujo máximo entre dos nodos en una red dirigida utilizando el algoritmo de Edmonds–Karp (una versión de Ford–Fulkerson que emplea BFS para encontrar caminos aumentantes).

La red se modela como un conjunto de "tuberías" (aristas) con un diámetro máximo (capacidad) por donde puede fluir agua (el flujo). El script guía al usuario paso a paso, explicando cada entrada con analogías de tuberías.

---

## Requisitos

- Python 3.6 o superior.
- Solo utiliza el módulo estándar `collections` (no requiere instalaciones adicionales).

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/maugalcst/edmonds-karp-algorithm.git
   cd edmonds-karp-algorithm
   ```
2. (Opcional) Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

## Uso del script

Ejecuta el programa directamente y sigue las indicaciones en la terminal:

```bash
python edmonds_karp.py
``` 

Verás mensajes como:

1. **Número de nodos**: te pedirá cuántas "válvulas" (nodos) hay en tu sistema de tuberías.
2. **Número de aristas**: cuántas tuberías hay conectando esas válvulas.
3. **Definición de cada tubería**: para cada tubería, ingresa el nodo de origen, el nodo de destino y la capacidad máxima (diámetro). Imagina que explicas de dónde a dónde va la tubería y cuánta agua puede pasar.
4. **Nodo fuente y sumidero**: indica la válvula de entrada (fuente) y salida (sumidero) entre las que quieres maximizar el flujo.

Tras la última entrada, el script calculará y mostrará en pantalla:

```
Flujo máximo de <fuente> a <sumidero>: <valor>
```

### Ejemplo...

Supongamos un sistema con 4 válvulas y 5 tuberías:

```
Número de válvulas (nodos): 4
Número de tuberías (aristas): 5
Definiendo tubería 1:
  Origen: 0
  Destino: 1
  Capacidad (máximo agua): 100
...                          # repite para las 5 tuberías
Fuente (válvula de entrada): 0
Sumidero (válvula de salida): 3
```

El resultado esperado será:

```
Flujo máximo de 0 a 3: 200
```

## Redirección desde archivo

Si prefieres usar un archivo de texto con las entradas en orden, puedes hacer:

```bash
python edmonds_karp.py < input.txt
```

donde `input.txt` contiene:
```
4 5
0 1 100
0 2 100
1 2 1
1 3 100
2 3 100
0 3
```
