#contadores- Ruim, Excelente
excelente = 0
ruim = 0 

#pesquisa com 50 entrevistadores
for i in range(50):
    print(f"\nEntrevistado {i+1}")
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade:"))

    print("digite sua opinião sobre o atendimento:")
    print("1 - Excelente")
    print("2 - Bom")
    print("3 - Ruim")
    opinião = int(input("digite sua opinião: "))

    #verifica a opinião
    if opinião == 1:
        excelente += 1
    elif opinião == 3:
        ruim += 1

    #resultado final
    print("\nResultado da pesquisa:")
    print(f"Quantidade de respostas Excelente: {excelente}")
    print(f"Quantidade de respostas Ruim: {ruim}")


