# -*- coding: UTF-8 -*-

# 2) Determine se um ano é bissexto.
# Tente dividir o ano por 4. Se o resto for diferente de 0, ou seja, se for indivisível por 4, ele não é bissexto.
# Se for divisível por 4, é preciso verificar se o ano acaba em 00 (zero duplo). Em caso negativo, o ano é bissexto.
# Se terminar em 00, é preciso verificar se é divisível por 400. Se sim, é bissexto; se não, é um ano normal. 
year = int(input('Digite o ano: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
# -*- coding: UTF-8 -	print ('Seu ano é bissexto')
else:
	print ('Seu ano não é bissexto')
