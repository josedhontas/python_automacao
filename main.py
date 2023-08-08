import requests
from bs4 import BeautifulSoup

def filtrar_texto(texto):
    # Remover conteúdo antes de "Next" (incluindo "Next")
    texto_filtrado = texto.split('Next', 1)[1]

    # Remover conteúdo depois de "Advertisement" (incluindo "Advertisement")
    texto_filtrado = texto_filtrado.split('Advertisement', 1)[0]

    return texto_filtrado

def baixar_texto_pagina_web(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verificar se a resposta foi bem-sucedida
        conteudo_html = resposta.text

        # Utilizando BeautifulSoup para extrair apenas o texto da página
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        texto_sem_tags = soup.get_text()

        return texto_sem_tags
    except requests.exceptions.RequestException as e:
        print('Ocorreu um erro ao baixar o conteúdo:', e)
        return None

# Lista de números de páginas a serem baixadas
numeros_paginas = range(1, 4)  # Por exemplo, baixar os dados das páginas 1, 2 e 3

for numero_pagina in numeros_paginas:
    url_pagina_web = f'https://www.ceunovel.com/warlock-of-the-magus-world/chapter-{numero_pagina}'  # Substitua pela URL da página que você deseja baixar o texto
    texto_pagina = baixar_texto_pagina_web(url_pagina_web)

    if texto_pagina:
        texto_filtrado = filtrar_texto(texto_pagina)

        # Obtendo o primeiro parágrafo (removendo espaços em branco extras no início e no final)
        paragrafo_limpo = texto_filtrado.strip().split('\n')[0].strip()

        if paragrafo_limpo:
            # Remover a ocorrência do primeiro parágrafo do texto filtrado
            texto_filtrado = texto_filtrado.replace(paragrafo_limpo, '', 1).strip()

            # Adicionar um "-" após cada parágrafo
            texto_filtrado = '\n- '.join(texto_filtrado.split('\n\n')).strip()

            # Salvando o texto filtrado em um arquivo de texto
            nome_arquivo = f'{numero_pagina} - {paragrafo_limpo}.txt'
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(texto_filtrado)

            print(f'Texto filtrado da página {numero_pagina} salvo em: {nome_arquivo}')
        else:
            print(f'A página {numero_pagina} não contém um primeiro parágrafo válido.')
