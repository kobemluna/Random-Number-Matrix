#Kobe Luna
#Student ID: P21590963
#Problem 1

import numpy as np 
Array1 = np.random.randint(0,11, size=(3,3))
Array2 = np.random.randint(0,11, size=(3,3))

OddValues = (Array1%2 == 1)
Array1[OddValues] = 1

EvenValues = (Array2%2 == 0)
Array2[EvenValues] = 2

print(Array1)
print("\n")
print(Array2)
print("\n")

Matrix = np.dot(Array1,Array2)
print(Matrix)

