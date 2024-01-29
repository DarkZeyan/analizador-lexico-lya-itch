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
def validarTokens(tokens, alfabeto, palabras_reservadas):
    counter = 0
    for token in tokens:
        if token in palabras_reservadas:
            counter=counter+1
        for caracter in token:
            if caracter not in alfabeto:
                print('Caracter incorrecto '+ caracter)
                return False
    if(counter==0):
        return False
    return True

# Abrir el archivo textoAnalizar.py y almacenar el valor
archivoAnalizar = open("textoAnalizar.py")

palabras_reservadas = ['synin', 'genji', 'goku', 'midas']

# Diccionario funciones
tokens = {'synin' : 'despliega', 'genji' : 'entrada', 'midas' : 'condicional', 'goku' : 'ciclo for', "'":[
    'inicio de cadena', 'fin de cadena'
]}
# Separamos solo las keys del diccionario
tokensKeys = tokens.keys()

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
    lexemas=linea.split(' ')
    sonTokensValidos = validarTokens(lexemas,alfabeto,palabras_reservadas)
    if sonTokensValidos == False:
        print('Se ha detectado un token invalido')
        break
    
    # Procesar las salidas del token synin
    str_salida = []
    for lexema in lexemas:
        if lexema == "'":
            numToken = lexemas.index(lexema)
            str_salida.append(lexemas[numToken+1:len(lexemas)-2])
            del lexemas[numToken+1:len(lexemas)-2]

    print("Los lexemas encontrados son: " , lexemas)

    print("Linea #", contador, "tokens individuales \n")
    # separamos los tokens individualmente y asignamos a qué grupo pertenecen
    for lexema in lexemas:
        if lexema=="'":
            continue
        if lexema in tokensKeys:            
            print("El lexema ", lexema, " es el token: ", tokens[lexema])
            if lexema=='synin':            
                print("El lexema ' es el token:  ", tokens["'"][0])
                print('El lexema ', ' '.join(str_salida[0]),' es el token CADENA DE TEXTO')
                print("El lexema ' es el token:  ", tokens["'"][1])
        if lexema in cierreKeys:
            print("El lexema ", lexema, " es el token: ", cierre[lexema])
    
    
    def procedimientoSynin(str_salida) :
        str_salida.remove([])
        str_salida = str_salida[0]
        str_salida = ' '.join(str_salida)
        print()
        print('Resultado: ', str_salida)
    def procedimientoGenji(): 
        print('Llamada a palabra reservada Genji, introduce tu variable o texto a desplegar')
        entrada = input()            
        print('Llamada a funcion genji realizada, el resultado de la llamada es: '+entrada)
    def procedimientoMidas():
        print('Llamada a palabra reservada Midas, introduce tus números a comparar')
        a = input()   
        b = input() 
        print('Introduce una condicion')
        condicion = input()
        if(condicion == '>'):
            print(a>b)
        elif(condicion == '<'):
            print(a<b)
        elif(condicion=='=='):
            print(a==b)
        elif(condicion=='!='):
            print(a!=b)
        elif(condicion=='<='):
            print(a<=b)
        elif(condicion=='>='):
            print(a>=b)
        else: print('Condicion invalida')

    #Se procesan las salidas de los tokens validos
    for lexema in lexemas:
        if lexema == 'synin':            
            procedimientoSynin(str_salida)
        if lexema == 'genji':
            procedimientoGenji()
        if lexema == 'midas':
            procedimientoMidas()
        if lexema.startswith('goku('):
            try:
                inicio, fin = map(int, lexema[lexema.find('(')+1:lexema.find(')')].split(','))
                print(inicio,fin)
                for i in range(inicio, fin + 1):
                    procedimientoGenji()
            except ValueError:
                    print('Error en la sintaxis de la llamada a Goku. Debe ser goku(inicio, fin)')


                        

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
    print()