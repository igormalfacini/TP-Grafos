from grafoPonderado import GrafoPonderado

g = GrafoPonderado()
nome_planilha = input("Informe o arquivo de votações: ")
arquivo_votacoes = g.gerar_arquivo_qtd_votacoes_participadas(nome_planilha)
arquivo_grafo = g.gerar_arquivo_grafo(nome_planilha)
print(f"Processando...\nO grafo foi escrito nos arquivos:\n- {arquivo_grafo}\n- {arquivo_votacoes}")