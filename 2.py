na=ca=nl=dt=pt=tl=of=pc=rq=bl=ip=bu=ct=hi=ma=ef=us=cs= None
import pandas as pd
import numpy as np
import json
import os
import sqlite3

data = json.load(open(r'C:\Users\jpmarques\Desktop\Jsons\REP 1971-19 - BA0441.json'))
dicionarios = []
labels = []
for chave in data.keys():
    if type(data[chave])==dict:
        dicionarios.append(data[chave])
        labels.append(chave)
for chave in labels:
      data.pop(chave)




class guarda_info():
    def __init__(self):
        self.con=sqlite3.connect('Laudos.db')
        self.c=self.con.cursor()
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS "Laudos" (
	        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	        "nome_do_arquivo"	String,
            "caminho_do_arquivo"  String,
            'num_laudo'  String,
            'data'  String,
            'perito'  String,
            'tipo_laudo'  String,
            'oficio'  String,
            'protocolo'  String,
            'requisitante'  String,
            'balistica'  String,
            'ip'  String,
            'bu'  String,
            'cartucho' String,
            'historico'  String,
            'material'  String,
            'eficiencia'  String,
            'uso'  String,
            'conclusao'  String
            );""")

    def input(self,na,ca,nl,dt,pt,tl,of,pc,rq,bl,ip,bu,ct,hi,ma,ef,us,cs):
            self.c.execute("""
            INSERT INTO "Laudos" (material,eficiencia,uso,conclusao)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(na,ca,nl,dt,pt,tl,of,pc,rq,bl,ip,bu,ct,hi,ma,ef,us,cs,))
            self.con.commit()

    def encontra_info(self):
        na=ca=nl=dt=pt=tl=of=pc=rq=bl=ip=bu=ct=hi=ma=ef=us=cs= None
        for i in data.keys():
            if i == 'nome_do_arquivo':
                na=data[i]
            elif i=='caminho_do_arquivo':
                ca=data[i]
            elif i=='num_laudo':
                nl=data[i]
            elif i=='data':
                dt=data[i]
            elif i=='perito':
                pt=data[i]
            elif i=='tipo_laudo':
                tl=data[i]
            elif i=='oficio':
                of=data[i]
            elif i=='protocolo':
                pc=data[i]
            elif i=='requisitante':
                rq=data[i]
            elif i=='balistica':
                bl=data[i]
            elif i=='ip':
                ip=data[i]
            elif i=='bu':
                bu=data[i]
            elif i=='cartucho':
                ct=data[i]
            elif i=='historico':
                hi=data[i]
            elif i=='material':
                ma=data[i]
            elif i=='eficiencia':
                ef=data[i]
            elif i=='uso':
                us=data[i]
            elif i=='conclusao':
                cs=data[i]
            g.input(na,ca,nl,dt,pt,tl,of,pc,rq,bl,ip,bu,ct,hi,ma,ef,us,cs)

g=guarda_info()
g.encontra_info()
