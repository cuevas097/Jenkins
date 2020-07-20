# Cuevas Salgado Carlos
# Mineria de Datos
import math 
import pandas 

#Creacion de la matriz
def CreaMatriz(n):
	Matriz= [[0 for j in range(n)] for i in range(n)]
	return Matriz

#Imprimir la Matriz
def MuestraMatriz(M1):
	for i in range(len(M1)):
		print('\n',i+1,"||", end=" ")
		for j in range(len(M1[i])):
			if M1[i][j] != 0.00:
				print(M1[i][j], end=' ')
	print()

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
MuestraMatriz(M1)

f = open ('Matriz.txt','w')
f.write(str(M1))
f.close()