from collections import deque

def bfs(grafo, vertice_inicial):
    visitados = set()
    fila = deque([vertice_inicial])
    ordem_visitacao = []
    
    visitados.add(vertice_inicial)
    
    while fila:
        vertice_atual = fila.popleft()
        ordem_visitacao.append(vertice_atual)
        
        for vizinho in grafo.obter_vizinhos(vertice_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                
    return ordem_visitacao

def encontrar_menor_caminho_bfs(grafo, inicio, fim):
    visitados = set([inicio])
    fila = deque([inicio])
    pais = {v: None for v in grafo.obter_todos_vertices()}
    
    while fila:
        atual = fila.popleft()
        if atual == fim:
            break
            
        for vizinho in grafo.obter_vizinhos(atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pais[vizinho] = atual
                fila.append(vizinho)
                
    caminho = []
    atual = fim
    if pais[fim] is not None or fim == inicio:
        while atual is not None:
            caminho.insert(0, atual)
            atual = pais[atual]
        return caminho
    return []
