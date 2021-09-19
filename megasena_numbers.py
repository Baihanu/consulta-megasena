from selenium import webdriver
from bs4 import BeautifulSoup
from chromedriver_py import binary_path


class GetMegaSenaNumber():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=binary_path)
        self.driver.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
    
    def get_numbers(self):
        result = {}
        html = self.driver.page_source
        parsed_html = BeautifulSoup(html, 'lxml')
        
        dezenas = parsed_html.find('ul', {'id': 'ulDezenas'})
        li_dezenas = dezenas.find_all('li')
        list_dezenas = []

        for li in li_dezenas:
            de = li.getText()
            list_dezenas.append(de)

        result['Dezenas'] = list_dezenas
        print(result)

try:
    bot = GetMegaSenaNumber()
    bot.get_numbers()
except:
    "Try again"