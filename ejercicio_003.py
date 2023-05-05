PASSWORD = 'facil123'

#Pedir contraseña
contra = input('Hola usuario, por favor ingresa la contraseña correspondiente: ')

while contra != PASSWORD:

    contra = input('Lo siento, la contraseña que has ingresado es incorrecta, por favor inténtalo de nuevo: ')

else:

    print('Gracias usuario, haz introducido la contraseña correcta, puedes continuar.')