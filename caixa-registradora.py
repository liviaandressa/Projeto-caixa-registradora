
def clear():
    print("\n" * 40)
def linha():
    print("{:-^60}".format('-'))

while True:
    print("\033[7;34m{: ^60}\033[m".format(' '))
    print("\033[7;34m{: ^60}\033[m".format('MERCADINHO DA ESQUINA'))
    print("\033[7;34m{: ^60}\033[m".format(' '))
    linha()
    print('DIGITE 0 PARA CONCLUIR AS COMPRAS E REALIZAR O PAGAMENTO')
    linha()
    total = 0
    quantidade_produtos = 1

# Cabeçalho da Loja

    while True:
        preço = float(input('Produto [{}]: R$'.format(quantidade_produtos)))
        quantidade_produtos += 1
        total += preço
        if preço == 0:
            break

# Total dos preços
    linha()
    print('\033[30;42mTotal das compras: R${:.2f}\033[m'.format(total))
    print("\n" * 1)

# Meneu de pagamentos
    print("\033[7;34m{: ^60}\033[m".format(' '))
    print("\033[7;34m{: ^60}\033[m".format('MENU DE PAGAMENTO'))
    print("\033[7;34m{: ^60}\033[m".format(' '))
    linha()
    print('''[1] - Pagamento à vista: Dinheiro
[2] - Pagamento à vista: Cartão
[3] - Parcelar em 2x no cartão: 5% de Juros
[4] - Parcelar em 3x ou mais no cartão: 10% de Juros''')
    linha()
    forma_pagamento = int(input('Digite a forma de pagamento: '))


# Primeira verificação de pagamento
    if forma_pagamento == 1:
        dinheiro = float(input('Dinheiro: R$'))
        troco = dinheiro - total
        if dinheiro > total:
            print('Troco: R${:.2f}'.format(troco))
            print('\033[30;42mCompra finalizada com sucesso! Volte Sempre!\033[m')
        elif dinheiro < total:
            print('Desculpe mas seu dinheiro é menor que o total da compra')
        elif dinheiro == total:
            print('O dinheiro é igual ao total, neste caso não tem troco.')
            print('\033[30;42mCompra finalizada com sucesso! Volte Sempre!\033[m')

# Segunda verificação de pagamento
    elif forma_pagamento == 2:
        print('\033[30;42mCompra finalizada com sucesso! Volte Sempre!\033[m')

# Terceira verificação de pagamento
    elif forma_pagamento == 3:
        juros = total + (total * 5 / 100)
        print('\033[34mSua compra será parcelada em 2x de R${:.2f} com 5% de juros'.format(juros / 2))
        print('No final sua compra custará R${}\033[m'.format(juros))
        print("\n" * 1)
        print('\033[30;42mCompra finalizada com sucesso! Volte Sempre!\033[m')

# Quarta verificação de pagamento
    elif forma_pagamento == 4:
        parcelas = int(input('Deseja dividir em quantas arcelas? '))
        juros = total + (total * 10 / 100)
        print('\033[34mSua compra será parcelada em {}x de R${:.2f} com 10% de juros'.format(parcelas, juros / parcelas))
        print('No final sua compra custará R${}\033[m'.format(juros))
        print("\n" * 1)
        print('\033[30;42mCompra finalizada com sucesso! Volte Sempre!\033[m')

# Verificação para valores inválidos
    else:
        print('\033[30;41mValor digitado inválido!\033[m')

# Cancelar operação ou reiniciar
    linha()
    reiniciar = int(input("Pressione 0 para reiniciar, 1 para encerrar: "))
    if reiniciar == 0:
        clear()
        continue
    else:
        clear()
        print("Encerrando caixa...")
        break
