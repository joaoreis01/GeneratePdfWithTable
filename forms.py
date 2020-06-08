from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors   
import csv

with open('dados.csv', encoding='utf-8') as dados:
        listaComDados = []
        ler = csv.reader(dados, delimiter=';') #Lê o arquivo .csv que está armazenado na variavel dados, avisa que ; é o delimitador
        next(ler) #pula o cabeçalho (primeira linha)
        for linha in ler:  #para cada linha na lista ler, é adicionada na listaComDados
            listaComDados.append(linha) #adicionando a linha a lista de nome lista
            print(listaComDados)

        i = 0 

        for cada_lista in listaComDados: #Para cada lista contida na listaComDados

            fileName = 'Forms'+str(i)+'.pdf' #Defini o nome do arquivo, caso existe sobrescreve, se não existir cria um novo
            data = [['NOME', listaComDados[i][0]], ['IDADE', listaComDados[i][1]], ['SEXO', listaComDados[i][2]], ['TELEFONE', listaComDados[i][3]]] #Campos com os dados que serão inseridos

            pdf = SimpleDocTemplate(fileName, pagesize=letter) #Cria o pdf

            table = Table(data) #Cria uma tabela com os dados de data

            # 1)Add Style
            style = TableStyle([
                ('FONTNAME', (0, 0), (0, -1), 'Courier'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),

                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ])

            table.setStyle(style)

            # 3)Add Borders
            ts = TableStyle([
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
                ('RIGHTPADDING', (1, 0), (-1, 0), 190),
            ])

            table.setStyle(ts)

            #Inserindo no pdf
            elems = []
            elems.append(table)

            pdf.build(elems)

            i = i + 1

