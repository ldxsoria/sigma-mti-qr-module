from GenHTML import GenHTML
from GenQR import GenQR
from GenPDF import crear_pdf

valor1 = 23000043
valor2 = 23000085

GenQR.rango(valor1,valor2)
html = GenHTML(valor1, valor2)
GenHTML.crear(html)

ruta_template = './sources/temporal.html'
info = {}
crear_pdf(ruta_template,info,valor1,valor2)

