from encodings import utf_8
from django.shortcuts import render
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os

def dashboard(request):
    return render(request, 'dashboard.html')

def detalhes(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=400,800')

    navegador = webdriver.Chrome(options=options)

    response = navegador.get('https://www.catho.com.br/')

    sleep(1)
    valor = request.POST['search']
    input_procurar = navegador.find_element_by_name('q')
    input_procurar.send_keys(valor)
    input_procurar.submit()

    sleep(1)

    page_content = navegador.page_source

    site = BeautifulSoup(page_content, 'html.parser')

    catho = site.find_all('span', {'class': 'job-description'})

    dados = pd.DataFrame(catho, columns=['Descrição'])

    dados = dados.to_html('template/catho.html', index=False)

    # DATA_DIR = "template"
    # OUT_DIR = "template"

    # def get_name(filename, dirname=DATA_DIR):
    #     return os.path.join(dirname, filename)

    # def remove_chars(text, undesireds):
    #     for c in undesireds:
    #         text  = text.replace(c, " ")
    #     return text

    # def stopwordslist():
    #     lines = []
    #     with open(get_name("stopwords.txt"), "r") as stopfile:
    #         lines = [ line.strip() for line in stopfile.readlines() ]
    #     return lines

    # TO_REMOVE = ['(', ')', '[', ']', '?', '!', ':', '...', ';', '"', ',',]

    # if __name__ == "__main__":
    #     with open(get_name(dados)) as cathofile:
    #         content = cathofile.read()
    #         content = remove_chars(content, TO_REMOVE)
    #         parts = [ p.strip() for p in content.split() ]
    #         stopwords = stopwordslist()
    #         words = [ part for part in parts if part not in stopwords ]
    #         with open(get_name("python.txt",OUT_DIR), "w") as textfile:
    #                 textfile.write(" ".join(words))

    return render(request, 'catho.html')
