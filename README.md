#EJERCICIOS DE PYTHON
Ejercicios de Python realizados por **Nicolás Bosoni Spinetto**. V1.0.22 Desarrollados y Ejecutados en PyCharm 2021.2.3 (Edu) Build #PE-212.5457.63, built on October 21, 2021

La idea de este readme es recordar cómo percibí los ejercicios y pensé en las soluciones a medida que desarrollaba cursos y ejercicios.

## STRINGS
### Ejercicio 01 - hello_world.py
Defina una Función de bienvenida 'greet' y regrese el mensaje de 'Hello Wolrd' u Hola Mundo.

Ideas: Hay que entender que existe una diferencia entre Imprimir en Pantalla **print()** y entre regresaro algo o **return**. La segunda devuelve un argumento/variable/mensaje/objeto que genera la propia función
```python
def greet():
    return 'Hello World'

print(greet())
```
### Ejercicio 02 - palabra_rango_impar.py
Dado un String Determinado, debe entregar un mensaje al usuario indicando qué palabras pertenecientes a la frase son pares. No considere Validación de Datos, sin ingreso de usuario y sin funciones. 

**Ideas**:  Primero debemos definir nuestro string (st) con la frase que vamos a evaluar. Luego tenemos que de alguna forma acceder a cada una de las palabras, esto lo podemos hacer porque la variable es iterable (se puede recorrer); así que utilizaremos un for para buscar este contenido, y dividiremos el string con la función **split()**. Nótese la lectura y luego la construcción: 

>"Por cada Palabra del String dividido, evaluaremos su largo: si el residuo de ese número (del largo) es igual a 0, quiere decir que es PAR, entonces se imprime"
```python
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
   if len(word) % 2 == 0:
       print(word + ': su Largo es par')
```
### Ejercicio 03 - palabra_rango_impar_v2.py
Genere una Función esta vez que realice lo mismo qu el ejercicio anterior. Esta vez, el input debe ser ingresado por el usuario. Reglas: No haga validaciones, el usuario ingresará mínimo 2 palabras dentro de la frase.

**Ideas**: Ya sabemos qué y como pensar el contenido de la función. No utilizaremos Return, porque per-sé la función imprime el resultado. Entonces, sí tenemos que Generar el ingreso de datos por el usuario, para esto utilizaremos la función **input()** y debemos guardar en una variable el contenido. Luego esa variable se la pasamos a la función como un parámetro/argumento para que pueda ejecutar su código.

```python
def even_words(word):
    for word in st.split():
        if len(word) % 2 == 0:
            print(word + ': su Largo es par')


st = input('Ingrese una frase: ')
even_words(st)
```
### Ejercicio 04 - palabra_primera_letra.py
Genere una Función, que permita obtener la primera letra de una palabra ingresada por el usuario. No considere Validaciones el usuario siempre ingresará al menos un string.

**Ideas**: Ya sabemos crear una función, Sabemos solicitar un input al usuario y que debe ser almacenado en una variable para que la función luego pueda ejecutar. Al igual que lo anterior el elemento será iterable y por lo tanto lo recorreremos con un for, vamos a dividir el string por cada palabra y por cada una de esas palabras vamos a acceder a su primer elemento
>"Entregame la primera letra de cada palabra que está en el string dividido"
```python
def letras(word):
    lista = [word[0] for word in st.split()] #List Comprehension
    print(lista)

st = input('Ingrese una Frase: ')
letras(st)
```
### Ejercicio 05 - camel_case.py
El camel case es un juego conocido que nos sirve para aprender a dividir un string que nos entrega el usuario. No Considere Validaciones, el usuario entregará por lo menos siempre un string.
Utilice una Función que imprima el resultado por pantalla

**Ideas**:  Como hemos visto en otros ejercicios, le pedimos al usuario que ingrese un texto y lo almacenamos en una Variable, para entregarla como argumento de la función. Luego se define la función y generamos una lista o un iterable con las palabras divididas por la función **split()**. Ya sólo falta imprimirla en pantalla.

