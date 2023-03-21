""""
repetiçao
while(equanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito - > quando um codigo nao tem fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou')

