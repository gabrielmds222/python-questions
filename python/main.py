# while True:
#   Count = int(input('Digite um numero:'))
#   if Count < 1 or Count > 9:
#     print('O numero precisa ser entre 1 e 9')
#     Count = int(input('Digite um numero:'))
#   for i in range(1, 30):
#     print(''.join([str(x) for x in [Count, ' x ', i, ' = ', Count * i]]))


#===============================================================================================================================================
#===============================================================================================================================================


# Adicione 5 nomes em uma lista (Julio, Anna, Isabel, Izaac, Eduardo) e depois verifique se um nome digitado pelo usuário está presente na lista. Imprima inicialmente todos os nomes da lista, depois teste se o nome digitado pelo usuário está na lista criada e imprima uma mensagem correspondente a cada caso, de acordo com os exemplos a seguir.

# name = ['Julio', 'Anna', 'Isabel', 'Izaac', 'Eduardo']
# print('A lista contem os seguintes nomes:\n')
# for i in range(0,5):
#   print(name[i])
# verify = input('Qual nome voce quer verificar?')
# if verify == name[i]:
#   print('O nome', verify, 'esta na lista!')
# else:
#   print('O nome', verify, 'nao esta na lista!')


#===============================================================================================================================================
#===============================================================================================================================================


# Adicione 5 nomes em uma lista e depois verifique se um nome digitado pelo usuário está presente na lista, se estiver apague esse nome. Inicialmente imprima todos os nomes da lista, depois, pergunte qual nome o usuário quer apagar, imprima uma mensagem caso o nome seja apagado ou caso não esteja na lista. Ao final imprima todos os nomes da lista novamente.

# list = ['Jupter', 'Saturno', 'Urano', 'Netuno', 'Plutao']
# print('A lista contem os seguintes nomes:')
# for i in range(0,5):
#   print(list[i])
# erase = input('Qual nome deseja apagar?')
# if erase in list:
#   list.remove(erase)
#   print('A lista atual eh:')
#   for i in range(0,4):
#     print(list[i])
# else:
#   print(erase, 'nao foi encontrado na lista!')
#   print('A lista atual eh:')
#   for i in range(0,5):
#     print(list[i])



#===============================================================================================================================================
#===============================================================================================================================================


# Use uma lista para armazenar o nome dos 12 meses do ano. Leia do usuário um número que deve corresponder a um mês (1-12), e através desse número imprima o mês correspondente usando a lista. Caso o usuário digite um número menor do que 1 ou maior do que 12 imprima também uma mensagem de erro, conforme mostrado no exemplo.

# list = ['', 'Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubto', 'Novembro', 'Dezembro']
# num = int(input('Qual o numero do mes? '))

# if num >= 1 or num <= 12:
#   print('O mes é', list[num])
# else:
#   print(num)


#===============================================================================================================================================
#===============================================================================================================================================

# list = []
# for i in range(1,11):
#   num = int(input('digite o numero'))
#   list = [i]

# print(list[i])


#===============================================================================================================================================
#===============================================================================================================================================


# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. Seu programa deverá ler do usuário um valor (fora da função), e usar a função para imprimir a saída de acordo com os exemplos:

# def parimp():
#   valor = int(input('digite um numero'))
#   if valor%2 == 0:
#     print('eh par')
#   else:
#     print('eh impar')

# parimp()

#===============================================================================================================================================
#===============================================================================================================================================

# Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial. Seu programa deverá pedir ao usuário um número fora da função e usar a função para calcular e imprimir o valor do fatorial.

# num = int(input('Qual numero voce gostaria de saber o fatorial?'))

# def fatorial():
#   fat = 1
#   for i in range(num, 0, -1):
#     fat = fat * i
#   print(str(num)+'! e '+str(fat))

# fatorial()

#===============================================================================================================================================
#===============================================================================================================================================

# Escreva um programa que recebe as 3 notas de um aluno e uma letra (A ou P). Se a letra for A o programa calcula a média aritmética das notas do aluno e, se for P, a sua média ponderada (pesos: 5, 3 e 2). O calculo das médias deve ser feito por duas funções, uma função para média aritmética e outra para ponderada. Seu programa deve fazer todos os prompts e prints fora das funções!

