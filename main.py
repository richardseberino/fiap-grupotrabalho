import menus
import operacoes

def main():
  menu = menus.menu_principal()
  operacoes.le_arquivo("teste.csv")
  while True:
    try:
      opcao_selecionada = menu.unsafe_ask()
      operacoes.executar(opcao_selecionada)
    except KeyboardInterrupt:
      opcao_selecionada = menus.menu_confirmacao_de_saida().ask()

      if opcao_selecionada:
        operacoes.executar(operacoes.SAIR)
      else:
        operacoes.executar(operacoes.LIMPAR_TERMINAL)
        continue
      
if __name__ == "__main__":
 
  main()
