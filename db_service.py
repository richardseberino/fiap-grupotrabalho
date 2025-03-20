import csv

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