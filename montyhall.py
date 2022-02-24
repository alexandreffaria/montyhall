import random

vitoriasCarmem = []
vitoriasMeulindo = []
simulacoes = 10000000



for _ in range(simulacoes):
    portas = [1,2,3]
    premio = random.randint(1,3)
    carmem = random.randint(1,3)
    meulindo = carmem
    
    if carmem == premio:
        vitoriasCarmem.append(carmem)
    
    if meulindo == premio:
        pass
    else:
        vitoriasMeulindo.append(meulindo)
    

        

percentualCarmem = (len(vitoriasCarmem)/simulacoes) * 100
percentualMeulindo = (len(vitoriasMeulindo)/simulacoes) * 100

simulacoesFormatado = "{:,}".format(simulacoes)

print(f"Simulações realizadas: {simulacoesFormatado}")
print(f"Percentual Carmem: {percentualCarmem}%")
print(f"Percentual MeuLindo: {percentualMeulindo}%")
