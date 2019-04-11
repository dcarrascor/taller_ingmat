import csv
import numpy

matrix=[]
with open('C:\Users\Daniel\Desktop\Random IPC\datos.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        matrix.append(row)
matrix[0][0]="DIA"
for i in range(1,61):
    for j in range(0,3):
        if j==0:
            matrix[i][j]="D"+str(matrix[i][j])
        elif j==1:
            matrix[i][j]="M"+str(matrix[i][j])
        else:
            matrix[i][j]="Y"+str(matrix[i][j])
with open('datos_legibles.csv', 'wb') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["PRODUCTO", "DIA", "MES", "YEAR", "VALOR"])
    for j in range(1, 304):
        nombre=matrix[0][2+j]
        for i in range (1,61):
            dia=matrix[i][0]
            mes=matrix[i][1]
            year=matrix[i][2]
            valor=matrix[i][j+2]
            fila=[nombre, dia, mes, year, valor]
            writer.writerow(fila)
csvFile.close()



