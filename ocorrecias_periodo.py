import json

def atualizar_periodo_por_nome_materia(dados, lista_nomes, novo_periodo):
    for periodo in dados:
        for disciplina in dados[periodo]:
            nome_disciplina = dados[periodo][disciplina]['nome']
            if nome_disciplina in lista_nomes:
                print(nome_disciplina)
                dados[periodo][disciplina]['periodo'] = novo_periodo

# Abre o arquivo JSON com a codificação UTF-8
with open('AllData.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Lista de nomes de matéria a serem atualizados
#Tenho que iniciar do 5 em cc, depois sigo os outros cursos
nomes_materias = ["Inteligência Artificial"]  # Adicione os nomes das matérias aqui
novo_periodo = "6°"  # Novo valor para o atributo "periodo"

# Chama a função para atualizar o valor do atributo "periodo"
atualizar_periodo_por_nome_materia(data['si'], nomes_materias, novo_periodo)

# Escreve o JSON modificado de volta no arquivo
with open('AllData.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Atributo 'periodo' atualizado para '{novo_periodo}' para as matérias: {', '.join(nomes_materias)} em todos os períodos.")
