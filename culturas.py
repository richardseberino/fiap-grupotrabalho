TIPOS_DE_CULTURA = ["Café", "Milho"]

CACHE_CULTURAS = []

def lista_culturas():
  return CACHE_CULTURAS

def encontra_cultura(identificador):
  try:
    return CACHE_CULTURAS[identificador]
  except IndexError:
    return None

def cria_cultura(cultura):
  CACHE_CULTURAS.append(cultura)

def atualiza_cultura(identificador, cultura):
  CACHE_CULTURAS[identificador] = cultura

def deleta_cultura(identificafor):
  try:
    return CACHE_CULTURAS.pop(identificafor)
  except IndexError:
    return None

def nova_cultuta(tipo_cultura, altura, largura):
  area_total = altura * largura

  insumos_m2 = 0
  ruas = 0

  if tipo_cultura == "Café":
    insumos_m2 = 0.05
    ruas = 0.9
  else:
    insumos_m2 = 0.02
    ruas = 0.95

  area_util = area_total * ruas
  insumos = area_util * insumos_m2

  return {
    "cultura": tipo_cultura,
    "altura": altura,
    "largura": largura,
    "area_total": area_total,
    "area_util": area_util,
    "insumos": insumos,
  }
    