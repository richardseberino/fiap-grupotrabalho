import util
import sys
import questionary
import culturas

SAIR = 5
LIMPAR_TERMINAL = -1

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

def __criar_cultura():
  cultura = questionary.select(
      "Escolha o tipo de cultura:",
      choices=culturas.TIPOS_DE_CULTURA,
  ).ask()

  print(f"\nCultura selecionada: {cultura}")
  
def __listar_culturas():
  print("Listando culturas")

def __atualizar_cultura():
  print("Informe o ID da cultura a ser atualizada:")

def __deletar_cultura():
  print("Informe o ID da cultura a ser deletada:")

def __sair():
  sys.exit("Até logo ✌\n")
