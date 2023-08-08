import json

# Abre o arquivo JSON com a codificação ISO-8859-1 (latin1)
with open('arquivo.json', 'r', encoding='iso-8859-1') as json_file:
    data = json.load(json_file)

# Lista de períodos
periodos = ["2018.2", "2019.1", "2019.2"]  # Adicione os períodos que você deseja

# Adiciona o atributo "periodo" para todas as disciplinas em todos os períodos
for periodo in periodos:
    for disciplina in data['cc'][periodo]:
        data['cc'][periodo][disciplina]['periodo'] = periodo

# Escreve o JSON modificado em um novo arquivo com a codificação ISO-8859-1 (latin1)
with open('dados_modificados.json', 'w', encoding='iso-8859-1') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Atributo 'periodo' adicionado com sucesso às disciplinas de todos os períodos!")
