from collections import deque

def bfs(residual, s, t, parent):
    """
    Busca un camino aumentante en 'residual' desde s hasta t.
    Devuelve True si existe, y rellena parent[] para reconstruir la ruta.
    """
    visited = [False] * len(residual)
    queue = deque([s])
    visited[s] = True
    parent[s] = -1

    while queue:
        u = queue.popleft()
        for v, cap in enumerate(residual[u]):
            if not visited[v] and cap > 0:
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
                queue.append(v)
    return False

def edmonds_karp(capacity, s, t):
    """
    Calcula el flujo máximo de s a t usando Edmonds–Karp.
    'capacity' es una matriz n×n de capacidades.
    Devuelve el valor del flujo máximo.
    """
    n = len(capacity)
    # Copiamos capacity en residual para no modificar la original
    residual = [row[:] for row in capacity]
    parent = [-1] * n
    max_flow = 0

    # Mientras haya un camino aumentante
    while bfs(residual, s, t, parent):
        # Encontrar la capacidad mínima a lo largo del camino hallado
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Actualizar la red residual: restar en la dirección del camino
        # y sumar en la dirección opuesta (arista inversa)
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

if __name__ == "__main__":
    # Lectura de datos
    # Formato:
    # n m
    # u1 v1 c1
    # ...
    # um vm cm
    # s t
    n, m = map(int, input().split())
    # Inicializa matriz de capacidades n×n con ceros
    capacity = [[0]*n for _ in range(n)]

    for _ in range(m):
        u, v, c = map(int, input().split())
        capacity[u][v] = c

    s, t = map(int, input().split())

    result = edmonds_karp(capacity, s, t)
    print("Flujo máximo de {} a {}: {}".format(s, t, result))
