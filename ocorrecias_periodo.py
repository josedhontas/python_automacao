import json

def atualizar_periodo_disciplina(nome_disciplina, nome_curso, novo_periodo):
    # Abre o arquivo JSON com a codificação ISO-8859-1 (latin1)
    with open('dados_modificados.json', 'r', encoding='iso-8859-1') as json_file:
        data = json.load(json_file)

    if nome_curso in data and nome_disciplina in data[nome_curso]:
        # Atualiza o atributo "periodo" para a disciplina especificada
        data[nome_curso][nome_disciplina]['periodo'] = novo_periodo

        # Escreve o JSON modificado de volta ao arquivo
        with open('dados.json', 'w', encoding='iso-8859-1') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f"Atributo 'periodo' da disciplina '{nome_disciplina}' do curso '{nome_curso}' atualizado para '{novo_periodo}'.")
    else:
        print(f"Disciplina '{nome_disciplina}' não encontrada no curso '{nome_curso}'.")

# Chame a função com os valores desejados
nome_disciplina = "Programação Imperativa"
nome_curso = "cc"
novo_periodo = "2°"
atualizar_periodo_disciplina(nome_disciplina, nome_curso, novo_periodo)
