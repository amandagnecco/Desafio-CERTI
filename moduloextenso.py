#transformar números de algarismo para extenso
#unidades
ext_u = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
#Dezenas irregulares - dez a dezenove
ext_u_ir = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
#dezenas regulares
ext_d = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
#centenas
ext_c = ('', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')
def funcextenso(n):
#    n = extenso
    lista = list()
    numeroextenso = list()
    if n < -100000 or n > 100000:#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        numeroextenso.append('Você não digitou um número entre -99,999 e 99,999. Tente novamente!')
    if n > -100000 and n < 100000:
        if n == 0:
            numeroextenso.append('zero')
        if n < 0:
            numeroextenso.append('menos')
            n = n * -1
        for cont in range (0,5):
            isolado = n % 10
            n = n // 10
            lista.insert(0, isolado)
        for r in range (0,5):
            if r == 0 and lista[0] > 1:#dezena de milhar regular
                numeroextenso.append(ext_d[lista[r]])
            if r ==1:
                if  lista[0] == 1:#dezena de milhar irregular
                    numeroextenso.append(ext_u_ir[lista[r]])
                elif lista[1] > 0:#milhar
                    if lista[0] > 1:
                        numeroextenso.append('e')#!!!!
                    numeroextenso.append(ext_u[lista[r]])
                if lista[0] or lista[1] > 0:
                    numeroextenso.append('mil')
            if r == 2 and lista[2] > 0:#centena
                if lista[1] > 0 or lista[0] > 0:
                    numeroextenso.append('e')
                if lista[3] == lista[4] == 0:
                    numeroextenso.append('cem')
                else:
                    numeroextenso.append(ext_c[lista[r]])
            if r == 3 and lista[3] > 1:#dezena regular
                if lista[2] > 0 or lista[1] > 0 or lista[0] > 0:
                    numeroextenso.append('e')
                numeroextenso.append(ext_d[lista[r]])
            if r == 4:
                if lista[3] > 0 or lista[2] > 0 or lista[1] > 0 or lista[0] > 0:
                    numeroextenso.append('e')
                if lista[3] == 1:#dezena irregular
                    numeroextenso.append(ext_u_ir[lista[r]])
                elif lista[4] > 0:#unidade
                    numeroextenso.append(ext_u[lista[r]])
    return " ".join(numeroextenso)
