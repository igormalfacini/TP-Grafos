import pandas as pd
import warnings

class GrafoPonderado:
    
    def __init__(self) -> None:
        self.lista_adj = {}
        self.num_nos = 0
        self.num_arestas = 0

    def adicionar_no(self, no):
        warnings.filterwarnings("ignore", category=UserWarning)
        if no in self.lista_adj:
            return
        
        self.lista_adj[no] = {}
        self.num_nos += 1

    def adicionar_no_adj(self, no_pai, no_filho):
        if no_filho not in self.lista_adj[no_pai]:
            self.lista_adj[no_pai][no_filho] = 1
            self.num_arestas += 1
            return

        self.lista_adj[no_pai][no_filho] += 1

    def adicionar_aresta(self, no1, no2):
        if no1 not in self.lista_adj:
            self.adicionar_no(no1)

        self.adicionar_no_adj(no1, no2)

    def ler_planilha_cria_nos(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)

        for indice, linha in planilha.iterrows():
            valor_nome = linha['deputado_nome']     
            self.adicionar_no(valor_nome)  

    def ler_planilha_criar_aresta(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        arestas = {}

        for indice, linha in planilha.iterrows():
            chave = (linha['idVotacao'], linha['voto'])
            deputado_nome = linha['deputado_nome']

            if chave not in arestas:
                arestas[chave] = [deputado_nome]
            else:
                for deputado in arestas[chave]:
                    self.adicionar_aresta(deputado, deputado_nome)
                arestas[chave].append(deputado_nome)
    
    def gerar_arquivo_grafo(self, nome_planilha):
        self.ler_planilha_criar_aresta(nome_planilha)
        nome_resultado = nome_planilha.split(".")[0] + '-graph.txt'

        with open(nome_resultado, 'w') as arquivo:
            arquivo.write(f"{self.num_nos} {self.num_arestas}\n")
            for no in self.lista_adj:
                for adj in self.lista_adj[no]:
                    arquivo.write(f"{no} {adj} {self.lista_adj[no][adj]}\n")
        return nome_resultado
                    
    def gerar_arquivo_qtd_votacoes_participadas(self, nome_planilha):
        self.ler_planilha_cria_nos(nome_planilha)
        planilha = pd.read_excel(nome_planilha)
        nome_resultado = nome_planilha.split(".")[0] + '-deputados.txt'

        for i in self.lista_adj:
            qtdVotacoes = 0
            linhas_filtradas = planilha[planilha['deputado_nome'] == i]
            for linha in linhas_filtradas.iterrows():
                qtdVotacoes += 1
            with open(nome_resultado, 'a') as arquivo:
                arquivo.write(f"{i} {qtdVotacoes} \n")
        return nome_resultado

    def __str__(self) -> str:
        saida = ""
        for no in self.lista_adj:
            saida += f"{no} -> {self.lista_adj[no]}\n"
        return saida