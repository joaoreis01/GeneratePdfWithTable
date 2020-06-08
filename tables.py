documentTitle = 'I am Title!'

#List of Lists
data = [
    ['Dedicated Hosting', 'VPS Hosting', 'Sharing', 'teste', ''],
    ['200 Reais', '300', '400', 'teste', ''],
    ['Free Domain', 'Free', 'Free Domain', 'teste', ''],
    ['2GB', '3GB', '4GB', 'teste', '']
]

data2 = [
    ['nome', 'idade', 'sexo'],
    ['joao', '18', 'masculino']
]

fileName = "pdfTable.pdf"

from reportlab.platypus import SimpleDocTemplate #With SimpleDocTemplate our table will be automatically in the centeros the document
from reportlab.lib.pagesizes import letter

pdf = SimpleDocTemplate( #Gernado um pdf
    fileName,
    pagesize=letter
)

from reportlab.platypus import Table
table = Table(data) #gera uma tabela a partir da Data

#add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors

style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.green), #(0, 0), (-1, 0) : Starting Cell and Ending Cell
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), # -1 means go to the last element in the X coordinate, caso deixe um número fico positivo, a config só ira até ali

    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

    ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),

    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('RIGHTPADDING', (4, 0), (4, 0), 50),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
])

table.setStyle(style)

# 2) Alternate backgroun color
rowNumb = len(data) #Número de linhas é igual ao tamanho da lista data
for i in range(1, rowNumb): #inicia o loop no 1 para ignorar o cabeçalho
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige

    ts = TableStyle(
        [('BACKGROUND', (0, i), (-1, i), bc)]
    )

    table.setStyle(ts)

# 3) Add borders
ts = TableStyle(
    [
    ('BOX', (0, 0), (-1, -1,), 2, colors.black),
    ('GRID', (0, 0), (-1, -1), 2, colors.black)
    ]
)
table.setStyle(ts)

#Inserindo no pdf
elems = [] #Elements to be added to our pdf
elems.append(table) #adicionando a list elems[],a variávell table que armazena os dados contidos na list Data


pdf.build(elems) #Passando a list que contem os elementos a serem inseridos no PDF
