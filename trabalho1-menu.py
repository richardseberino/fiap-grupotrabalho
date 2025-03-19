
continua = True
# altura e largura
area = [0,0]
cultura = ""
areaTotal = 0
areaUtil = 0
insumos = 0
densidade = 0
insumo_m2 = 0

while continua:
    print("Menu de opções:\n")

    print("1 - Informar os dados para calculo")
    print("2 - Atualizar os daados")
    print("3 - Excluir os dados")
    print("4 - Calcular")
    print("5 - Exibit resultado")
    print("\n\n0 - Sair")

    opcao = int(input("Escolha a opção desejada: "))

    if opcao == 0:
        continua = False
    elif opcao == 1:
        print ("Qual o tipo de Cultura?\n1 - Café\n2 - Milho")
        volta = True
        while volta:
            c = int(input("Escolha a opção: "))
            if c==1:
                cultura = "Café"
                volta = False
            elif c==2:
                cultura = "Milho"
                volta = False
            else:
                print("Opção inválida!")            
       
        area[0] = int(input("Informa a altura da area de plantio me metros: "))
        area[1] = int(input("Informe a largura da area de plantio em metros: "))
    elif opcao == 2:
        print ("Qual o tipo de Cultura?\n1 - Café\n2 - Milho")
        volta = True
        while volta:
            c = int(input(f"Escolha a opção (valor atual: {cultura}): "))
            if c==1:
                cultura = "Café"
                volta = False
            elif c==2:
                cultura = "Milho"
                volta = False
            else:
                print("Opção inválida!")            
        
        area[0] = int(input(f"Informa a altura da area de plantio me metros (valor atual {area[0]}): "))
        area[1] = int(input(f"Informe a largura da area de plantio em metros: (valor atual {area[1]})"))
    elif opcao == 3:
        area[0] = 0
        area[1] = 0
        cultuira = ""
    elif opcao == 4:
        areaTotal = area[0] * area[1]
        # cafe 10, milho 5
        ruas=0
        if cultura=="Café":
            ruas = 10
            densidade = 5000
            insumo_m2 = 0.05
        elif cultura=="Milho":
            ruas=5
            densidade = 60000
            insumo_m2 = 0.02
        areaUtil = areaTotal * ((100-ruas)/100)
        insumos = areaUtil * insumo_m2
    elif opcao == 5:
        print(f"Cultura: {cultura}")
        print(f"Area total {areaTotal} metros" )
        print(f"Area util {areaUtil} metros" )
        print(f"Insumos {insumos} ")
        

