# encoding: utf-8
import math 
import pandas 

#Creacion de la matriz
def CreaMatriz(n):
	Matriz= [[0 for j in range(n)] for i in range(n)]
	return Matriz

#Algoritmo para la distancia Euclidiana			
def DistEU(M1, val):
	for i in range(len(val)-1):
		j = i+1
		while j > 0:   
			j-=1
			Dist = 0
			for k in range(len(val[0])):
				Dist += pow(val[j][k]-val[i+1][k],2)	
			M1[i+1][j] = round(math.sqrt(Dist),3)
				
#Lectura de datos
Datos = pandas.read_excel('WDBC-569.xlsx')

#Obtención de las columnas de tipo  flotante
ColumnasUtiles = [Datos.columns[i] for i in range(len(Datos.columns)) if Datos.dtypes[i] == 'float']  

#Obtención de los valores de las columnas
Valores = Datos[ColumnasUtiles].values

#Llamado de las funciones
M1 = CreaMatriz(len(Valores))
DistEU(M1, Valores)

