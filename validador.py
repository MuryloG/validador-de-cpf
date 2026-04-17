while True:

    erro = False # Flag de erro caso o try cause erro

    lista_num = []

    cpf_input = input('Digite o seu CPF utilizando apenas números e sem pontuação: ')
    lista_cpf = list(cpf_input) # Separa cada caractere do CPF em um indice na lista

    print(lista_cpf)

    for i in lista_cpf:
        try:
            num = int(i)
            lista_num.append(num)
            
        except ValueError:
            print(f'O caractere {i} não é um número válido e foi ignorado')
            erro = True # Transforma a flag em verdadeira
            break

    if erro:
        continue # Reinicia o codigo

    nove_digitos = lista_num[:9]
    soma = 0
    mult = 10

    for i in nove_digitos:
        soma = soma + (i * mult)
        mult = mult -1
            
    resto_div = soma % 11

    if resto_div < 2:
        primeiro_digito = 0

    else:
        primeiro_digito = 11 - resto_div

    if primeiro_digito != lista_num[9]:
        print('CPF inválido')

    print(primeiro_digito)

