#transformar números de algarismo para extenso
#unidades
ext_u = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
#Dezenas irregulares - dez a dezenove
ext_u_ir = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
#dezenas regulares
ext_d = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
#centenas
ext_c = ('', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')
n = int(input('Digite um número entre -99,000 e 99,000: '))
while n < -100000 or n > 100000:
    print ('Tente novamente!')
    n = int(input('Digite um número entre -99,000 e 99,000: '))
if n == 0:
    print ('zero')
if n < 0:
    print ('menos', end=' ')
lista = list()
for cont in range (0,5):
   isolado = n % 10
   n = n // 10
#    print (isolado)
   lista.insert(0, isolado)
for r in range (0,5):
   if r == 0 and lista[0] > 1:#dezena de milhar regular
       print (ext_d[lista[r]], end=' ')
   if r ==1:
       if  lista[0] == 1:#dezena de milhar irregular
           print (ext_u_ir[lista[r]], end=' ')
       elif lista[1] > 0:#milhar
           if lista[0] > 1:
               print ('e', end=' ')#!!!!
           print (ext_u[lista[r]], end=' ')
       if lista[0] or lista[1] > 0:
           print ('mil', end=' ')
   if r == 2 and lista[2] > 0:#centena
       if lista[1] > 0 or lista[0] > 0:
           print ('e', end=' ')
       if lista[3] == lista[4] == 0:
           print ('cem', end=' ')
       else:
           print (ext_c[lista[r]], end=' ')
   if r == 3 and lista[3] > 1:#dezena regular
       if lista[2] > 0 or lista[1] > 0 or lista[0] > 0:
           print ('e', end=' ')
       print (ext_d[lista[r]], end=' ')
   if r == 4:
       if lista[3] > 0 or lista[2] > 0 or lista[1] > 0 or lista[0] > 0:
           print ('e', end=' ')
       if lista[3] == 1:#dezena irregular
           print (ext_u_ir[lista[r]], end=' ')
       elif lista[4] > 0:#unidade
           print (ext_u[lista[r]], end=' ')

