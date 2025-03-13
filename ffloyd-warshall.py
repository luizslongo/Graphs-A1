from grafo import Grafo
from grafo import GrafoMatrizAdjacencia as GrafoMatriz

def floyd_warshall(grafo: Grafo) -> list:
    # Retorna matriz de menor distancia 

    # Inicializa matriz de distancias com peso das arestas
    D_matriz = [[grafo.peso(u, v) for v in range(grafo.qtdVertices()+1)] for u in range(grafo.qtdVertices()+1)]

    # Inicializa diagonal principal com 0 (distancia de um vertice para ele mesmo)
    for i in range(grafo.qtdVertices()+1):
        D_matriz[i][i] = 0

    # Inicializa matriz de predecessores
    PI_matriz = [[None for _ in range(grafo.qtdVertices()+1)] for _ in range(grafo.qtdVertices()+1)]
    
    # Inicializa matriz de predecessores com os vertices
    for i in range(grafo.qtdVertices()+1):
        for j in range(grafo.qtdVertices()+1):
            if D_matriz[i][j] != float('inf'):
                PI_matriz[i][j] = i

    # Executa o algoritmo
    for k in range(grafo.qtdVertices()+1):
        for i in range(grafo.qtdVertices()+1):
            for j in range(grafo.qtdVertices()+1):
                # if i == 7 and j == 8:
                #     print(f'{D_matriz[i][j]} > {D_matriz[i][k]} + {D_matriz[k][j]}')
                if (D_matriz[i][j] > (D_matriz[i][k] + D_matriz[k][j]) and (D_matriz[k][j]!=float('inf') and D_matriz[i][k] != float('inf'))):
                    D_matriz[i][j] = D_matriz[i][k] + D_matriz[k][j]
                    PI_matriz[i][j] = k

    return D_matriz, PI_matriz

def print_shortest_path(PI_matriz: list, u: int, v: int) -> None:
    # Imprime caminho minimo entre dois vertices
    if u == v:
        print(u)
    else:
        if PI_matriz[u][v] == None:
            print("Caminho inexistente de u para v")
        else:
            print_shortest_path(PI_matriz, u, PI_matriz[u][v])
            print(v)

if __name__ == "__main__":
    grafo = Grafo()
    grafo.ler("instancias/caminho_minimo/fln_pequena.net")

    d, pi = floyd_warshall(grafo)

    # print_shortest_path(pi, 5, 1)
    
    for verticex in sorted(list(grafo.vertices)):
        print(str(verticex) + ': ' + ','.join(str(d[verticex][y]) for y in sorted(grafo.vertices)))

    print('---------------------------')

    grafo = GrafoMatriz()
    grafo.ler("instancias/caminho_minimo/fln_pequena.net")

    d, pi = floyd_warshall(grafo)
    
    for verticex in sorted(list(grafo.vertices)):
        print(str(verticex) + ': ' + ','.join(str(d[verticex][y]) for y in sorted(grafo.vertices)))


