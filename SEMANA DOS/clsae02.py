#!/usr/bin/python
# METODOS
'''
Se ensenara algunos formateos en cadena como

\t para tabs
\n para saltos de linea
y \' \" para comillas simples y dobles en cadenas

'''

#METODOS EN CADENA

"""
mayusuculas -> upper()
minusculas -> lower()
primera letra en mayuscula -> capitalize()
TODAS LA PRIMERA LETRA SERA EN MAYUSUCLA -> title()
reemplazar una cadena -> replace('old', 'new')
contar cuantas veces aparece una cadena -> count('cadena')
quitar espacio en blanco al principio y al final -> strip()
"""

#COMO HACER FORMATEOS AL IMPRIMIR

"""
f"cadena {variable}" -> f"cadena {variable}"
https://www.w3schools.com/python/ref_string_format.asp
" cadena {} ".format(variable)
" cadena {0} y {1}".format(variable)
" cadena {variable} ".format(variable=variable)
f-strings son más rápidos y fáciles de leer cuando usas Python 3.6 o superior.
.format() es útil si estás en versiones antiguas de Python o si prefieres un enfoque más explícito para referenciar variables.
"""

#TIPOS DE DATOS EN PYTHON Y SUS DEFINICIONES Y CONVERSIONES
'''
int -> entero
float -> decimal
str -> cadena
bool -> booleano
ESTRUCTURA DE DATOS
list -> lista
tuple -> tupla
dict -> diccionario
set -> conjunto
TIPOS DE DATOS CARACTERISTICOS DE PYTHON
None -> nulo
range -> rango
complex -> complejo
byte -> byte
bytearray -> arreglo de bytes
memoryview -> vista de memoria
'''

#EXPLCIACION DE BOOLEAN
"""
True -> verdadero
False -> falso

para que sirve?
para hacer comparaciones
y para hacer condicionales
por ejemplo

"""


#METODOS DE COMPPROBACION DE CADENA
"""
isalnum() -> si es alfanumerico
isalpha() -> si es alfabetico
isdecimal() -> si es decimal
isdigit() -> si es digito
isidentifier() -> si es identificador
islower() -> si esta en minusculas
isupper() -> si esta en mayusculas
isspace() -> si es espacio
istitle() -> si es titulo
iscapitalize() -> si esta capitalizado


"""

#ESTRUCTURA DE IF, ELSE y ELIF

"""
if -> si
else -> sino
elif -> sino si

ejemplo de uso
if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo

"""

#ESTRUCTURA DE MATCH CASE

"""
match case -> caso de coincidencia
se usa para hacer comparaciones de una manera mas eficiente
como un switch case en otros lenguajes
pero solo admite valores constantes
osea no se puede hacer comparaciones con variables
estructura
match variable:
    case valor:
        codigo
    case valor:
        codigo
    default:
        codigo

diferencia con if
if -> se usa para comparaciones mas complejas
match case -> se usa para comparaciones mas simples

"""

#FUNCION LEN

"""
len() -> longitud
se usa para saber la longitud de una cadena o una lista
"""

# OPERADORES LOGICOS

"""
and -> y
or -> o
not -> no

jerarquia de operadores
1. ()
2. **
3. *, /, //, %
4. +, -
5. <, >, <=, >=, !=, ==
6. not
7. and
8. or


JERARQUIA DE OPERADORES LOGICOS
1. not
2. and
3. or
"""

print(5 > 6 or 4 < 6 )
