from codigo.grafo import GrafoCoautoria
from codigo.bfs import bfs
from codigo.componentes import encontrar_componentes_conexas
from codigo.dfs import dfs
import os

##parte de grafos

# 1. Criar o objeto grafo
g = GrafoCoautoria()

# 2. Carregar os dados 
caminho = os.path.join('data', 'D4_coautoria.csv')
g.carregar_do_csv(caminho)

# 3. prints das métricas Grados
print(f"A rede possui {g.total_vertices()} pesquisadores no total.")
print(f"Em média, cada pesquisador colabora com {g.calcular_grau_medio():.2f} outros colegas.")

prof, grau = g.obter_no_maior_grau()
print(f"O professor com maior rede de distribuição de informações é {prof} com {grau} conexões.")

# Lista todos os pesquisadores disponíveis
todos_pesquisadores = g.obter_todos_vertices()

print("\n--- Lista de Pesquisadores Disponíveis ---")
for i, nome in enumerate(todos_pesquisadores):
    print(f"{i}: {nome}")

## analise com bfs
professor_exemplo = todos_pesquisadores[0]
alcance = bfs(g, professor_exemplo)

print(f"O pesquisador {professor_exemplo} consegue alcançar {len(alcance)} colegas na rede.")

## analise com componentes

grupos = encontrar_componentes_conexas(g)
print(f"A rede está dividida em {len(grupos)} grupos distintos (ilhas).")
# imprimir o tamanho de cada grupo (para ver se há uma comunidade gigante e várias pequenas)
for i, grupo in enumerate(grupos):
    print(f"Grupo {i+1}: {len(grupo)} pesquisadores.")

    ## analise Dfs
    print(f"Análise de DFS")

    professor_exemplo, _ = g.obter_no_maior_grau()
    exploracao = dfs(g, professor_exemplo)

    print(f"Ao realizar uma busca em profundidade a partir da rede ({professor_exemplo}):")
print(f"O algoritmo percorreu uma sequência de {len(exploracao)} pesquisadores.")

## conclusão da analise
print(f"\n--- Conclusão da Análise ---")

if len(grupos) == 1:
    print("Conclusão: A rede de coautoria é um componente único e coeso.")
else:
    print(f"Conclusão: A rede apresenta uma estrutura fragmentada em {len(grupos)} grupos.")

print(f"O pesquisador {prof} atua como o principal fonte de informação, alcançando {len(alcance)} pesquisadores.")

if len(alcance) == g.total_vertices():
    print("Isso demonstra uma alta centralidade e poder de influência em toda a rede.")