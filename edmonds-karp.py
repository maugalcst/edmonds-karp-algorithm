from collections import deque

# Función para buscar un camino aumentante en la red residual
def bfs(residual, s, t, parent):
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

# Algoritmo Edmonds–Karp para flujo máximo
def edmonds_karp(capacity, s, t):
    n = len(capacity)
    residual = [row[:] for row in capacity]
    parent = [-1] * n
    max_flow = 0

    while bfs(residual, s, t, parent):
        # Encuentra el caudal mínimo (cuello de botella) en este camino
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Actualiza la red residual
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

if __name__ == "__main__":
    print("\n=== Cálculo de Flujo Máximo (Edmonds–Karp) ===")
    print("se usa la analogía como un conjunto de tuberías por donde fluye agua.")
    print("Cada tubería (arista) tiene un diámetro máximo (capacidad) que no puedes superar.\n")

    # Entrada de nodos y aristas
    entrada = input("Introduce el número de nodos y aristas separados por espacio (ej. '4 5'): ")
    n, m = map(int, entrada.split())

    # Inicializa matriz de capacidades
    capacity = [[0]*n for _ in range(n)]

    print(f"\nAhora define tus tuberías. Vas a introducir {m} tuberías.")
    print("Para cada tubería, ingresa: nodo_origen nodo_destino capacidad")
    for i in range(m):
        linea = input(f"Tubería {i+1}/{m}: ")
        u, v, c = map(int, linea.split())
        capacity[u][v] = c

    # Nodo fuente y sumidero
    st = input("\nIntroduce el nodo fuente y el nodo sumidero separados por espacio (ej. '0 3'): ")
    s, t = map(int, st.split())

    # Cálculo y resultado
    resultado = edmonds_karp(capacity, s, t)
    print(f"\nEl flujo máximo desde el nodo {s} hasta el nodo {t} es: {resultado}\n")
