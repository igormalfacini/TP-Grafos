from grafoPonderado import GrafoPonderado

g = GrafoPonderado()
# g.ler_planilha("votacoesVotos-Teste.xlsx")
g.ler_planilha_cria_nos("votacoesVotos-Teste.xlsx")
g.qntd_votacao("votacoesVotos-Teste.xlsx")

# g.ler_planilha_cria_nos("votacoesVotos-2023.xlsx")
# g.qntd_votacao("votacoesVotos-2023.xlsx")

# print(g)