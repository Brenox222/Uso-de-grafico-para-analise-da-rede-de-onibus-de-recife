import os
from codigo.grafo import GrafoCoautoria
from codigo.bfs import bfs, encontrar_menor_caminho_bfs  # Puxando a nova função de caminho
from codigo.dfs import dfs_completa
from codigo.componentes import encontrar_componentes_conexas
from codigo.caminhos import dijkstra

def desenhar_arvore_dfs(mapa_pais, no_atual, nivel=0):
    print("  " * nivel + f"└── {no_atual}")
    filhos = [filho for filho, pai in mapa_pais.items() if pai == no_atual]
    for filho in filhos:
        desenhar_arvore_dfs(mapa_pais, filho, nivel + 1)

def executar_projeto():
    print("=" * 60)
    print("      SISTEMA DE ANÁLISE DE REDE DE COAUTORIA - UFPE      ")
    print("=" * 60)

    g = GrafoCoautoria()
    caminho = os.path.join('data', 'D4_coautoria.csv')
    
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo {caminho} não encontrado!")
        return
        
    g.carregar_do_csv(caminho)

    print("\n--- [REQUISITO 3.1 & PERGUNTA 3] Métricas de Grau ---")
    print(f"A rede possui {g.total_vertices()} pesquisadores no total.")
    print(f"A rede possui {g.total_arestas()} conexões (arestas) no total.")
    print(f"Em média, cada pesquisador colabora com {g.calcular_grau_medio():.2f} outros colegas.")

    prof, grau = g.obter_no_maior_grau()
    print(f"-> Resposta da Pergunta 3: O hub da rede é o {prof} com {grau} conexões.")

    todos_pesquisadores = g.obter_todos_vertices()

    print("\n--- [REQUISITO 3.2 & PERGUNTA 2] Menor Caminho via BFS ---")
    professor_exemplo = "Prof_01"
    professor_destino = "Prof_19"
    
    alcance = bfs(g, professor_exemplo)
    caminho_bfs = encontrar_menor_caminho_bfs(g, professor_exemplo, professor_destino)
    
    print(f"O pesquisador {professor_exemplo} consegue alcançar {len(alcance)} colegas na rede via BFS.")
    print(f"-> Resposta da Pergunta 2 (Menor Caminho):")
    print(f"   Caminho exato: {' -> '.join(caminho_bfs)}")
    print(f"   Distância (número de arestas): {len(caminho_bfs) - 1}")
    print(f"   Justificativa: Como o grafo de coautoria D4 não possui pesos atribuídos às arestas,")
    print(f"   a Busca em Largura (BFS) é o algoritmo ótimo e correto para determinar a menor distância,")
    print(f"   garantindo a descoberta do caminho mínimo ao expandir a busca uniformemente por níveis.")

    print("\n--- [REQUISITO 3.2 & PERGUNTAS 4 e 5] Análise com DFS ---")
    resultado_dfs = dfs_completa(g, professor_exemplo)
    
    print(f"Ordem de visitação da DFS: {resultado_dfs['ordem']}\n")
    
    print("-> Resposta da Pergunta 4 (Estrutura Visual da Árvore de Busca DFS):")
    desenhar_arvore_dfs(resultado_dfs['mapa_pais'], professor_exemplo)
    
    print(f"\nArestas Oficiais que Compõem a Árvore ({len(resultado_dfs['arestas_arvore'])}):")
    print(f"   {resultado_dfs['arestas_arvore']}")
    
    print("\n-> Metadados dos Nós (Tempos de Descoberta 'd' e Finalização 'f'):")
    for no in sorted(resultado_dfs['descoberta'].keys()):
        d = resultado_dfs['descoberta'][no]
        f = resultado_dfs['finalizacao'][no]
        print(f"   - {no}: d={d} | f={f}")
        
    print(f"\nArestas de Retorno Encontradas ({len(resultado_dfs['arestas_retorno'])}):")
    print(f"   {resultado_dfs['arestas_retorno']}")
    
    print("\n-> Resposta da Pergunta 5 (Ciclos):")
    if len(resultado_dfs['arestas_retorno']) > 0:
        print("   O grafo POSSUI ciclos, determinados pela presença das arestas de retorno listadas acima.")
    else:
        print("   O grafo NÃO possui ciclos.")

    print("\n--- Análise de Componentes Conexas ---")
    grupos = encontrar_componentes_conexas(g)
    print(f"A rede está dividida em {len(grupos)} grupos distintos (ilhas).")
    for i, grupo in enumerate(grupos):
        print(f"Grupo {i+1}: {len(grupo)} pesquisadores.")

    print("\n--- [PERGUNTA 6 - ORIGINAL] Diâmetro da Rede ---")
    maior_distancia = 0
    par_distante = ("", "")
    for i in range(len(todos_pesquisadores)):
        for j in range(i + 1, len(todos_pesquisadores)):
            _, custo = dijkstra(g, todos_pesquisadores[i], todos_pesquisadores[j])
            if custo != float('inf') and custo > maior_distancia:
                maior_distancia = custo
                par_distante = (todos_pesquisadores[i], todos_pesquisadores[j])
                
    print(f"Qual o diâmetro da rede? Resposta: {maior_distancia}.")
    print(f"A maior distância entre dois cientistas quaisquer é de {maior_distancia} passos (ex: entre {par_distante[0]} e {par_distante[1]}).")


    print(f"\n{'='*20} Conclusão da Análise {'='*20}")
    if len(grupos) == 1:
        print("Conclusão: A rede de coautoria é um componente único e coeso.")
    else:
        print(f"Conclusão: A rede apresenta uma estrutura fragmentada em {len(grupos)} grupos.")

    print(f"O pesquisador {prof} atua como a principal fonte de informação, possuindo o maior grau.")
    
    if len(alcance) == g.total_vertices():
        print("Isso demonstra uma alta centralidade e poder de influência em toda a rede, onde a partir de um único nó é possível alcançar 100% dos pesquisadores.")
    print("=" * 60)

if __name__ == "__main__":
    executar_projeto()
