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

def quadrados(valor):
    resultado = []
    for i in valor:
        resultado.append(i ** 2)
        sorted(resultado)
    return resultado

if __name__ == '__main__':
    valor = [2,56,3,1,-7, 67, 3 , 566, -9999, 7, 4]
    resultado = quadrados(valor)

   
    for numeros in resultado:
        if numeros < 20:
            print(f'O quadrado do numero {numeros} é menor que 20')

        