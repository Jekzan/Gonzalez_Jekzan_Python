AÑO_ACTUAL = 2022

#Primera Pregunta
print('¿Cuál es tu nombre?')
name = input()

#Segunda pregunta
print('¿Cuál es tu primer apellido?')
lastname1 = input()

#Tercera pregunta
print('¿Cuál es tu segundo apellido?')
lastname2 = input()

#Cuarta pregunta
print('¿En qué año naciste?')
year = input()

#Quinta pregunta
print('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
monthday = input()

fullname = name + ' ' + lastname1 + ' ' + lastname2

#A
fullnameu = fullname.upper()
print('Este es tu nombre completo en mayúsculas: ' + fullnameu)

#B
fullnamel = fullname.lower()
print('Este es tu nombre completo en minúsculas: ' + fullnamel)

#C
birthday = monthday[-2:] + '-' + monthday[0:2] + '-' + year
print('Esta es tu fecha de nacimiento: ' + birthday)

#D
age = AÑO_ACTUAL - int(year)
print('Esta es tu edad: ' + str(age))

#E
vowels = len([i for i in fullnamel if i in 'aeiou'])
print('Tu nombre completo tiene: ' + str(vowels) + ' vocales.')

#F
nname = len(fullname)
print('Tu nombre completo tiene: ' + str(nname) + ' letras.')

#G
isnum = isinstance(age,int)
print('¿Tu edad es un carácter de tipo número?: ' + str(isnum))

#H
isstr = isinstance(fullname,str)
print('¿Tu nombre completo es un carácter de tipo alfanumérico?: ' + str(isstr))

#I
future10 = age + 10
print('Tu edad en 10 años será: ' + str(future10))

#J
future20 = age + 20
futurelist = [age,future20]
print('La media de tu edad actual y tu edad en 20 años es: ' + str(round((sum(futurelist)/len(futurelist)))))