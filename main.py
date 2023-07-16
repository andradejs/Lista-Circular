from lista_circular import Lista_circula


lista = Lista_circula()


while True:

    print(10*'-')
    print('0- sair',)
    print('1- adcionar')
    print('2- remover')
    print(10*'-')

    escolha = int(input('escolha uma ação para a lista: '))
    if escolha == 1:
        escolha2 =  input('quer colocar varios elemento [s/n]: ')

        if escolha2 == 's':
            valores = input('coloque os valores separados por vírgula: ').split(',')
            for valor in valores:
                lista.adicionar(int(valor))
        else:        
            valor = int(input('valor: '))

            posicao = int(input('Posição da lista: '))
            lista.adicionar(valor, posicao)

    elif escolha == 2:
        valor = int(input('valor: '))
        lista.apagar(valor)
    elif escolha == 0:
        break
    lista.mostrar()


lista.tamanho()
lista.mostra()
