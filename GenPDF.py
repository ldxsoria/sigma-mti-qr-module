#By https://www.youtube.com/watch?v=9XKlnD11lAA
from re import A, S
import jinja2
import pdfkit

def crear_pdf(ruta_template,info,num_start,num_end,rutacss='./sources/estilo.css'):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')
    nombre_pdf = f'{num_start}-{num_end}'

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)
    # print(html)

    options = { 
                'enable-local-file-access': True,
                'page-size': 'A4',
                'margin-top': '0.5in',
                'margin-right': '0.5in',
                'margin-bottom': '0.5in',
                'margin-left': '0.5in',
                'encoding': 'UTF-8'}

    config = pdfkit.configuration(wkhtmltopdf='./wkhtmltopdf/bin/wkhtmltopdf.exe')
    ruta_salida = f'./result/{nombre_pdf}.pdf'
    pdfkit.from_string(html,ruta_salida,css=rutacss,options=options,configuration=config)#Este hace todo


if __name__ == '__main__':
    ruta_template = './sources/temporal.html'
    info = {}
    crear_pdf(ruta_template,info)





