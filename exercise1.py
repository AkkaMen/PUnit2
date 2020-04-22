#imports
# -*- coding: utf-8 -*-
import re
from os import listdir
import codecs

#constant
input = "./input/"


files = listdir(input)

def name(outputName, function):
    for file in files:
        print(file)
        content = codecs.open(input + file, "r", encoding="UTF-8")
        writer = codecs.open(outputName + file, "w", encoding="UTF-8")
        for i in content:
            writer.write(function(i))    
        
    pass

def exercise1(content):
    f=content#.decode('UTF-8', errors='ignore')
    res=re.findall(r'\w+|\W+|\d+|[а-яА-Я]+|\.|\,', f)
    #res=re.findall(r'[0-9a-zA-Zа-яА-Я]+|[^0-9a-zA-Zа-яА-Я]{1}', f)
    #print(' '.join(res))
    return ' '.join(res)



name("./exercise1/output/", exercise1)
#string='РґРёРєС‚РѕСЂР°, РїРµСЂРµРІРѕРґС‡РёРєР°-СЃРёРЅС…СЂРѕРЅРёСЃС‚Р° Рё РєРёРЅРѕР°РєС‚РµСЂР° РљРёСЂРёР»Р»Р° Р’Р°С†Р°.'
#res=string.decode('UTF-8', errors='ignore')
#print(res)
#print(' '.join(re.findall(r'[а-яА-Я]*', res)))

text = '100 ИНФ Информатика, 120 АНГ Английский. 130 МАТ Математика,'

print(' '.join(re.findall('\w+|[а-яА-Я]+', text)).decode('UTF-8', errors='ignore'))

