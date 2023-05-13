#Frutería
fruteria = {
    'frutas' : ['Plátano','Manzana','Pera','Naranja'],
    'precios' : [1.35,0.80,.85,.70]
}

frutae = input('Qué fruta necesita: ')


if frutae in fruteria['frutas']:
    
    kilos = float(input('Cúantos kilos necesita: '))

    i = 0
    while frutae != fruteria['frutas'][i]:
        i += 1

    #print(fruteria['frutas'][i])
    #print(fruteria['precios'][i])
    preciototal = kilos * fruteria['precios'][i]
    print(f'El precio a pagar por la fruta será de {round(preciototal,2)} pesos.')

else:

    print('La fruta elegida no esta disponible (por favor escribe el nombre con los acentos correspondientes).')