# print('Quais sao as notas?')
# nota1 = int(input(''))
# nota2 = int(input(''))
# nota3 = int(input(''))
# tipo = input('Que tipo de media voce quer?')

# def arit():
#   media = (nota1+nota2+nota3)/3
#   print(media)

# def pond():
#   media = ((nota1*5)+(nota2*3)+(nota3*2))/(5+3+2)
#   print(media)

# if tipo == 'A':
#   arit()
# elif tipo == 'P':
#   pond()

#===============================================================================================================================================
#===============================================================================================================================================

# Fazer uma função que receba três números, os quais representam o comprimento dos lados de um triângulo. A função deve retornar 0 caso não possa ser um triângulo,  1 para equilátero, 2 para isósceles e 3 para escaleno. Seu programa deve perguntar ao usuário os lados, passar os valores para a função e imprimir a saída de acordo com os exemplos:

# print('Informe os lados')
# l1 = int(input(''))
# l2 = int(input(''))
# l3 = int(input(''))

# def triangulo():
#   if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l2 + l1:
#     if l1 == l2 == l3:
#       print('os lados '+str([l1, l2, l3])+' representam um triangulo equilatero')
#     elif l1 != l2 != l3:
#       print('os lados '+str([l1, l2, l3])+' representam um triangulo escaleno')
#     else:
#       print('os lados '+str([l1, l2, l3])+' representam um triangulo isosceles')
#   else:
#     print('os lados '+str([l1, l2, l3])+' nao representam um triangulo')

# triangulo()

#===============================================================================================================================================
#===============================================================================================================================================

# Escreva um programa que peça ao usuário um número inteiro e imprima a quantidade de divisores do número. O programa deve pedir ao usuário o número e usar uma função que recebe um número inteiro e retorne a quantidade de divisores que ele tem. O programa deve usar o retorno da função para imprimir a quantidade de divisores de acordo com o formato abaixo:

# num = int(input('Qual numero gostaria de checar os divisores?'))
# cont = 0

# def divisores(cont):
#   for i in range(1,num+1):
#     if num%i == 0:
#      cont = cont + 1   
#   print('O numero '+str(num)+' tem '+str(cont)+' divisores') 

# divisores(cont)


#===============================================================================================================================================
#===============================================================================================================================================
# num = []
# words = []
# qtdnum = int(input('Digite a quantidade de numeros que deseja incluir:'))
# qtdwords = int(input('Digite a quantidade de textos que deseja incluir:'))

# def numeros():
#     for i in range(0,qtdnum):
#         digitenum = input('Digite um numero:')
#         num.append(digitenum)


# def palavras():
#     for i in range(0,qtdwords):
#         digiteword = input('Digite um texto:')
#         words.append(digiteword)

# numeros()
# palavras()

# print('Lista de numeros:')
# print(str(num).strip('[]'))

# print('Lista de textos:')
# print(str(words).strip('[]'))


#===============================================================================================================================================
#===============================================================================================================================================

# print('Vamos encontrar os numeros primos em um intervalo entre dois numeros positivos?')
# nmenor = int(input('Digite o numero menor do intervalo'))
# nmaior = int(input('Digite o numero maior do intervalo'))
# tot = 0
# def primos(tot):
#     for i in range(nmenor, nmaior+1):
#         if nmaior%i == 0: 
#             tot += 1
#             print(tot)
#         else:
#             print('Nao ha numeros primos nesse intervalo!')

# primos(tot)

# print('Os numeros primos sao: '+ str(tot))

#===============================================================================================================================================
#===============================================================================================================================================
# import math

# numA = float(input('Digite o numero A:'))
# numB = float(input('Digite o numero B:'))

# ad = numA + numB
# sub = numA - numB
# div = numA / numB
# inteiro = math.floor(div)
# resto = numA % numB

# print(str(numA)+ ' + '+ str(numB)+ ' = '+ str(ad))
# print(str(numA)+ ' - '+ str(numB)+ ' = '+ str(sub))
# print(str(numA)+ ' / '+ str(numB)+ ' = '+ str(div))
# print(str(int(numA))+ ' // '+ str(int(numB))+ ' = '+ str(inteiro))
# print(str(int(numA))+ ' % '+ str(int(numB))+ ' = '+ str(int(resto)))


#===============================================================================================================================================
#===============================================================================================================================================

# from math import log, sin, cos

