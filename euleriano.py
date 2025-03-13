from grafo import GrafoMatrizAdjacencia
import random


def buscarSubcicloEuleriano(grafo, v, Ce):
  Ciclo = [v]
  t = v
  while True:
    nao_visitados = [u for u in grafo.vizinhos(v) if not Ce.get((v, u), True)]
    
    if not nao_visitados:
      return (False, None)
    
    u = nao_visitados[0]
    Ce[(v, u)] = True
    Ce[(u, v)] = True 
    v = u
    Ciclo.append(v)
    
    if v == t:
      break
  vertices_com_arestas_nao_visitadas = []
  for u in Ciclo:
    if any(not Ce.get((u, w), True) for w in grafo.vizinhos(u)):
      vertices_com_arestas_nao_visitadas.append(u)

  for x in vertices_com_arestas_nao_visitadas:
    r, Ciclo_prime = buscarSubcicloEuleriano(grafo, x, Ce)
    if not r:
      return False, None
    index_x = Ciclo.index(x)
    Ciclo = Ciclo[:index_x] + Ciclo_prime + Ciclo[index_x + 1:]

  return True, Ciclo
    
def Hierholzer(grafo):
    Ce = {}
    arestas = grafo.getArestas()
    for aresta in arestas:
      Ce[aresta] = False
    v_inicial = list(grafo.vertices)[random.randint(0, grafo.qtdVertices() - 1)]
    r, ciclo = buscarSubcicloEuleriano(grafo, v_inicial, Ce)
    if r == False:
      return (False, None)  
    for aresta in arestas:
      if(Ce[aresta] == False):
        return (False, None)
    return (True, ciclo)  

grafo = GrafoMatrizAdjacencia()

arquivo = input("digite o grafo de ciclo euleriano: ") 
grafo.ler(arquivo)

tem_ciclo, ciclo = Hierholzer(grafo)

if tem_ciclo:
  print(1)
  print(",".join(map(str, ciclo)))
else:
  print(0)