```python
def camel_case(text):
    words = text.split()
    print(words)

text  = input('write some Stuff: ')
camel_case(text)
```
### Ejercicio 06- palabra_empieza_con_s.py
Genere una función que pida al usuario alguna frase o palabras. Detecte aquellas que empiecen por S e imprimalas por pantalla, si ninguna comienza por s informelo por pantalla.

**Ideas**: La idea de ingreso y construcción de la función sigue siendo la misma para todo. Mediante la función **input()** recibimos un string que guardaremos en una variable y la entregaremos como argumento a la función que luego dividirá el texto.
La idea es recorrer el string dividido y preguntar por cada una de las palabras, en un mismo "formato" si su primer elemento es 's'; ¿Porqué en mismo formato? porque los Strings son 'Case Sensitive'. Con la función lower() nos aseguramos que todas las palabras al ser evaluadas, sea con una misma letra 's'. Digamos entonces que vamos a crear una lista y cada vez que una palabra empiece por 's' la contaremos, y además la agregamos a la nueva lista para mostrarlas. Contamos creando una variable de repetición que aumente en uno, y el método append() permite agregar la palabra a la lista. Finalmente sería un if..else para controlar el flujo de los prints cuando está vacío y cuando tiene contenido.


> Ojo: Estamos usando las herramientas aprendidas hasta ahora.

```python
def palabra(word):
    ls = []
    rep = 0
    for word in the_word.split():
        if word[0].lower() == 's':
            ls.append(word)
            rep += 1
    if rep == 0:
        print(f'No hay palabras que comiencen por S')
    else:
        print(f'Hay {rep} Palabras Seleccionadas:\n {ls}')

the_word = input('Ingrese una palabra o frase que empìece con "s" : ')
palabra(the_word)
```
### Ejercicio 07 - palabra_invertida.py
Defina una función para que el usuario ingrese una palabra; esta debe retornar dicha un string con la frase invertida. No utilice flujos de control ni validaciones.

**Ideas**: Creamos un input para el usuario y que se guarde en una variable, luego lo pasamos como argumento a la función 'master_yoda'. Dividimos el String y lo guardamos en una nueva lista. Regresamos de forma práctica  la palabra de forma invertida en un solo string.

```python
def master_yoda(word):
    # Genero una Nueva Lista con el método Split de mi palabra
    new_word = word.split()
    # Regreso un nuevo String unido por espacios con le método join, pero de forma inversa
    return new_word
    # return '.'.join(new_word[::-1])


the_word = input('Ingrese una Frase para separar: ')
r = master_yoda(the_word)
print(r)
```

### Ejercicio 08 - palabras_abreviadas.py
Dado un string de dos palabras, regrese como string la primera letra de cada palabra separada con un punto. No utilice input de usuario ni validaciones ni control de flujo

**Ideas**: El string dado está en una variable y lo pasamos a la función como argumento. Utilizando 
un iterable (en este caso la forma de List Comprehension) le pedimos que nos regrese en una nueva lista la primera letra de cada palabra del string dividido. Luego la función regresa la nueva lista como string (unida)
```python
def abrev_name(name):
    lista = [word[0] for word in name.split()]
    # return lista
    return '.'.join(lista).title()

name = 'Chaparrito GOnzales'
r = abrev_name(name)
print(r)
```
### Ejercicio 09 - buscar_palabra.py
Dada una lista, cree una función que regrese la posición del string 'needle'. Reglas: Siempre debe existir la palabra, no use control de flujo ni validaciones; utilice el método index()

**Ideas**:  Al igual que el ejercicio anterior, el String es dado. En este caso vamos a depender de un elemento iterable y la función index(). Además notese que index() nos retornará un integer, como vamos a concatenar un texto y el resultado, necesariamente debemos regresar es un string.

```python
def find_needle(mylist):
        return 'found the needle at position ' + str(mylist.index('needle'))


mylist = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
r = find_needle(mylist)
print(r)
```
