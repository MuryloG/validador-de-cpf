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
            

    print(lista_num)

