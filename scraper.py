from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
from bs4 import BeautifulSoup

def getDependencies(raw):
    '''Processa os intertravamentos das disciplinas, removendo caracteres indesejados e mantendo apenas os códigos'''
    first = raw.split('ou')
    first = list(map(lambda x: x.split('e'), first))
    first = [item for sublist in first for item in sublist]
    first = list(map(lambda x: x.replace('(', ''), first))
    first = [i.strip() for i in first]
    first = [i.replace(')', '') for i in first]
    first = [i.replace(' ', '') for i in first]
    first = [i.replace('*', '') for i in first]
    first = [i for i in first if 'OBR' not in i]
    first = [i for i in first if 'TOT' not in i]
    if "" in first:
        return []
    return first

def getCourses():
    '''Pega as páginas da matriz de todos os cursos do catálogo e salva na pasta /pages'''
    driver = webdriver.Firefox()
    driver.get('http://www.catalogo.ufv.br/')

    print(driver.title)

    try:
        # Espera até os elementos carregarem
        works = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bloco"))
        )
    finally:
        blocos = driver.find_elements_by_tag_name('a')
        names = []
        links = []
        # Pega os links e os nomes das disciplinas
        for bloco in blocos:
            link = bloco.get_attribute('href')
            name = bloco.get_attribute('title')
            if 'interno.php' in link:
                names.append(name)
                links.append(link)

        links = list(map(lambda x: x.replace('interno', 'matriz'), links))
        
        try:
           os.mkdir('pages')
        except:
            pass
        
        for index, link in enumerate(links):
            driver.get(link)
            with open("pages/" + names[index].replace(" ", "").lower() + '.html', 'w') as f:
                f.write(driver.page_source)

        driver.quit()

def scrapePages():
    '''Pega todas as informações relevantes das matrizes do curso'''
    ID = 1

    # Json structure for Courses
    courses = {
        "course": []
    }

    disciplines = {
        "disciplines": []
    }

    for filename in os.listdir(os.path.join(os.getcwd(),'pages')):
        # Open all pages
            with open(os.path.join(os.getcwd(), 'pages', filename)) as f:
                page = BeautifulSoup(f, "html.parser")
                # Get the name of the Course
                name = page.find('h2', {'id': 'titulo'}).text.strip()
                discs = []
                table = page.select("div.col-md-12")[1]
                trs = table.select("tr")
                i = 0
                # Discipline information starts in tr 8
                for row in trs[8:]:
                    per = row.select("th.periodo")
                    if per:
                        i = i + 1 if "Optativas" not in per[0].text else 50 
                        continue

                    th = row.find("th")
                    if "Total" not in th.text:
                        # Some disciplines start on tr 7, so I have to check
                        if i == 0:
                            i += 1
                        code = th.text
                        tds = row.select("td")
                        discName = tds[0].text.strip()
                        discs.append({"Code": code, "Semester": i})
                        deps = getDependencies(tds[3].text)

                        disc = {'code': code, 'name': discName, 'dependencies': deps}
                        disciplines['disciplines'].append(disc)
                
                course = {
                    "id": ID,
                    "name": name,
                    "disciplines": discs
                }

                courses['course'].append(course)
                ID += 1

    with open(os.path.join(os.getcwd(), 'courses.json'), 'w') as f:
        json.dump(courses, f, ensure_ascii=False)

    with open(os.path.join(os.getcwd(), 'disciplines.json'), 'w') as f:
        json.dump(disciplines, f, ensure_ascii=False)

getCourses()
scrapePages()