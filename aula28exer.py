nome = input('Digite seu nome: ')



print(f'seu nome é {nome}')
print(f'seu nome invertido é {nome[-1:-10:-1]}')

if " " in nome: 
    print("Seu nome contem espaços")
else:
    print("Seu nome não contém espaços")

print(f'seu nome tem {len(nome)} letras')

print(f'A primeira letra do seu nome é {nome[0]}')
#print(f'A primeira letra do seu nome é {nome[:1:]}')
print(f'A ultima letra do seu nome é {nome[-1]}')
#print(f'A ultima letra do seu nome é {nome[5::]}')