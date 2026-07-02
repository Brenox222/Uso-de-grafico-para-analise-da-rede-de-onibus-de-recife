def dfs_completa(grafo, vertice_inicial):
    tempos_descoberta = {}
    tempos_finalizacao = {}
    arestas_retorno = []
    ordem_visitacao = []
    
    estados = {v: 0 for v in grafo.obter_todos_vertices()}
    pais = {v: None for v in grafo.obter_todos_vertices()}
    
    tempo = [0] 

    def dfs_visitar(u):
        tempo[0] += 1
        tempos_descoberta[u] = tempo[0]
        estados[u] = 1 
        ordem_visitacao.append(u)
        
        for vizinho in grafo.obter_vizinhos(u):
            if estados[vizinho] == 0:
                pais[vizinho] = u
                dfs_visitar(vizinho)  
                
            elif estados[vizinho] == 1 and vizinho != pais[u]:
                if (vizinho, u) not in arestas_retorno:
                    arestas_retorno.append((u, vizinho))
                    
        estados[u] = 2  
        tempo[0] += 1
        tempos_finalizacao[u] = tempo[0]

    dfs_visitar(vertice_inicial)
    
    return {
        "ordem": ordem_visitacao,
        "descoberta": tempos_descoberta,
        "finalizacao": tempos_finalizacao,
        "arestas_retorno": arestas_retorno
    }
