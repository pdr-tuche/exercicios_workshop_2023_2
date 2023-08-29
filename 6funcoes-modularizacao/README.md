# Exercicios (Funçoes e modularizacao)


**Funções**	
- Função é uma sequência de comandos que visa o processamento de uma tarefa específica.
Usada para reutilizar uma funcionalidade repetida
> exemplo
```py
#funcao para somar dois numeros
def soma (a,b):
    return a + b

print(soma(1,1)) # 2
print(soma(2,2)) # 4
print(soma(3,3)) # 6
```

**Modularização**

*Por que modularizar o código?*
- Essa abordagem facilita o desenvolvimento, a manutenção e a organização de programas maiores, tornando-os mais compreensíveis e reutilizáveis.

*Como importar módulos?*
>Exemplo de como importar módulos
```py
# arquivo funcoes.py

def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a * b

```
*importando modulo funcoes.py*
```py
import funcoes #importando modulo
from funcoes import soma #importando funcao do modulo

print(funcoes.soma(1,1)) # 2
print(soma(2,2)) # 4
```

# Exercicios

1. escolha qualquer exercicio anterior e crie funcoes e modulos =)