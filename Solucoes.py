# 1
# bom = 'Bom'
# dia = ' dia'
# bd = bom + dia
# db = bom *3
# print(db)

# 2 - escolhi a tabuada do 5
# a = 5
# print('5x1 = ',a*1)
# print('5x2 = ',a*2)
# print('5x3 = ',a*3)
# print('5x4 = ',a*4)
# print('5x5 = ',a*5)
# print('5x6 = ',a*6)
# print('5x7 = ',a*7)
# print('5x8 = ',a*8)
# print('5x9 = ',a*9)
# print('5x10 = ',a*10)

# 3
# entrada = int(input('Digite um número inteiro: '))

# if (entrada%2) == 0:
#     print(f'O número {entrada} é par',)
# else:
#     print(f'O número {entrada} não é par',)
    
# 4 

#entrada = input('Digite uma palavra: ')
# for i in entrada:
#     if (i == 'a') or (i == 'e') or (i == 'o') or (i=='u') or (i == 'i'):
#         print(i)
#     else:
#         pass

# for i in entrada:
#     if (i != 'a') and (i != 'e') and (i != 'i') and (i != 'o') and (i != 'u'):
#         print(i)



# 5

# def Aprov(p1, p2, frq):
#     sum_p = p1+p2
#     sum_p = sum_p/2

#     if frq > 0.100:
#         frq = frq/100

#     if (sum_p >7.0 and frq >= 0.75):
#         return True, sum_p, frq
#     else:
#         return False, sum_p, frq

# nomealuno = input("Digite o nome do aluno: ")
# p1 = float(input("Digite o valor da P1: "))
# p2 = float(input("Digite o valor da P2: "))
# frq = float(input("Digite o a frequencia do aluno: "))

# apr, media, frq = Aprov(p1, p2, frq)
# print(f'Aprovadou/Reprovado {apr} media : {media} frequencia: {frq} ')

# 6

# def fatorial(n):
#     if type(n) != int:
#         print('Esse fatorial não é interavel.')
#         return None
#     elif n < 0:
#         print('Esse fatorial é negativo.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         recurse = fatorial(n-1)
#         result = n * recurse
#         return result

# n = int(input("Digite um inteiro: "))
# resultado = fatorial(n)
# print(f"O Fatorial de {n} é {resultado}")

# 7 

# def Ark(m,n):
#     if m==0:
#         return n+1
#     elif m > 0 and n == 0:
#         return Ark(m-1, 1)
#     elif m > 0 and n > 0:
#         return Ark(m-1, Ark(m, n-1))

# arkman  = Ark(3, 4)

# print(arkman)


# 8
# from math import pi


# def Pi():
#     n = 0
#     p_i = 0
#     while True:
        
#         p_i += ((-1)**n)/(2*n + 1)

#         if n == 1000:
#             return p_i * 4 
#         n += 1    


# print(f' Função {Pi()} e PI {pi}')
# print(f' Diferença {Pi() - pi}')


# 9

# from math import exp
# #from math import factorial

# def expon(x):
#     n = 0
#     e = 0 
#     while True:
#         e += (x**n)/fatorial(n)
#         n += 1
#         if n == 100:
#             return e


# print(exp(2))
# print(expon(2))


# 10

# def fibon(n):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fibon(n-1) + fibon(n-2))
    
# print(fibon(7))