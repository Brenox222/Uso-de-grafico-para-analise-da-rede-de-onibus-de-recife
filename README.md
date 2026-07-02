# Sistema de Análise de Rede de Coautoria (UFPE)

Este projeto foi desenvolvido como parte dos requisitos avaliativos da disciplina de Algoritmos e Estruturas de Dados / Teoria dos Grafos na UFPE. O sistema realiza a leitura, modelagem e análise estrutural de uma rede de coautoria científica de professores/pesquisadores universitários baseando-se no dataset **D4**.

## Funcionalidades Realizadas

O sistema cumpre integralmente os requisitos solicitados no regulamento:
- **Estatísticas Básicas (Requisito 3.1):** Contagem de vértices (pesquisadores), arestas (colaborações) e cálculo do Grau Médio da rede.
- **Busca em Largura - BFS (Requisito 3.2):** Rastreamento da ordem de visitação e função de reconstrução de caminho mínimo para determinar a menor distância entre dois nós de forma ótima em grafos não valorados.
- **Busca em Profundidade - DFS (Requisito 3.2):** Abordagem recursiva elegante para mapear a ordem de visitação, metadados dos nós (Tempos de Descoberta $d$ e Finalização $f$), além de segregar as arestas pertencentes à Árvore de Busca e as Arestas de Retorno.
- **Componentes Conexas:** Identificação quantitativa e qualitativa das subredes/ilhas isoladas no grafo.
- **Resolução das Perguntas Obrigatórias (Requisito 4):**
  - Identificação do *Hub* da rede (Nó de maior grau).
  - Verificação e comprovação matemática da existência de Ciclos via DFS.
  - Pergunta Inédita (Cálculo do Diâmetro da rede utilizando caminhos mínimos).

---

## Estrutura do Projeto

```text
Trabalho Trajno/
│
├── data/
│   └── D4_coautoria.csv       # Dataset original de parcerias da UFPE
│
├── codigo/
│   ├── __init__.py
│   ├── grafo.py               # Estrutura do Grafo (Lista de Adjacência)
│   ├── bfs.py                 # Algoritmo de Busca em Largura e Caminho Mínimo
│   ├── dfs.py                 # Algoritmo de Busca em Profundidade Recursiva
│   ├── componentes.py         # Identificação de Componentes Conexas
│   └── caminhos.py            # Implementação do algoritmo de Dijkstra
│
├── main.py                    # Script principal unificado e relatório no console
└── README.md                  # Documentação do projeto
