import re
import os
import unidecode
import json


doc=open(r"C:\Users\jpmarques\Desktop\Jsons\REP 17265-19 - BI3952.json")
dici=json.load(doc)
lista=dici.keys()
print(lista)
