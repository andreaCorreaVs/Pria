#Cria string e escreve em tela
palavra="Python"
print(palavra)
#Calcula tamanho
print('Tamanho: %d' % len(palavra))
#Converte string para Lista
minha_lista=list(palavra)
print(minha_lista)
print('Primeira letra da palavra: %c' % minha_lista[0])
print('Última letra da palavra: %c' % minha_lista[-1])


listaRev = []

palabra = str(input('Ingrese una frase: '))
lista = list(palabra)
for i in reversed(lista):
    listaRev.append(i)

print(''.join(listaRev))



