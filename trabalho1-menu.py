import csv

lista = []
bd_path = 'bd.csv'

def imprimeValores(itens):
    for volta in range(0, len(itens), 1):
        print("# "+ str(volta+1)  +  " - Cultura: " + itens[volta]["cultura"] + ", altura: " 
              + str(itens[volta]["altura"]) + ", largura: " + str(itens[volta]["largura"]) 
              + ", area Total: " + str(itens[volta]["areaTotal"])
              + ", area Util: " + str(itens[volta]["areaUtil"]) 
              + ", Insumos: " + str(itens[volta]["insumos"])) 

def informaCultura():
    print ("Qual o tipo de Cultura?\n1 - Café\n2 - Milho")
    volta = True
    ruas = 0
    while volta:
        c = int(input("Escolha a opção: "))
        if c==1:
            cultura = "Café"
            ruas = 10
            volta = False
        elif c==2:
            cultura = "Milho"
            ruas = 5
            volta = False
        else:
            print("Opção inválida!")            
    
    altura = int(input("Informa a altura da area de plantio me metros: "))
    largura = int(input("Informe a largura da area de plantio em metros: "))
    dados = {"cultura": cultura, 
              "altura": altura,
              "largura": largura,
              "areaTotal": (altura*largura),
              "areaUtil": 0,
              "insumos": 0
              }
    return dados

def read_csv(path: str) -> list[dict]:
    data = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for line in reader:
            for key in ['altura', 'largura', 'areaUtil', 'areaTotal', 'insumos']:
                line[key] = int(line[key])
            data.append(line)
    return data

def write_csv(path: str, data: list[dict]):
    header = ['cultura', 'altura', 'largura', 'areaUtil', 'areaTotal', 'insumos']
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

def run():
    while True:
        print("Menu de opções:\n")

        print("1 - Informar os dados para calculo")
        print("2 - Atualizar os daados")
        print("3 - Excluir os dados")
        print("4 - Calcular")
        print("5 - Exibit resultado")
        print("\n\n0 - Sair")

        opcao = int(input("Escolha a opção desejada: "))

        if opcao == 0:
            break
        elif opcao == 1:
            lista.append(informaCultura())
        elif opcao == 2:
            print("Segue a lista atual: ")
            imprimeValores(lista)
            linha = int(input("Informe a linha que voce quer alterar: "))
            if linha > len(lista):
                print("Linha invalida!")
            else:
                lista[linha-1] = informaCultura()
        elif opcao == 3:
            print("Segue a lista atual: ")
            imprimeValores(lista)
            linha = int(input("Informe a linha que voce quer excluir: "))
            if linha > len(lista):
                print("Linha invalida!")
            else:
                del(lista[linha-1])
        elif opcao == 4:
            for volta in range(0, (len(lista)), 1):
                print(volta)
                cultura = lista[volta]["cultura"]
                if cultura == "Café":
                    lista[volta]["areaUtil"] = lista[volta]["areaTotal"] * 0.9
                    insumo_m2 = 0.05
                    lista[volta]["insumos"] = lista[volta]["areaUtil"] * insumo_m2
                elif cultura == "Milho":
                    lista[volta]["areaUtil"] = lista[volta]["areaTotal"] * 0.95
                    insumo_m2 = 0.02
                    lista[volta]["insumos"] = lista[volta]["areaUtil"] * insumo_m2

        elif opcao == 5:
            imprimeValores(lista)

if __name__ == '__main__':
    lista = read_csv(bd_path)
    run()
    write_csv(bd_path, lista)