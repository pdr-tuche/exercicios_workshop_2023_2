def show():
    pass
def calculadora():
    def soma (a,b):
        print(a+b)
    def sub (a,b):
        print(a-b)
    def mult (a,b):
        print(a*b)
    def div (a,b):
        print(a/b)
    var = input('operacao')
    numero = int(input('digite um numer'))
    numero2 = int(input('digite um numer'))
    if var == 'soma':
        soma(numero,numero2)
    elif var == 'subtracao':
        sub(numero,numero2)
    elif var == 'multiplicacao':
        mult(numero,numero2)
    elif var == 'divisao':
        div(numero,numero2)
    else:
        print('operacao nao reconhecida')
        

calculadora()