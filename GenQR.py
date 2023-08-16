import qrcode
from PIL import Image

class GenQR():

    def __init__(self, numero=int):
        self.numero = numero
        self.imagen = qrcode.make(self.numero)
        self.nombre_imagen = f'{self.numero}.png'
        self.ruta_imagen = f'./sources/{self.nombre_imagen}'

        #archivo_imagen = open (f'./sources/{self.nombre_imagen}','wb')
        archivo_imagen = open(self.ruta_imagen, 'wb')
        self.imagen.save(archivo_imagen)
        archivo_imagen.close()

    def rango(valor1, valor2):
        for valor in range (valor1,valor2+1):
            GenQR(valor)

    def __str__(self):
        return f'{self.ruta_imagen}'

if __name__ == '__main__':
    codigo1 = GenQR(10)
    codigo1 = GenQR(11)
    codigo1 = GenQR(12)
    print(codigo1)
    a = 50
    b = 60
    GenQR.rango(50,60)


"""
    #Abrir imagen
    #ruta_imagen = './'+nombre_imagen
    #Image.open(ruta_imagen).show()
"""