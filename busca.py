# from grafo import GrafoMatrizAdjacencia as Grafo
from grafo import Grafo
from grafo import GrafoMatrizAdjacencia as GrafoMatriz
from collections import deque, defaultdict

def busca_em_largura(grafo: Grafo, s: int) -> str:
    resultado = ''
    # c_visitados = set() # No set = true, fora = false
    c_visitados = [False for _ in range(grafo.qtdVertices()+1)]
    d_niveis = defaultdict(list)

    # c_visitados.add(s)
    c_visitados[s] = True
    fila = deque()
    fila.append((0, s)) # (nivel, vertice)

    while fila:
        nivel, vertice = fila.popleft()
        d_niveis[nivel].append(vertice)

        for vizinho in grafo.vizinhos(vertice):
            # if not vizinho in c_visitados:
            #     c_visitados.add(vizinho)
            if not c_visitados[vizinho]:
                c_visitados[vizinho] = True
                fila.append((nivel+1, vizinho))
    

    # represenção em string
    max_nivel = max(d_niveis.keys())
    for nivel in range(max_nivel+1):
        resultado += f'{nivel}: {",".join(grafo.rotulo(v) for v in sorted(d_niveis[nivel]))}\n'

    return resultado

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 busca.py <arquivo.net>")
        sys.exit(1)

    grafo = Grafo()
    grafo.ler(sys.argv[1])

    res_graf = busca_em_largura(grafo, 1)

    grafo_matriz = GrafoMatriz()
    grafo_matriz.ler(sys.argv[1])

    res_graf_matriz = busca_em_largura(grafo_matriz, 1)

    print(res_graf)
    print(res_graf_matriz)
    print(res_graf == res_graf_matriz)

