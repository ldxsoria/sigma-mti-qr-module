from GenHTML import GenHTML
from GenQR import GenQR
from GenPDF import crear_pdf

def main(num_inicial, num_final):
    GenQR.rango(num_inicial,num_final)
    html = GenHTML(num_inicial, num_final)
    GenHTML.crear(html)

    ruta_template = './sources/temporal.html'
    info = {}
    crear_pdf(ruta_template,info,num_inicial,num_final)

start = 1
end = 212

valor1 = 2300000 + start
valor2 = 2300000 + end


#FUNCION PARA CREAR RANGOS PARES
total = 42
rangos = [start]

while start + total <= end:
    end_range = (start - 1) + total
    print(end_range)
    start = end_range + 1
    print(start)

    rangos.append(end_range)
    rangos.append(start)

rangos.append(end)

# print("La lista resultante es:", rangos)

#CREAR PAGINA POR CADA RANGO
total_rangos = int(len(rangos) / 2)
# print(total_rangos)

a = 0

while a <= total_rangos:
    inicio = rangos[a]
    fin = rangos[a+1]
    a +=2
    print(f"{inicio} - {fin}")
    main(inicio,fin)






