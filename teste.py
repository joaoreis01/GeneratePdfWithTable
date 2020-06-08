import csv

lista =[]


with open('datas.csv', encoding='utf-8') as entrada:
    ler = csv.reader(entrada, delimiter=';')
    next(ler)
    for linha in ler:
        lista.append(linha)
        print(lista)

'''for cada_lista in lista:
    print(cada_lista)'''