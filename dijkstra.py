from grafo import GrafoMatrizAdjacencia

def dijkstra(grafo, s):
    distancia = {v: float('inf') for v in grafo.vertices}
    antecessor = {v: None for v in grafo.vertices}
    visitados = {v: False for v in grafo.vertices}
    distancia[s] = 0
    
    while True:
        u = None
        for vertice in grafo.vertices:
            if not visitados[vertice] and (u is None or distancia[vertice] < distancia[u]):
                u = vertice

        if u is None:
            # Todos os vértices foram visitados
            break
        
        visitados[u] = True
        if u is not None:  # Verifica se u não é None
            for v in grafo.vizinhos(u):
                if distancia[v] > distancia[u] + grafo.peso(u, v):
                    distancia[v] = distancia[u] + grafo.peso(u, v)
                    antecessor[v] = u

    return distancia, antecessor

def imprimir_resultados(distancias, antecessores):
    for destino, distancia in distancias.items():
        caminho = reconstruir_caminho(antecessores, destino)
        print(f"{destino}: {caminho}; d={distancia}")

def reconstruir_caminho(antecessores, destino):
    caminho = [str(destino)]
    antecessor = antecessores[destino]
    while antecessor is not None:
        caminho.insert(0, str(antecessor))
        antecessor = antecessores[antecessor]
    return ",".join(caminho)

grafo = GrafoMatrizAdjacencia()
nome_arquivo = input("Digite o nome do arquivo .net: ")
s = int(input("Digite o número do vértice de origem: "))
grafo.ler(nome_arquivo)
distancias, antecessores = dijkstra(grafo, s)
imprimir_resultados(distancias, antecessores)
