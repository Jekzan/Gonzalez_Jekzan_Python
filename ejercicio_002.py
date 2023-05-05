ANTES_M = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
DESPUES_N = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

#Preguntar Nombre
nombre = input('Por favor escribe tú primer nombre (único nombre): ')

#Preguntar sexo
sexo = str(input('Por favor escribe tú sexo (H/M): '))

#Resultado

if nombre.isalpha() and sexo in ['H','M']:

        if (nombre.lower()[0] in ANTES_M and sexo == 'M') or (nombre.lower()[0] in DESPUES_N and sexo == 'H'):
                print(f'Hola {nombre} con sexo "{sexo}", eres parte del grupo A.')
        else:
                print(f'Hola {nombre} con sexo "{sexo}", eres parte del grupo B.')
else:
        print('Has introducido valores erróneos. Por favor lee las instruncciones de cada sección e inténtalo otra vez.')