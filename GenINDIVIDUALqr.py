import qrcode
import os

class GenQR:
    def __init__(self, url: str, nombre_imagen: str):
        self.url = url
        self.nombre_imagen = nombre_imagen
        self.imagen = qrcode.make(self.url)
        self.ruta_carpeta = './individual/'
        self.ruta_imagen = os.path.join(self.ruta_carpeta, f'{self.nombre_imagen}.png')

        # Crear la carpeta si no existe
        os.makedirs(self.ruta_carpeta, exist_ok=True)

        # Guardar la imagen QR
        with open(self.ruta_imagen, 'wb') as archivo_imagen:
            self.imagen.save(archivo_imagen)

    def __str__(self):
        return f'Código QR guardado en: {self.ruta_imagen}'

if __name__ == '__main__':
    url = input('Ingresa la URL > ')
    nombre_imagen = input('Ingresa el nombre de la imagen (sin extensión) > ')
    qr = GenQR(url, nombre_imagen)
    print(qr)

#funciona