# x = int(input('x?'))
# y = int(input('y?'))
# z = int(input('z?'))

# raiz = ((x**2)+(y**2)+(z**2))**1/3

# pot = int((x**y)+(y**z))

# seno = sin((x**2+y**2))
# cosseno = cos((y**2+z**2))
# logaritmos = (log(x)+log(y)+log(z))**(x+y+z)


# print('raiz cubica({}^2 + {}^2 + {}^2) = {}' .format(x,y,z,raiz))

# print('{}^{} + {}^{} = {}' .format(x,y,y,z,pot))

# print('sin({}^2+{}^2) + cos({}^2+{}^2) = {}'  .format(x,y,y,z,seno+cosseno))

# print('log {} + log {} + log {} ^ ({} + {} + {}) = {}' .format(x,y,z,x,y,z,logaritmos))


#===============================================================================================================================================
#===============================================================================================================================================


# texto1 = str(input('Digite o texto A: '))
# texto2 = str(input('Digite o texto B: '))
# c1 = len(texto1)
# c2 = len(texto2)
# ultimo1 = texto1[c1-1]
# ultimo2 = texto2[c2-1]

# print('tamanho(A) - tamanho(B) = {}'.format(len(texto1)-len(texto2)))
# print('A + B = {}' .format(texto1+texto2))
# print('A contem B = {}' .format(texto2 in texto1))
# print('B contem A = {}' .format(texto1 in texto2))
# print('Primeira letra de A = {}' .format(texto1[0]))
# print('Primeira letra de B = {}' .format(texto2[0]))
# print('Ultima letra de A = {}' .format(ultimo1))
# print('Ultima letra de B = {}' .format(ultimo2))

#===============================================================================================================================================
#===============================================================================================================================================

# texto1 = str(input('Digite o texto A: '))
# # texto2 = str(input('Digite o texto B: '))

# textdiv = len(texto1)/2

# print(texto1[2:])


# Digite o texto A: uma_palavra_A

# Digite o texto B: outro_texto_B

# Texto A dividido em duas Partes: uma_pa e lavra_A

# Texto B dividido em duas Partes: outro_ e texto_B

# uma_pa + texto_B = uma_patexto_B

# lavra_A + outro_ = lavra_Aoutro_

# u + u + A + B = uuAB

#===============================================================================================================================================
#===============================================================================================================================================



# p1 = input('Texto 1? ')
# p2 = input('Texto 2? ')
# p3 = input('Texto 3? ')


# print('seguem os textos em ordem:')

# # Todos diferentes

# if p2 > p1 > p3:
#     print('1o. '+str(p2))
#     print('2o. '+str(p1))
#     print('3o. '+str(p3))
# elif p3 > p1 > p2:
#     print('1o. '+str(p3))
#     print('2o. '+str(p1))
#     print('3o. '+str(p2))
# elif p1 > p2 > p3:
#     print('1o. '+str(p1))
#     print('2o. '+str(p2))
#     print('3o. '+str(p3))
# elif p3 > p2 > p1:
#     print('1o. '+str(p3))
#     print('2o. '+str(p2))
#     print('3o. '+str(p1))
# elif p1 > p3 > p2:
#     print('1o. '+str(p1))
#     print('2o. '+str(p3))
#     print('3o. '+str(p2))
# elif p2 > p3 > p1:
#     print('1o. '+str(p2))
#     print('2o. '+str(p3))
#     print('3o. '+str(p1))

# # Todos iguais

# if p1 == p2 and p2 == p3:
#     print('1o. '+str(p1))
#     print('2o. '+str(p2))
#     print('3o. '+str(p3))


# # Se dois forem iguais 

# if p1 == p2 and p1 != p3:
#     if p1 < p3:
#         print('1o. '+str(p2))
#         print('2o. '+str(p3))
#         print('3o. '+str(p1))
#     elif p1 > p3:
#         print('1o. '+str(p1))
#         print('2o. '+str(p2))
#         print('3o. '+str(p3))
        
# if p1 == p3 and p1 != p2:
#     if p1 < p2:
#         print('1o. '+str(p2))
#         print('2o. '+str(p3))
#         print('3o. '+str(p1))
#     elif p1 > p2:
#         print('1o. '+str(p1))
#         print('2o. '+str(p2))
#         print('3o. '+str(p3))
        
