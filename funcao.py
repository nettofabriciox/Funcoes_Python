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
    for i in range(valor):
        resultado.append(i ** 2)
    return resultado

if __name__ == '__main__':
    valor = [2,56,3,1,-7]
    print(f'Os quadrados dos números de 0 a {len(valor)-1} são: {quadrados(len(valor))}')