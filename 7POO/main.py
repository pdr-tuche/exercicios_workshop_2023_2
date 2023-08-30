class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
    
    def __str__(self):
        return f'oi eu sou uma garrafa {self.marca}'
    
    def __eq__(self, obj):
        if self.marca == obj.marca:
            return True
        else:
            return False
    
    def encher(self):
        print('estou enchida')
    
    def esvaziar(self):
        print('estou ficando vazia')



garrafa = Garrafa(100, 'preto', 'kasfkkfs')
print(garrafa)

stanley = Garrafa(100, 'preto', 'shopee')
print(stanley)

print(garrafa == stanley)


stanley.encher()

stanley.esvaziar()