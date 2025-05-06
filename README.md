# Algoritmo de Edmonds–Karp para Flujo Máximo

Este programa implementa el algoritmo de Edmonds–Karp (versión de Ford–Fulkerson con búsqueda en anchura) para calcular el flujo máximo en una red dirigida. Está escrito en Python y es fácil de usar en cualquier entorno que tenga instalado Python 3.6 o superior.

---

## Requisitos

* Python 3.6 o superior
* Módulo estándar `collections` (no requiere instalación adicional)

## Instalación

1. Clona o descarga el repositorio que contiene el archivo `edmonds_karp.py`.
2. Asegúrate de tener instalado Python:

   ```bash
   python --version
   ```

## Uso

Ejecuta el script desde la terminal y proporciona los datos de la red mediante entrada estándar o redireccionando un archivo:

```bash
python edmonds_karp.py < input.txt
```

### Formato de entrada

La entrada debe ajustarse al siguiente esquema:

```
n m
u1 v1 c1
u2 v2 c2
...
um vm cm
s t
```

* `n`: número de nodos (etiquetados de `0` a `n-1`).
* `m`: número de aristas dirigidas.
* Cada línea `ui vi ci` define una arista de `ui` a `vi` con capacidad `ci`.
* Finalmente, `s` es el nodo origen y `t` el nodo sumidero.

### Ejemplo de `input.txt`

```
4 5
0 1 100
0 2 100
1 2 1
1 3 100
2 3 100
0 3
```

Al ejecutar:

```bash
python edmonds_karp.py < input.txt
```

La salida será:

```
Flujo máximo de 0 a 3: 200
```

## Descripción de las funciones principales

* `bfs(residual, s, t, parent)`: realiza una búsqueda en anchura en la red residual para encontrar un camino aumentante desde `s` hasta `t`. Rellena el array `parent` para reconstruir la ruta.
* `edmonds_karp(capacity, s, t)`: itera llamando a `bfs`, actualiza la red residual y acumula el flujo hasta que no existan más caminos aumentantes.
