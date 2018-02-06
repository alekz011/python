#! /usr/bin/python3
import logging
logging.basicConfig(filename='error.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
   logging.debug('Start of factorial(%s%%)' % (n))
   logging.disable(logging.DEBUG)
   total = 1
   #for i in range(1, n + 1):
   for i in range( n + 1):
      total *= i
      logging.debug('i is ' + str(i) + ', total is ' + str(total))
   return total
   logging.debug('End of factorial(%s%%)' % (n))

print(factorial(5))
logging.debug('End of program')