# if p3 == p2 and p1 != p2:
#     if p2 < p1:
#         print('1o. '+str(p1))
#         print('2o. '+str(p3))
#         print('3o. '+str(p2))
#     elif p2 > p1:
#         print('1o. '+str(p2))
#         print('2o. '+str(p1))
#         print('3o. '+str(p3))  


# p1 é a maior
# if p1 > p2 and p1 > p3:
#     maior = p1
#     if p2 > p3:
#         meio = p2
#         menor = p3
#     elif p3 > p2:
#         meio = p3
#         menor = p2
#     elif p3 == p2:
#         meio = p3
#         menor = p2

# # p2 é a maior
# if p2 > p1 and p2 > p3:
#     maior = p2
#     if p1 > p3:
#         meio = p1
#         menor = p3
#     elif p3 > p1:
#         meio = p3
#         menor = p1
#     elif p3 == p1:
#         meio = p3
#         menor = p1

# # p3 é a maior
# if p3 > p2 and p3 > p1:
#     maior = p3
#     if p2 > p1:
#         meio = p2
#         menor = p1
#     elif p1 > p2:
#         meio = p1
#         menor = p2
#     elif p1 == p2:
#         meio = p1
#         menor = p2

# if p1 == p2 == p3:
#     maior = p1
#     meio = p2
#     menor = p3
# print('1o. {}' .format(menor))
# print('2o. {}' .format(meio))
# print('3o. {}' .format(maior))



#===============================================================================================================================================
#===============================================================================================================================================


# ndias = int(input('Qual o numero de dias? '))
# dia = 0

# # Menos de uma semana

# if ndias == 0:
#     print('{} dias equivale a nenhum dia.' .format(ndias))


# elif ndias > 0 and ndias < 7:
#     print('{} dias equivalem a 0 semana e {} dias!' . format(ndias, ndias))


# # Uma semana

# elif ndias == 7:
#     print('{} dias equivalem a 1 semana!' .format(ndias))


# elif ndias > 7 and ndias < 14:
#     dia = ndias - 7
#     if dia > 1:
#         print('{} dias equivalem a 1 semana e {} dias!' .format(ndias, dia))
#     else:
#         print('{} dias equivalem a 1 semana e {} dia!' .format(ndias, dia))


# # Duas semanas

# elif ndias == 14:
#     print('{} dias equivalem a 2 semanas!' .format(ndias))


# elif ndias > 14 and ndias < 21:
#     dia = ndias - 14
#     if dia > 1:
#         print('{} dias equivalem a 2 semanas e {} dias!' .format(ndias, dia))
#     else:
#         print('{} dias equivalem a 2 semanas e {} dia!' .format(ndias, dia))


# # Três semanas

# elif ndias == 21:
#     print('{} dias equivalem a 3 semanas!' .format(ndias))


# elif ndias > 21 and ndias < 28:
#     dia = ndias - 21
#     if dia > 1:
#         print('{} dias equivalem a 3 semanas e {} dias!' .format(ndias, dia))
#     else:
#         print('{} dias equivalem a 3 semanas e {} dia!' .format(ndias, dia))


# # Quatro semanas

# elif ndias == 28:
#     print('{} dias equivalem a 4 semanas!' .format(ndias))


# elif ndias > 28:
#     dia = ndias - 28
#     if dia > 1:
#         print('{} dias equivalem a 4 semanas e {} dias!' .format(ndias, dia))
#     else:
#         print('{} dias equivalem a 4 semanas e {} dia!' .format(ndias, dia))

#===============================================================================================================================================
#===============================================================================================================================================


# n =int( input(""))
# t1 = 1
# t2 = 1

# if n == 1:
#     print(1)
    
# elif n == 2:
#     print('{}, {}' .format(1,2))

# else:
#     print('{}, {}, ' .format(t1, t2), end='')
#     cont = 2

#     while cont < n:
#         t3 = t1 + t2
#         print("{}, ".format(t3), end='')
#         t1 = t2
#         t2 = t3
#         cont += 1
#     t3 = t1 + t2
#     print("{}".format(t3), end='')

#===============================================================================================================================================
#===============================================================================================================================================


# n = int(input("n?"))

# i = 1
# while i * (i+1) * (i+2) < n:
#     i = i + 1

