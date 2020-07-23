import sqlite3
import json

doc=open(r"C:\Users\jpmarques\Desktop\BS4\Nome_filme.json")
dici=json.load(doc)
lista=dici.items()

print(lista)


#SQL
class guarda_info():
    def __init__(self):
        self.con=sqlite3.connect('Adoro_Cinema.db')
        self.c=self.con.cursor()

    def cria_tabela(self):
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS "Info_filmes" (
	        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	        "Nome"	String,
            "Desc"  String

                     );""")

    def ent_info(self):
            self.c.executemany("""
            INSERT INTO "Info_filmes" ( Nome, Desc )
            VALUES (?,?)""",lista)
            self.con.commit()





g=guarda_info()
g.cria_tabela()
g.ent_info()
