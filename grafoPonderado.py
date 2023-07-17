import pandas as pd

class GrafoPonderado:
    
    def __init__(self) -> None:
        self.lista_adj = {}
        self.num_nos = 0
        self.num_arestas = 0

    def adicionar_no(self, no):
        if no in self.lista_adj:
            # print(f"AVISO: Nó {no} já existe!")
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

    def ler_arquivo(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        i = 0
        for linha in arquivo:
            i += 1
            if i == 1:
                continue
            conteudo = linha.strip().split(" ")
            u = conteudo[0]
            v = conteudo[1]
            w = int(conteudo[2])
            self.adicionar_aresta(u, v, w)
        arquivo.close()

    def ler_planilha_cria_nos(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        for indice, linha in planilha.iterrows():
            valor_nome = linha['deputado_nome']     
            self.adicionar_no(valor_nome)  
    
    def linha_comparator(self, linha1, linha2):
        return (linha1['idVotacao'] == linha2['idVotacao'] 
                and linha1['voto'] == linha2['voto'] 
                and linha1['deputado_nome'] == linha2['deputado_nome'] 
                and linha1['deputado_id'] == linha2['deputado_id'])
    
    def ler_planilha_criar_aresta(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        for indice1, linha1 in planilha.iterrows():
            for indice2, linha2 in planilha.iterrows():
                if(self.linha_comparator(linha1, linha2)):
                    continue
                if(linha1['idVotacao'] == linha2['idVotacao']
                   and linha1['voto'] == linha2['voto']):
                    self.adicionar_aresta(linha1['deputado_nome'], linha2['deputado_nome'])
    
    def gerar_arquivo_grafo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"{self.num_nos} {round(self.num_arestas/2)}\n")
            nos_gravados = {}
            for no in self.lista_adj:
                for adj in self.lista_adj[no]:
                    if adj in nos_gravados and no in nos_gravados[adj]:
                        continue
                    arquivo.write(f"{no} {adj} {self.lista_adj[no][adj]}\n")
                    
                    if(no not in nos_gravados):
                        nos_gravados[no] = {}
                    nos_gravados[no][adj] = True
    
    def gerar_arquivo_qtd_votacoes_participadas(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        for i in self.lista_adj:
            qtdVotacoes = 0
            linhas_filtradas = planilha[planilha['deputado_nome'] == i]
            for linha in linhas_filtradas.iterrows():
                qtdVotacoes += 1
            with open("votacaoVotos-2023-deputados.txt", 'a') as arquivo:
                arquivo.write(f"{i} {qtdVotacoes} \n")

    def __str__(self) -> str:
        saida = ""
        for no in self.lista_adj:
            saida += f"{no} -> {self.lista_adj[no]}\n"
        return saida