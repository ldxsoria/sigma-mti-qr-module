from GenHTML import GenHTML
from GenQR import GenQR
from GenPDF import crear_pdf

def main(sticker, num_inicial, num_final):
    GenQR.rango(num_inicial,num_final)
    html = GenHTML(sticker,num_inicial, num_final)
    GenHTML.crear(html)

    ruta_template = './sources/temporal.html'
    info = {}
    crear_pdf(ruta_template,info,num_inicial,num_final)

start = 2300000 + 1
end = 2300000 + 252
# mini o estandar
sticker = 'mini'
#sticker = 'estandar'

#FUNCION PARA CREAR RANGOS PARES
if sticker == 'estandar':
    total = 42
else:
    total = 45 #faltaria estable maximo por hoja aqui


if sticker == 'estandar':
    rangos = [start]

    while start + total <= end:
        end_range = (start - 1) + total
        # print(end_range)
        start = end_range + 1
        # print(start)

        rangos.append(end_range)
        rangos.append(start)

    rangos.append(end)

    #CREAR PAGINA POR CADA RANGO
    total_rangos = int(len(rangos) / 2)
    # print(total_rangos)

    a = 0

    while a <= total_rangos + 2:
        print(a)
        inicio = rangos[a]
        fin = rangos[a+1]
        a +=2
        print(f"{inicio} - {fin}")
        main(sticker, inicio,fin)
else:
    print("generando mini qr")
    inicio = start
    print(inicio)
    fin = end   
    print(fin)
    main(sticker, inicio,fin)





