#Área de un circulo
PI = 3.141592653589793
radio = float(input('Introduzca el radio del circulo: '))

area = (radio**2) * PI
print(f'El área del circulo proporcionado es de {round(area,2)}.')

#Calcular volumen de un cilindro
pregunta1 = input('Desea calcular el volumen del cilindro (si o no): ')

while pregunta1 != 'si' and pregunta1 != 'no':

    pregunta1 = input('La opción seleccionada no es correcta, inténtenlo de nuevo: ')

else:    

        if pregunta1 == 'si':
            altura = float(input('Por favor introduzca la altura del cilindro: '))
            volumen = round((area * altura),2)
            print(f'El volumen del cilindro es de {volumen}.')
        elif pregunta1 == 'no':
            print('Gracias, sesión terminada.')
