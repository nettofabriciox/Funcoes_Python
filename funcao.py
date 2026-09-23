#def msg():
   # print('Olá, mundo!')
#print(msg()) 
#msg()     

def soma(a,b,c):
    if c != 0:
        return (a+b)/c
    else:
        return 'Não é possível dividir por zero!'

if __name__ == '__main__':
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    print(soma(a, b, c))