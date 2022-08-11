"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def esPrimo(n):
  if n == 0 or n ==4:
   return False
  for i in range(2, int(n/2)):
      if n % i == 0:
        return False
  return True

for num in range(10):
  if esPrimo(num):
    print(num)

