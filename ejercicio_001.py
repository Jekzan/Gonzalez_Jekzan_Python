AÑO_ACTUAL = 2022

#Primera Pregunta
print('1. ¿Cuál es tu nombre?')
name = input()

#Segunda pregunta
print('2. ¿Cuál es tu primer apellido?')
lastname1 = input()

#Tercera pregunta
print('3. ¿Cuál es tu segundo apellido?')
lastname2 = input()

#Cuarta pregunta
print('4. ¿En qué año naciste?')
year = input()

#Quinta pregunta
print('5. ¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
monthday = input()

fullname = name + ' ' + lastname1 + ' ' + lastname2

#A
fullnameu = fullname.upper()
print('A. Este es tu nombre completo en mayúsculas: ' + fullnameu)

#B
fullnamel = fullname.lower()
print('B. Este es tu nombre completo en minúsculas: ' + fullnamel)

#C
birthday = monthday[-2:] + '-' + monthday[0:2] + '-' + year
print('C. Esta es tu fecha de nacimiento: ' + birthday)

#D
age = AÑO_ACTUAL - int(year)
print(f'D. Esta es tu edad: {age}')

#E
vowels = set('aeiou')  
counter = 0
for c in fullnamel:
    if c in vowels:
        counter += 1
print(f'E. Tu nombre completo tiene: {counter} vocales.')

#F
nname = len(fullname.replace(' ',''))
print(f'F. Tu nombre completo tiene: {nname} letras.')

#G
isnum = isinstance(age,int)
print(f'G. ¿Tu edad es un carácter de tipo número?: {isnum}')

#H
isstr = isinstance(fullname,str)
print(f'H. ¿Tu nombre completo es un carácter de tipo alfanumérico?: {isstr}')

#I
future10 = age + 10
print(f'I. Tu edad en 10 años será: {future10}')

#J
future20 = age + 20
futurelist = [age,future20]
print(f'J. La media de tu edad actual y tu edad en 20 años es: {round((sum(futurelist)/len(futurelist)))}')