import json
from unidecode import unidecode

def atualizar_periodo_por_nome_materia(dados, nome_materia, novo_periodo):
    for periodo in dados:
        for disciplina in dados[periodo]:
            nome_disciplina = (dados[periodo][disciplina]['nome'])
            nome_materia_formatado = (nome_materia)
            print(nome_disciplina, nome_materia_formatado)
            if nome_disciplina == nome_materia_formatado:
                print(nome_disciplina)
                dados[periodo][disciplina]['periodo'] = novo_periodo

# Abre o arquivo JSON com a codificação ISO-8859-1 (latin1)
with open('dados_modificados.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Parâmetros para atualização
nome_materia = "Programação Imperativa"  # Nome da matéria a ser atualizada
novo_periodo = "2°"  # Novo valor para o atributo "periodo"

# Chama a função para atualizar o valor do atributo "periodo"
atualizar_periodo_por_nome_materia(data['cc'], nome_materia, novo_periodo)

# Escreve o JSON modificado de volta no arquivo
with open('dados_modificados.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Atributo 'periodo' atualizado para '{novo_periodo}' para a matéria '{nome_materia}' em todos os períodos.")
