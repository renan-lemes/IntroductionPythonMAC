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


