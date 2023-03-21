""""
repetiçao
while(equanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito - > quando um codigo nao tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Nao vou mostar 0', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')