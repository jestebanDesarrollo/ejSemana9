import pandas as pd

#Esto es un diccionario.

data = {'Nombre': ['Ana', 'Juan', 'Pedro', 'María', 'luis', 'Sofia', 'Carlos','Laura','Diego','Valentina','Andres'], 
        'Edad': [25, 30, 22, 27, 17, 22, 32, 68, 50, 58, 28], 
        'Ciudad': ['Medellín', 'Bogotá', 'Cali', 'Cartagena', 'Barbosa', 'Girardot', 'Copacabana', 'Santa Marta', 'Cucuta', 'San Andres', 'Medellín'],
        'Articulo':['Balon de futbol', 'Zp Tennis Deportivos', 'Zap Guayos','Medias Largas', 'Espinilleras', 'C de Nacional', 'C de Medellin','C de Millonarios','Zp Guayos','Cordones', 'CB Colombia'],
        'Precio':[220.000, 180.000, 150.000, 30.000, 25.000, 120.000, 120.000, 120.000, 190.000, 10.000, 150.000]}

df = pd.DataFrame(data)

#print(df.describe()) #Estadistica 
#print(df.max()) #Me dice la edad maxima del usuario en el diccionario
#print(df['Edad']>25) #Puedo usar filtros de esta forma muestra si es verdadero o false si un usuario es menor a o mayor
#print(df[df['Edad']>25]) #De esta forma de filtrar no me muestras los usuarios que son menos a 25
#print(df[~(df['Edad']>25)|(df['Nombre'] == 2)]) #De esta forma de filtrar no me muestras los usuarios que son menos a 25 IMPORTANTE ~ ES UN CARACTER DE NEGAR.
print(df.sort_values(['Edad']) )
print(df.max(['Precio']))



