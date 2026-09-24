#def msg():
   # print('Olá, mundo!')
#print(msg()) 
#msg()     

def soma(a, b, c):
    if c != 0:
        return (a + b) / c
    return 'Não é possível dividir por zero!'

#if __name__ == '__main__':
 #   a = float(input('Digite o valor de a: '))
  #  b = float(input('Digite o valor de b: '))
  #  c = float(input('Digite o valor de c: '))
  #  print(f'O numero {a} somado com o numero {b} dividido pelo numero {c} é igual a {soma(a,b,c)}')

#def quadrados(valor):
 #   resultado = []
 #   for i in valor:
      #  resultado.append(i ** 2)
      #  sorted(resultado)
  #  return resultado

#def contar(num=11, caracter='*'):
   # for i in range(1, num):
       # print(caracter) 

def square(n):
    return n ** 2


if __name__ == '__main__':

    lista = [1, 2, 3, 4, 5]
    for numeros in lista:
        num = square(numeros)
        print(f'O quadrado de {numeros} é {num}')

        



        