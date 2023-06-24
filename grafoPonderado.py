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

    def adicionar_aresta(self, no1, no2, peso):
        if no1 not in self.lista_adj:
            self.adicionar_no(no1)
        if no2 not in self.lista_adj:
            self.adicionar_no(no2)
        self.lista_adj[no1][no2] = peso
        self.num_arestas += 1

    def adicionar_nos(self, nos):
        for no in nos:
            self.adicionar_no(no)

    def adicionar_aresta_bidirecional(self, no1, no2, peso):
        self.adicionar_aresta(no1, no2, peso)
        self.adicionar_aresta(no2, no1, peso)

    def remover_no(self, no):
        for no2 in self.lista_adj:
            if no in self.lista_adj[no2]:
                self.lista_adj[no2].pop(no)
                self.num_arestas -= 1
        self.num_arestas -= len(self.lista_adj[no])
        self.num_nos -= 1
        self.lista_adj.pop(no)

    def remover_aresta(self, no1, no2):
        try:
          self.lista_adj[no1].pop(no2)
          self.num_arestas -= 1
        except KeyError as e:
            print(f"AVISO: Nó {e} não existe")
        except ValueError as e:
            print(f"AVISO: Aresta {no1} -> {no2} não existe")

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
    
    def ler_planilha_criar_aresta(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        for linha in planilha.iterrows():
            valor_idVotacao = linha['idVotacao']
            valor_nome = linha['deputado_nome']
            valor_voto = linha['voto']
            for i in self.lista_adj:
                pass
    
    def qntd_votacao(self, nome_planilha):
        planilha = pd.read_excel(nome_planilha)
        for i in self.lista_adj:
            qtdVotacoes = 0
            linhas_filtradas = planilha[planilha['deputado_nome'] == i]
            for linha in linhas_filtradas.iterrows():
                qtdVotacoes += 1
            with open("quantidadeVotacoes.txt", 'a') as arquivo:
                arquivo.write(f"{i} {qtdVotacoes} \n")
            

    def gerar_arquivo_qtd_votacoes_participadas(self, nome_planilha):
        self.qntd_votacao(nome_planilha)
        with open("quantidadeVotacoes.txt", 'w') as arquivo:
            arquivo.write('teste')

    def __str__(self) -> str:
        saida = ""
        for no in self.lista_adj:
            saida += f"{no} -> {self.lista_adj[no]}\n"
        return saida