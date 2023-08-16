import json

def atualizar_periodos(dados):
    for periodo in dados:
        for disciplina in dados[periodo]:
            if "periodo" in dados[periodo][disciplina]:
                novo_periodo = dados[periodo][disciplina]['periodo']
                if len(novo_periodo) == 1 and novo_periodo.isdigit():
                    dados[periodo][disciplina]['periodo'] = novo_periodo.zfill(2)

# Abre o arquivo JSON com a codificação UTF-8
with open('AllData.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Chama a função para atualizar o valor do atributo "periodo" em todas as matérias e períodos
atualizar_periodos(data['cc'])
atualizar_periodos(data['si'])
# Adicione chamadas para outros cursos ('cc', 'si', etc.) se necessário

# Escreve o JSON modificado de volta no arquivo
with open('AllData.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Atributo 'periodo' atualizado em todos os períodos e matérias.")
