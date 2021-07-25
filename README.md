# Catálogo Scraper

Script em Python que faz a raspagem de infomações do Catálogo da UFV.

## Funcionalidades

Basicamente captura informações do catálogo e disponibiliza em formato json. São gerados dois arquivos, com as estruturas a seguir:

courses.json:

```json
{
    "id": ...,
    "name": ...,
    "disciplines": [
        {
            "Code": ...,
            "Semester": ...
        },
    ]
}
```

disciplines.json

```json
{
    "code": ...,
    "name": ...,
    "dependencies": [...]
}
```

## 🚀 Começando

### 1. Instale o Python 3 e o GeckoDriver

Caso ainda não tenha o Python 3 instalado no seu computador, instale seguindo as [instruções oficiais para o seu sistema operacional](https://www.python.org/downloads/).

Além disso, também precisará do [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

### 2. Clone o repositório

```
git clone https://github.com/OpenSourceLabUFV/catalogo-scraper.git
```

### 3. Navegue até a pasta

```
cd catalogo-scraper
```

### 4. Instale as Dependências

```
pip install -r requirements.txt
```

### 5. Execute o Script

```
python scraper.py
```

## 🤝 Contribua

Sua ajuda é muito bem-vinda, independente da forma! Confira o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para conhecer todas as formas de contribuir com o projeto. Por exemplo, [sugerir uma nova funcionalidade](https://github.com/OpenSourceLabUFV/catalogo-scraper/issues/new?assignees=&labels=&catalogo-scraper=feature_request.md&title=), [reportar um problema/bug](https://github.com/OpenSourceLabUFV/catalogo-scraper/issues/new?assignees=&labels=bug&catalogo-scraper=bug_report.md&title=), enviar um pull request, ou simplemente utilizar o projeto e comentar sua experiência.

Lembre - se que as contribuições devem seguir nosso [Código de Conduta](CODE_OF_CONDUCT.md).

## 🎫 Licença

Esse projeto é licenciado nos termos da licença open-source [MIT](https://choosealicense.com/licenses/mit) e está disponível de graça.