def limparzeros(string):
    dig = int(string)
    final = str(dig)
    return final

def boasvindas():
    print('\033[34mOlá!, seja bem-vindo ao meu programa.')
    print('\033[36mEle serve para mostrar qualquer número de 0 a 999 por extenso.')
    print('\033[34mUtilize com sabedoria.')
    print('\033[36mAh, quase me esqueci, digite 1000 para parar de digitar números.')


unidade = {
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove'
}

dezena = {
    '10': 'dez',
    '20': 'vinte',
    '30': 'trinta',
    '40': 'quarenta',
    '50': 'cinquenta',
    '60': 'sessenta',
    '70': 'setenta',
    '80': 'oitenta',
    '90': 'noventa'
}

onzeAoDezenove = {
    '11': 'onze',
    '12': 'doze',
    '13': 'treze',
    '14': 'quatorze',
    '15': 'quinze',
    '16': 'dezesseis',
    '17': 'dezessete',
    '18': 'dezoito',
    '19': 'dezenove'
}
centenas = {
    '100': 'cento',
    '200': 'duzentos',
    '300': 'trezentos',
    '400': 'quatrocentos',
    '500': 'quinhetos',
    '600': 'seiscentos',
    '700': 'setecentos',
    '800': 'oitocentos',
    '900': 'novecentos'
}