# if i * (i+1) * (i+2) == n:
#     print("e triangular")
# else:
#     print("nao e triangular")


#===============================================================================================================================================
#===============================================================================================================================================


# n1 = int(input('n1?'))
# n2 = int(input('n2?'))
# total = 0

# for i in range (n1+1,n2):
   
#     if i%2 != 0:
#         total += 1

# if total == 1:
#     print('Existe {} numero primo entre {} e {}' .format(total,n1,n2))
# else:
#     print('Existem {} numeros primos entre {} e {}' .format(total,n1,n2))

#===============================================================================================================================================
#===============================================================================================================================================

# n1 = int(input('Digite n1:'))
# n2 = int(input('Digite n2:'))

# for i in range(n1,n2+1):
#     print('=-=-=-= Tabuada de {} =-=-=-=' .format(i))
#     for c in range(1,11):
#         print('{} x {} = {}' .format(i, c, i*c))

#===============================================================================================================================================
#===============================================================================================================================================

# n = int(input('n?'))

# for i in range(1,n+1):
#     print(str(i)*i)

#===============================================================================================================================================
#===============================================================================================================================================

# n = int(input('Quantos nomes?'))
# list = []
# j = 0

# for i in range(1,n+1):
#     nomes = input('')
#     list.append(nomes)

# print('Voce digitou:')

# for j in reversed(list):
#     print(j)
    
#===============================================================================================================================================
#===============================================================================================================================================


# n = int(input('Qual o N? '))
# print('Digite os valores: ')

# lista = []

# for i in range(1,n+1):
#     num = input('')
#     lista.append(num)

# op = int(input('Qual a op? '))
# a = int(input('Qual o A? '))
# b = int(input('Qual o B? '))


# if op == 0:
    
#     print('{} + {} = {}' .format(int(lista[a-1]), int(lista[b-1]), int(lista[a-1]) + int(lista[b-1])))
# elif op == 1:
    
#      print('{} * {} = {}' .format(int(lista[a-1]), int(lista[b-1]), int(lista[a-1]) * int(lista[b-1])))

#===============================================================================================================================================
#===============================================================================================================================================


# qtalunos = int(input('Quantos alunos?'))
# print('Digite os nomes dos alunos:')

# lista = []
# aux = 0

# for i in range(1,qtalunos+1):
#     alunos = input('')
#     lista.append(alunos)

# print('Nova lista:')

# primeiro = 1

# if len(lista)%2 == 0:
#     ultimo = len(lista) - 1
# else:
#     ultimo = len(lista) - 2

# while primeiro < ultimo:
#      aux = lista[primeiro]
#      lista[primeiro] = lista[ultimo]
#      lista[ultimo] = aux

#      primeiro = primeiro + 2
#      ultimo = ultimo - 2

# for j in (lista):
#     print(j)

#===============================================================================================================================================
#===============================================================================================================================================


# texto = input('Digite o texto:').lower()
# aux = ''
# tam = len(texto)

# def cripto(aux):
#     for i in range(0, tam):
#         if texto[i] >= 'a' and texto[i] <= 'e':
#             aux = aux + '1'
        
#         elif texto[i] >= 'f' and texto[i] <= 'j':
#             aux = aux + '2'

#         elif texto[i] >= 'k' and texto[i] <= 'o':
#             aux = aux + '3'

#         elif texto[i] >= 'p' and texto[i] <= 'z':
#             aux = aux + '4'

#         else:
#             aux = aux + '5'

#     return aux

# resultado = cripto(aux)

# print('Encriptado: {}' .format(resultado))

#===============================================================================================================================================
#===============================================================================================================================================

def primos(num):
  list = []
  for i in range(1, num//2+1):
    if num % i == 0: 
      list.append(i)
  list.append(num)
  return list
      
  
dataSet = []

n = int(input('Qual o valor de N?'))

print('Digite os valores:')

for i in range (0, n):
  num = int(input(''))
  dataSet.append(num)

print('A classificacao e:')
for i in range (0, n):
  num = dataSet[i]
  divisores = primos(num)
  if(len(divisores) == 2 and divisores == [1, num]):
    print('{} e primo'.format(num))
  else:
    print('{} nao e primo, os divisores sao: {}'.format(num, primos(num)))