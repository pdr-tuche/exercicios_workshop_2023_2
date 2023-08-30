'''Herança de Formas Geométricas Crie uma classe base chamada FormaGeometrica com um método para calcular a área. Em seguida, crie subclasses como Retangulo e Circulo que herdam de FormaGeometrica e implementam seus próprios métodos para calcular a área.
'''

class FormaGeometrica:
    def calcular_a_área(self, raio):
        return 3.14*(raio**2)
    
class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcular_a_área(self, base, altura):
        return base*altura

class Quadrado(Retangulo):
    pass

circulo = Circulo()
area = circulo.calcular_a_área(20)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_a_área(5,10)
print(area)

quadrado = Quadrado()
area = quadrado.calcular_a_área(2,2)
print(area)