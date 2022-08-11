"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def isAnagram(str1,str2):
    str1_s = sorted(str1)
    str2_s = sorted(str2)
    if str1_s == str2_s:
        print("Es un anagrama")
    else:
        print("No es un anagrama")


a = "amparo"
b = "paramo"
isAnagram(a,b)
