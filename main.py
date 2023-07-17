from grafoPonderado import GrafoPonderado

g = GrafoPonderado()
nome_planilha = "votacoesVotos-2023.xlsx"
#input("Informe o arquivo de votações: ")
g.ler_planilha_cria_nos(nome_planilha)
g.ler_planilha_criar_aresta(nome_planilha)
g.gerar_arquivo_qtd_votacoes_participadas(nome_planilha)
g.gerar_arquivo_grafo("grafovotacao2023.txt")
print(f"Processando...\nO grafo foi escrito nos arquivos:\n- votacaoVotos-2023-graph.txt\n- votacaoVotos-2023-deputados.txt")