# Declaramos el alfabeto de nuestro lenguaje
simbolos  = {
        'letras': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'numeros': '0123456789',
    'espacios': ' \t\n\r\x0b\x0c',
    'simbolos': r"""!#$%&()*+,-./:;<=>?@[\]^_`{|}~'"""
}

alfabeto = (
    simbolos['letras'] + simbolos['numeros'] + simbolos['espacios'] + simbolos['simbolos']
)

# Funcion para analizar tokens o lexemas validos.
def validarTokens(tokens, alfabeto):
    for token in tokens:
        for caracter in token:
            if caracter not in alfabeto:
                print('Caracter incorrecto '+ caracter)
                return False
    return True

# Abrir el archivo textoAnalizar.py y almacenar el valor
archivoAnalizar = open("textoAnalizar.py")

# Diccionario funciones
funciones = {'synin' : 'despliega', 'genji' : 'entrada'}
# Separamos solo las keys del diccionario
funcionesKeys = funciones.keys()

# Diccionario cierre
cierre = {'atreus' : 'cierre'}
# Separamos solo las keys del diccionario
cierreKeys = cierre.keys()

contador = 0
lectura = archivoAnalizar.read()

programa = lectura.split("\n")
# indica la línea en la que se encuentra
for linea in programa:
    contador += 1
    print("Linea #" , contador, "\n " , linea)

    # separar los tokens por línea
    tokens=linea.split(' ')
    sonTokensValidos = validarTokens(tokens,alfabeto)
    if sonTokensValidos == False:
        print('Se ha detectado un token invalido')
        break
    
    # Procesar las salidas del token synin
    str_salida = []
    for token in tokens:
        if token == "'":
            numToken = tokens.index(token)
            str_salida.append(tokens[numToken+1:len(tokens)-2])
            del tokens[numToken+1:len(tokens)-2]

    print("Los tokens son: " , tokens)

    print("Linea #", contador, "tokens individuales \n")
    # separamos los tokens individualmente y asignamos a qué grupo pertenecen
    for token in tokens:
        if token in funcionesKeys:
            print("La funcion ", token, " es: ", funciones[token])
        if token in cierreKeys:
            print("La palabra ", token, " es: ", cierre[token])
    
    #Se procesan las salidas de los tokens validos
    for token in tokens:
        if token == 'synin':            
            str_salida.remove([])
            str_salida = str_salida[0]
            str_salida = ' '.join(str_salida)
            print()
            print('Resultado: ', str_salida)
        if token == 'genji':
            print('Llamada a palabra reservada Genji, introduce tu variable o texto a desplegar')
            entrada = input()            
            print('Llamada a funcion genji realizada, el resultado de la llamada es: '+entrada)

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
    print()