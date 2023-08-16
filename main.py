import requests
from bs4 import BeautifulSoup
from ebooklib import epub

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

# Criar um arquivo EPUB
livro = epub.EpubBook()

# Informações do livro
livro.set_title('Warlock of the Magus World')
livro.set_language('pt-BR')

# Lista de números de páginas a serem baixadas
numeros_paginas = range(500, 801)  # Por exemplo, baixar os dados das páginas 1, 2 e 3

total_paginas = len(numeros_paginas)
for index, numero_pagina in enumerate(numeros_paginas, start=1):
    url_pagina_web = f'https://www.ceunovel.com/warlock-of-the-magus-world/chapter-{numero_pagina}'
    texto_pagina = baixar_texto_pagina_web(url_pagina_web)

    if texto_pagina:
        texto_filtrado = filtrar_texto(texto_pagina)

        # Adicionar o conteúdo filtrado ao arquivo EPUB
        capitulo = epub.EpubHtml(title=f'Capítulo {numero_pagina}', file_name=f'capitulo-{numero_pagina}.xhtml', lang='pt-BR')
        capitulo.content = texto_filtrado
        livro.add_item(capitulo)

    # Exibir a porcentagem de conclusão
    porcentagem_concluida = (index / total_paginas) * 100
    print(f'Progresso: {porcentagem_concluida:.2f}%')

# Definir a ordem dos capítulos no livro
livro.spine = ['nav'] + [capitulo for capitulo in livro.get_items()]

# Salvar o arquivo EPUB
epub.write_epub('warlock_of_the_magus_world.epub', livro, {})

print('Arquivo EPUB criado com sucesso!')
