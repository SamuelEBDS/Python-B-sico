numero_str = input (
        'Vou dobrar o numero que vc digitar: '
)

try: 
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('isso nao é um numero')