'''Herança de Formas Geométricas Crie uma classe base chamada FormaGeometrica com um método para calcular a área. Em seguida, crie subclasses como Retangulo e Circulo que herdam de FormaGeometrica e implementam seus próprios métodos para calcular a área.
'''

class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return f'tamanho: {self.tamanho}, marca: {self.marca}'

class GarrafaDeVidro(Garrafa):
    def quebrar(self):
        print('crack')


garrafa = Garrafa(200, 'preto', 'Stanley')

garrafa_de_vidro = GarrafaDeVidro(200, 'transparente', 'vidro')




print(garrafa_de_vidro.__str__())