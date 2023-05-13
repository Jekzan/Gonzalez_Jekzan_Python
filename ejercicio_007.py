#Frase, palabras y longitud
frase = input('Por favor introduzca una frase: ')

frasesplit = {
    
    'separacion':frase.split()
}

for palabra in frasesplit['separacion']:
    
    print(f'La palabra es {palabra}, y su longitud es de {len(palabra)}.')