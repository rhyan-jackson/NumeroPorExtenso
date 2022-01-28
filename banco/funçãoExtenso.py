from time import sleep
from banco import *


def mostrarextenso(digito, printar=False):
    # Inserção do termo com verificação de flag de parada e se o digito está entre os intervalos especificados.
    digito = str(digito)
    if digito.isnumeric() and 0 <= int(digito) <= 999 and printar:
        print('\033[35mNúmero inserido com sucesso.\033[m')
        sleep(0.6)
    else:
        print('\033[31mERRO! Insira um número inteiro de 0 a 999 para mostrá-lo por extenso.\033[m')
        exit()
    # Limpeza de zeros e verificação do tamanho do número inserido (1, 2 ou 3 dígitos).
    digito = limparzeros(digito)
    tamanho = len(digito)
    extenso = 'NULL'
    if tamanho == 1:  # Se o tamanho for 1.
        extenso = unidade[digito]

    elif tamanho == 2:  # Se o tamanho for 2.
        extensoLista = []
        extenso = 'NULL'
        if digito[0] == '1' and digito[1] != '0':
            for nmr in onzeAoDezenove.keys():
                if nmr == digito:
                    extenso = onzeAoDezenove[digito]
        else:
            for nmr in dezena.keys():
                if nmr[0] == digito[0]:
                    extensoLista.append(dezena[nmr])
            if digito[1] != '0':
                for nmr in unidade.keys():
                    if nmr == digito[1]:
                        extensoLista.append((unidade[nmr]))
                extenso = ' e '.join(extensoLista)

            else:
                extenso = extensoLista[0]

    elif tamanho == 3:  # Se o tamanho for 3.
        extensoLista = []
        if digito == '100':  # Tratei o 100 separadamente pois a palavra 'cem' só se encontra neste número.
            extensoLista = 'cem'

        else:  # Nesse else utilizo das posições dos números das strings para adicionar na lista os nomes.
            for nmr in centenas.keys():
                if digito[0] == nmr[0]:
                    extensoLista.append(centenas[nmr])
            for nmr in dezena.keys():
                if digito[1] == nmr[0]:
                    extensoLista.append(dezena[nmr])
            for nmr in unidade.keys():
                if digito[2] == nmr and digito[2] != '0':
                    extensoLista.append((unidade[nmr]))

        extenso = ' e '.join(extensoLista)  # Aqui é feita a junção das palavras na lista.

    # Print de tudo e 'final' do programa principal.
    if printar:
        print(f'\033[36;40mO número indicado tem {tamanho} dígitos\033[m'
              if tamanho != 1 else f'O número indicado tem 1 dígito.\033[m')
        print(f'\033[35mEle por extenso é ➤ \033[34m{extenso}.\033[m')
        print('―' * 40)
    else:
        return extenso
