#pip install beautifulsoup4
from selenium import webdriver
from bs4 import BeautifulSoup as bs


end_base= 'http://www.adorocinema.com'
end_Mfil=  f'{end_base}/filmes/todos-filmes/notas-espectadores/'

ff=webdriver.Firefox()
ff.get(end_Mfil)
obj_AC=bs(ff.page_source, 'html.parser')

filmes = obj_AC.find_all('div',{'class':'data_box'})

compl_filme = [link_desc.find('a').get('href') for link_desc in filmes]
links_completo= [f'{end_base}{i}' for i in compl_filme]


v=obj_AC.find('a',{'class':'xXx button btn-default btn-large fr'}).get('href')
h= f'{end_base}{v}'

while ff.get(h):
	pass
for j in links_completo:
    ff.get(j)
    pag_desc=bs(ff.page_source, 'html.parser')
    Nome_filme=pag_desc.find('div', {'class':'titlebar-title titlebar-title-lg'}).text
    Descrição_Filme=pag_desc.find('div', {'class':'content-txt '}).text

    print(Nome_filme, Descrição_Filme)

