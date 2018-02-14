#! /usr/bin/python3

# Calculate the product of the first 100.000 numbers
import time

def calcProd():   
   product = 1
   for i in range(1, 100000):
       product = product *i
   return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The resulsts is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate,' % (endTime - startTime))

