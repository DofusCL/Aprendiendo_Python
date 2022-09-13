import  urllib.request
import numpy
from bs4 import BeautifulSoup

# Defino la Web y hago el request para recibir el código
web = "http://ramco.cl/"
datos = urllib.request.urlopen(web).read().decode()

# muestro los datos iniciales
## print(datos)

# Creo una SOUP con la web en formato bonito y legible y extraigo la etiqueta que me intersa
soup = BeautifulSoup(datos)
links = soup('a')

# Defino que sean datos únicos para esas etiquetas por segmento
ulinks = set(links)

#imprimo cada path de la lista de urls que obtuvimos
for path in ulinks:
    if path != '':
        ## print(numpy.unique(path.get('href')))
        print(path.get('href'))