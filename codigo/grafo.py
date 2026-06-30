import csv

class GrafoCoautoria:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        """adiciona um pesquisador ao grafo se ele ainda não existir"""
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, u, v):
        """cria uma conexão de co-autoria entre o pesquisador u e v"""
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        
        if v not in self.adjacencia[u]:
            self.adjacencia[u].append(v)
        if u not in self.adjacencia[v]:
            self.adjacencia[v].append(u)

    def carregar_do_csv(self, caminho_arquivo):
        """le o arquivo CSV de arestas e monta o grafo na memoria"""
        with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                u = linha['Source']
                v = linha['Target']
                self.adicionar_aresta(u, v)

    def obter_vizinhos(self, vertice):
        """retorna a lista de co-autores de um pesquisador"""
        return self.adjacencia.get(vertice, [])

    def obter_todos_vertices(self):
        """retorna todos os pesquisadores da rede"""
        return list(self.adjacencia.keys())

    def total_vertices(self):
        """retorna a quantidade total de vertices"""
        return len(self.adjacencia)

    def total_arestas(self):
        """retorna a quantidade total de arestas"""
        soma_graus = sum(len(vizinhos) for vizinhos in self.adjacencia.values())
        return soma_graus // 2