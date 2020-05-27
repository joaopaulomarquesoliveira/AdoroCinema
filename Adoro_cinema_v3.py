#pip install beautifulsoup4
from selenium import webdriver
from bs4 import BeautifulSoup as bs


saida={}


class Adoro_Cinema:
    def __init__(self,driver):
        self.driver = driver
        self.end_base= 'http://www.adorocinema.com'
        self.end_Mfil= (f'{self.end_base}/filmes/todos-filmes/notas-espectadores/')

    def Navegar(self):
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
            Nome_filme=self.pag_desc.find('div', {'class':'titlebar-title titlebar-title-lg'}).text
            Descrição_Filme=self.pag_desc.find('div', {'class':'content-txt '}).text
            saida[Nome_filme]=Descrição_Filme
            print(saida)
            return saida

    def Pass_pag(self):
        v=self.obj_AC.find('a',{'class':'xXx button btn-default btn-large fr'}).get('href')
        self.end_Mfil = f'{self.end_base}{v}'
        if v !=0:
            return True





ff=webdriver.Firefox()
g=Adoro_Cinema(ff)
g.Navegar()
g.Encontrar_obj()
g.Raspagem()
g.Pass_pag()
while g.Pass_pag():
    g.Navegar()
    g.Encontrar_obj()
    g.Raspagem()
    g.Pass_pag()


ff.quit()
