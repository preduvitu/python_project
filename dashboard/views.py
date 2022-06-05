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

    dados_catho = []

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

    catho = site.find('ul', {'class': 'sc-gGBfsJ exVOlL gtm-class'})

    for cath in catho:

        link = cath.find('a', {'tabindex': '1'})

        descricao = cath.find('span', {'class': 'job-description'})

        dados_catho.append([link['title'], link['href'],descricao])

        dados = pd.DataFrame(dados_catho, columns={'Título', 'Link', 'Descrição'})

    dados.to_html('template/catho.html', index=False)
    dados.to_excel('catho.xlsx', index=False)

    return render(request, 'detalhes.html')
