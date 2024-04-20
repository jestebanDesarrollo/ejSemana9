import pandas as pd

#Esto es un diccionario.

data = {'Nombre': ['Ana', 'Juan', 'Pedro', 'María', 'luis', 'Sofia', 'Carlos','Laura','Diego','Valentina','Andres'], 
        'Edad': [25, 30, 22, 27, 17, 22, 32, 68, 50, 58, 28], 
        'Ciudad': ['Medellín', 'Bogotá', 'Cali', 'Cartagena', 'Barbosa', 'Girardot', 'Copacabana', 'Santa Marta', 'Cucuta', 'San Andres', 'Medellín']}

df = pd.DataFrame(data)

#print(df.describe()) #Estadistica 
#print(df.max()) #Me dice la edad maxima del usuario en el diccionario
#print(df['Edad']>25) #Puedo usar filtros de esta forma muestra si es verdadero o false si un usuario es menor a o mayor
#print(df[df['Edad']>25]) #De esta forma de filtrar no me muestras los usuarios que son menos a 25
#print(df[~(df['Edad']>25)|(df['Nombre'] == 2)]) #De esta forma de filtrar no me muestras los usuarios que son menos a 25 IMPORTANTE ~ ES UN CARACTER DE NEGAR.

