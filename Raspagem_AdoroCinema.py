#pip install beautifulsoup4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import json
import unidecode
import time

dic = {}

class Adoro_Cinema:
    def __init__(self,driver):
        self.driver = driver
        self.end_base= 'http://www.adorocinema.com'
        self.end_Mfil= (f'{self.end_base}/filmes/todos-filmes/notas-espectadores/')

    def pegOrc(self,driver,nome):
        self.aux=driver
        self.nome=nome
        driver.execute_script("window.open('http://www.google.com')")
        self.aux.find_element_by_name("q").send_keys(f'{self.nome} orçamento' + Keys.RETURN)
        time.sleep(5)
        font=bs(self.aux.page_source, 'html.parser')
        Orc=unidecode.unidecode(font.find('div', {'class':'Z0LcW XcVN5d'}).text)
        self.aux.close() 
        return Orc

        
	
    def Navegar(self):
        aux=False
        self.driver.get(self.end_Mfil)
        self.obj_AC=bs(self.driver.page_source, 'html.parser')

    def Encontrar_obj(self):

        self.filmes = self.obj_AC.find_all('div',{'class':'data_box'})
        self.compl_filme = [link_desc.find('a').get('href') for link_desc in self.filmes]
        self.links_completo= [f'{self.end_base}{i}' for i in self.compl_filme]

    def Raspagem(self):

        for j in self.links_completo:
            self.driver.get(j)
            self.pag_desc=bs(self.driver.page_source, 'html.parser')
            Descrição_Filme=Titulo_original=Distribuidor=Ano=Tipo=Orcamento=Data_ret=Idiomas=Formato=Cor=Audio=Tipo_proje=Num_visa=None
            Nome_filme=unidecode.unidecode(self.pag_desc.find('div', {'class':'titlebar-title titlebar-title-lg'}).text)
            dic[Nome_filme] = []
            ovelha=None
            try:
                Descrição_Filme=unidecode.unidecode(self.pag_desc.find('div', {'class':'content-txt'}).find('p').text)
                dic[Nome_filme].append(Descrição_Filme)
            except:
                 dic[Nome_filme].append(ovelha)
            try:           
                Titulo_original=unidecode.unidecode(self.pag_desc.find('h2',{'class':'that'}).text)
                dic[Nome_filme].append(Titulo_original)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Distribuidor = unidecode.unidecode(self.pag_desc.find('a',{'class':'xXx that blue-link'}).text)
                dic[Nome_filme].append(Distribuidor)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Ano =unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[0].text)
                dic[Nome_filme].append(Ano)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Tipo = unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[1].text)
                dic[Nome_filme].append(Tipo)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Orcamento =unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[2].text)
                dic[Nome_filme].append(Orcamento)
            except:
                dic[Nome_filme].append(ovelha)
            
            try:
            	Data_ret =unidecode.unidecode(self.pag_desc.findbs_html.find('div',{'class':'more-hidden'}).find_all('a')[1].text)
            	dic[Nome_filme].append(Data_ret)
            except:
           		dic[Nome_filme].append(ovelha)
            try:
                Idiomas =unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[3].text)
                dic[Nome_filme].append(Idiomas)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Formato = unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[4].text)
                dic[Nome_filme].append(Formato)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Cor = unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[5].text)
                dic[Nome_filme].append(Cor)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Audio =unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[6].text)
                dic[Nome_filme].append(Audio)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Tipo_proje =unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[7].text)
                dic[Nome_filme].append(Tipo_proje)
            except:
                dic[Nome_filme].append(ovelha)
            try:
                Num_visa = unidecode.unidecode(self.pag_desc.find('div',{'class':'more-hidden'}).find_all('span',{'class':'that'})[8].text)
                dic[Nome_filme].append(Num_visa)
            except:
                dic[Nome_filme].append(ovelha)



    def Pass_pag(self):
        v=self.obj_AC.find('a',{'class':'xXx button btn-default btn-large fr'}).get('href')
        self.end_Mfil = f'{self.end_base}{v}'
        if v !=0:
            return True

    def json(self):
        with open('Completon', 'w') as arquivo:
            json.dump(dic, arquivo)
            arquivo.close()
        print(dic)

ff=webdriver.Firefox()
g=Adoro_Cinema(ff)
g.Navegar()
g.Encontrar_obj()
g.Raspagem()
g.Pass_pag()
#while g.Pass_pag():
 #   g.Navegar()
  #  g.Encontrar_obj()
   # g.Raspagem()
    #g.Pass_pag()

g.json()
ff.quit()


