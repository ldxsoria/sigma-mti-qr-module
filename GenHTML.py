import os
class GenHTML():

    def __init__(self, num_inicial, num_final=''):
        self.num_inicial = num_inicial
        self.num_final = num_final
        if self.num_final == '':
            self.tipo = 'unitario'
        else:
            self.tipo = 'lista'
        self.lista_codigos = []
        self.html_original = '<head><link rel="stylesheet" href="estilo.css"></head><body><div class="sticker-container"><table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr> <tr><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td></tr><tr><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td>29</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td></tr><tr><td>36</td><td>37</td><td>38</td><td>39</td><td>40</td><td>41</td><td>42</td></tr></table></div></body>'

    def generarLista(self):
        if self.tipo == 'lista' :
            for x in range(self.num_inicial, self.num_final+1):
                self.lista_codigos.append(x)
            return self.lista_codigos
        else:
            self.lista_codigos.append(self.num_inicial)
            return self.lista_codigos

    def generarDiv(self, codigo):
        reemplazar = codigo
        div = f'<td><div class="sticker"><div class="titulo">INVENTARIO ACTIVO FIJO 2023</div><div class="qr"><img src="file:///D:/Scripts/modulo_qr/sources/{reemplazar}.png" alt=""/></div><div class="codigo"><p>{reemplazar}</p></div><div class="colegio"><div class="logo"></div><div class="nombre"><p>San José Maristas</p></div></div><div class="pie"><p>SIGMA MTI</p></div></div></td>'
        return div

    def editarTD(self, numero_td, codigos_a_generar):
        td = numero_td
        codigo = codigos_a_generar
        valores = [f"<td>{td}</td>",f"{self.generarDiv(codigo)}"]
        self.html_original = self.html_original.replace(valores[0],valores[1])
        return f'{self.html_original}'

    def eliminar(self):
        pass

    def crear(self):
        contador_ediciones = 0
        datos = self.generarLista()
        for dato in datos:
            contador_ediciones += 1
            self.editarTD(contador_ediciones, dato)
        #Generar el archivo
        hoja_html = open("./sources/temporal.html", "w",encoding='utf-8')
        hoja_html.write(f'{self.html_original}')
        hoja_html.close()


    def __str__(self):
        contador_ediciones = 0
        datos = self.generarLista()
        for dato in datos:
            contador_ediciones += 1
            self.editarTD(contador_ediciones, dato)
        #Generar el archivo
        hoja_html = open("./sources/temporal.html", "w",encoding='utf-8')
        hoja_html.write(f'{self.html_original}')
        hoja_html.close()
        #Reporte de lo generado en consola
        return f'{self.html_original}'

if __name__ == '__main__':
    lista1 = GenHTML(10,12)
    print(lista1)
