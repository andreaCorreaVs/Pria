"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

for i in range(10):
    print(rec_fib(i))
