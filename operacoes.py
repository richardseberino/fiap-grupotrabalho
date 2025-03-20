import util
import sys
import questionary
import culturas
import csv


SAIR = 5
LIMPAR_TERMINAL = -1

lista = []



def le_arquivo(path: str) -> list[dict]:
    data = []

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for line in reader:
                linha = {"cultura": line['cultura'], 
                    "altura": int(line['altura']),
                    "largura": int(line['largura']),
                    "areaTotal": int(line['areaTotal']),
                    "areaUtil": int(line['areaUtil']),
                    "insumos": int(line['insumos'])
                    }
                data.append(linha)
    except FileNotFoundError:
        data = [] 
    return data

def salva_arquivo(path: str, data: list[dict]):
    header = ['cultura', 'altura', 'largura', 'areaUtil', 'areaTotal', 'insumos']
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

def executar(opcao_selecionada):
  match opcao_selecionada:
    case 1:
      __executar_acao("Criando nova cultura", __criar_cultura)
    case 2:
      __executar_acao("Listando culturas", __listar_culturas)
    case 3:
      __executar_acao("Atualizando cultura", __atualizar_cultura)
    case 4:
      __executar_acao("Deletando cultura", __deletar_cultura)
    case 5:
      __executar_acao("Saindo da aplicação...", __sair)
    case _:
      util.limpar_terminal()

def __executar_acao(titulo, acao):
  util.limpar_terminal()

  linha = "*" * (len(titulo) + 6) 
  print(linha)
  print(f"** {titulo} **")
  print(linha)

  print()
  acao()
  print()
  
  input("Pressione qualquer tecla para voltar ")
  util.limpar_terminal()


def informarCultura():
  cultura = questionary.select(
      "Escolha o tipo de cultura:",
      choices=culturas.TIPOS_DE_CULTURA,).ask()
  altura = int(input("Informa a altura da area de plantio me metros: "))
  largura = int(input("Informe a largura da area de plantio em metros: "))
  insumo_m2=0
  ruas = 0
  if cultura == "Café":
    insumo_m2 = 0.05
    ruas = 0.9
  elif cultura == "Milho":
    insumo_m2 = 0.02
    ruas = 0.95

  dados = {"cultura": cultura, 
            "altura": altura,
            "largura": largura,
            "areaTotal": (altura*largura),
            "areaUtil": ((largura*altura)*ruas),
            "insumos": ((largura*altura)*ruas)*insumo_m2
            }
  return dados

def imprimeValores(itens):
    for volta in range(0, len(itens), 1):
        print("# "+ str(volta+1)  +  " - Cultura: " + itens[volta]["cultura"] + ", altura: " 
              + str(itens[volta]["altura"]) + ", largura: " + str(itens[volta]["largura"]) 
              + ", area Total: " + str(itens[volta]["areaTotal"])
              + ", area Util: " + str(itens[volta]["areaUtil"]) 
              + ", Insumos: " + str(itens[volta]["insumos"])) 

def __criar_cultura():
  lista.append(informarCultura())
  
  
def __listar_culturas():
  print("Listando culturas")
  imprimeValores(lista)

def __atualizar_cultura():
    print("Segue a lista atual: ")
    imprimeValores(lista)
    linha = int(input("Informe a linha que voce quer alterar: "))
    if linha > len(lista):
        print("Linha invalida!")
    else:
        lista[linha-1] = informarCultura()


def __deletar_cultura():
      print("Segue a lista atual: ")
      imprimeValores(lista)
      linha = int(input("Informe a linha que voce quer excluir: "))
      if linha > len(lista):
          print("Linha invalida!")
      else:
          del(lista[linha-1])

def __sair():
  salva_arquivo("teste.csv", lista)
  sys.exit("Até logo ✌\n")
