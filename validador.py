import os

while True:

    erro = False # Flag de erro caso o try cause erro

    lista_num = []

    cpf_input = input('Digite o seu CPF utilizando apenas números e sem pontuação: ')
    lista_cpf = list(cpf_input) # Separa cada caractere do CPF em um indice na lista

    for i in lista_cpf:
        try:
            num = int(i)
            lista_num.append(num)
            # Transforma os caracteres do CPF digitado em int
            
        except ValueError:
            print(f'\nO caractere "{i}" não é um número válido e foi ignorado\n')
            erro = True # Transforma a flag em verdadeira
            break

    if erro:
        continue # Reinicia o codigo

    # O bloco abaixo realiza o calculo para validar o primeiro digito
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
        print('\nCPF inválido!\n')
        continue

    # O bloco abaixo realiza o calculo para validar o segundo digito
    dez_digitos = lista_num[:10]
    mult = 11
    soma = 0

    for i in dez_digitos:
        soma = soma + (i * mult)
        mult = mult -1

    resto_div = soma % 11

    if resto_div < 2:
        segundo_digito = 0

    else:
        segundo_digito = 11 - resto_div

    if segundo_digito != lista_num[10]:
        print('\nCPF inválido! \n')
        continue

    else:
        loop = input(f'\nO CPF {cpf_input} É VÁLIDO!\n\nGostaria de validar outro CPF (S/N/Sim/Não)?\n').upper()[0]

        os.system('cls' if os.name == 'nt' else 'clear')

        if loop == 'S':
            continue

        else:
            print('Programa encerrado!')
            break