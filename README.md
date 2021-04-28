# Catálogo Scraper
Script em Python que faz a raspagem de infomações do Catálogo da UFV. Utilizado para criar o banco de dados do Espia Só.

## Uso

Para executar o script é necessário que você tenha o Python 3 instalado no seu computador. Depois disso, precisa executar o comando `pip install -r requirements.txt` para instalar as bibliotecas necessárias e executar o script com `python scraper.py`

Será criado um diretório `pages` contendo os arquivos html das matrizesc curiculares. Além disso, serão criados dois arquivos json: `courses.json` e `disciplines.json`, que contém as informações dos cursos e disciplinas, respectivamente.