CAMINHO_DO_ARQUIVO = "./bd.csv"

import csv

def carrega_dados_para_cache(cache):
  data = []

  try:
    with open(CAMINHO_DO_ARQUIVO, mode='r', encoding='utf-8') as file:
      reader = csv.DictReader(file, delimiter=';')
      
      for line in reader:
        data.append({
          "cultura": line['cultura'], 
          "altura": int(line['altura']),
          "largura": int(line['largura']),
          "area_total": float(line['area_total']),
          "area_util": float(line['area_util']),
          "insumos": float(line['insumos']),
        })
  except Exception as e:
    print(e)
    data = []

  # Limpa se algo existir previamente
  # [:] é necessário porque no Python argumentos são passados por valor e não por referência
  cache[:] = data

  return cache

def salva_dados_do_cache(cache):
  header = ['cultura', 'altura', 'largura', 'area_util', 'area_total', 'insumos']
  
  with open(CAMINHO_DO_ARQUIVO, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
    writer.writeheader()
    writer.writerows(cache)
