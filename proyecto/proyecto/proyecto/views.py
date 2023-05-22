from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

datos = {
    'nombres' : 'Levi Jekzan',
    'primer_apellido' : 'Gonzalez',
    'segundo_apellido' : 'Calderon',
    'fecha_nacimiento' : '07/01/1998',
    'celular' : '3314275923',
    'correo' : 'levi-jekzan.gonzalez@hpe.com',
    'domicilio' : 'Los arboles 24',
    'genero' : 'Masculino',
    'objetivo' : 'Volverme un experto en Python',
    'salario_esperado' : 50000
}


skills = ['SSMS','VBA','DAX','Powershell','Power Query','Python','Html']

trabajos = {
    'lugar_trabajo' : ['Hewlett Packard Enterprise','Caja Popular Colonias Unidas'],
    'ano_inicio' : [2021,2019],
    'ano_fin' : ['Indefinido','2020'],
    'puesto' : ['Data Analyst','Análista Financiero']
}


def index(request): #Siempre tengo un request que se debe definir.
    
    return HttpResponse('Directorio de Levi Gonzalez.')

#Index
class Inicio(View):
    template_name = 'index.html'
    
    def get(self,request):
        eleccion = 'Por favor elija la información que quiere ver:'
        datos = 'Datos Generales'
        skills = 'Skills'
        trabajos = 'Trabajos'
        #Aquí va todo el contenido del proyecto final
        return render(request, self.template_name,{
            'eleccion': eleccion, #hacer json
            'datos' : datos,
            'skills' : skills,
            'trabajos' : trabajos
        })
#Datos
class Datos(View):
    template_namedatos = 'datos.html'
    
    def get(self,request):
        datosp = 'Estos son los datos generales:'
        return render(request, self.template_namedatos,{
            'datosp': datosp,
            'datonombre' : datos['nombres'],
            'datoapellido' : datos['primer_apellido'],
            'datoapellido2' : datos['segundo_apellido'],
            'fechabirth' : datos['fecha_nacimiento'],
            'celular' : datos['celular'],
            'correo' : datos['correo'],
            'domicilio' : datos['domicilio'],
            'genero' : datos['genero'],
            'objetivo' : datos['genero'],
            'salario_esperado' : datos['salario_esperado']
        })
#Skills
class Skills(View):
    template_nameskills = 'skills.html'
    
    def get(self,request):
        skillsp = 'Estás son los skills:'
        return render(request, self.template_nameskills,{
            'skillsp': skillsp,
            'skill1' : skills[0],
            'skill2' : skills[1],
            'skill3' : skills[2],
            'skill4' : skills[3],
            'skill5' : skills[4],
            'skill6' : skills[5],
            'skill7' : skills[6],
        })
#Trabajos
class Trabajos(View):
    template_nametrabajos = 'trabajos.html'
    
    def get(self,request):
        trabajosp = 'Estos son los trabajos:'
        return render(request, self.template_nametrabajos,{
            'trabajosp': trabajosp,
            'lugar_trabajo1' : trabajos['lugar_trabajo'][0],
            'ano_inicio1' : trabajos['ano_inicio'][0],
            'ano_fin1' : trabajos['ano_fin'][0],
            'puesto1' : trabajos['puesto'][0],
            'lugar_trabajo2' : trabajos['lugar_trabajo'][1],
            'ano_inicio2' : trabajos['ano_inicio'][1],
            'ano_fin2' : trabajos['ano_fin'][1],
            'puesto2' : trabajos['puesto'][1]
        })
#Print Datos
print('---Datos---')
for k, v in datos.items():
    print(f'{k} : {v}')

#Print Skills
print('---Skills---')
for i in range(0, len(skills)):

     print(skills[i])

#Print Trabajos
print('---Trabajos---')
for k, v in trabajos.items():
    valor = (f'{k} : {v}').replace('[','').replace(']','').replace("'","")
    print(valor)