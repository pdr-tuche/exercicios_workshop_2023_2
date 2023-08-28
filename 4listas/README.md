# Exercicios (listas)

## conceito

**Listas, pilhas e filas são estruturas de dados com diferentes propriedades e comportamentos**

**Lista:**
Uma lista é uma coleção ordenada de elementos onde cada elemento é acessado por um índice. Ela não possui restrições específicas sobre como os elementos são inseridos ou removidos.

>Exemplo:
```py
lista = [10, 20, 30, 40, 50]
print(lista[2])  # Saída: 30
```

**Pilha:**
Uma pilha é uma estrutura de dados baseada no princípio "LIFO" (Last In, First Out), o último elemento inserido é o primeiro a ser removido. É como uma pilha de pratos, onde você adiciona pratos no topo e retira do topo.

>Exemplo:
```py
pilha = []
# Adicionando elementos à fila (enqueue)
pilha.append(10)
pilha.append(20)
pilha.append(30)
# Removendo o ultimo elemento que entrou na pilha (dequeue)
print(pilha.pop())  # Saída: 30
```

**Fila:**
Uma fila é uma estrutura de dados baseada no princípio "FIFO" (First In, First Out), o primeiro elemento inserido é o primeiro a ser removido. É como uma fila de pessoas esperando em um caixa, onde a primeira que chegou é a primeira a ser atendida.

>Exemplo:
```py
fila = []
# Adicionando elementos à fila (enqueue)
fila.append(10)
fila.append(20)
fila.append(30)
# Removendo o primeiro elemento da fila (dequeue)
primeiro_elemento = fila.pop(0)
print(primeiro_elemento)  # Saída: 10
```

## Em resumo:

- Uma lista é uma coleção ordenada com acesso por índice.
- Uma pilha é uma coleção onde o último elemento inserido é o primeiro a sair.
- Uma fila é uma coleção onde o primeiro elemento inserido é o primeiro a sair.

**Cada uma dessas estruturas de dados é útil para diferentes cenários, dependendo dos requisitos do seu programa.**


# Exercicios

**1. Fila de Tarefas**
- Crie um programa que simule uma fila de tarefas a serem executadas. O usuário deve poder adicionar tarefas à fila e retirá-las na ordem em que foram adicionadas.

```bash
DIGITE O QUE FAZER:
1. Adicionar tarefa
2. Executar fila de tarefas
3. Sair

Escolha uma opção: 1
Digite a descrição da tarefa: Limpar a cozinha

Escolha uma opção: 1
Digite a descrição da tarefa: Fazer compras

Escolha uma opção: 2
Executando: Limpar a cozinha

Escolha uma opção: 2
Executando: Fazer compras

Escolha uma opção: 3

```

**2. pilha de Tarefas**
- parabens ^^ voce conseguiu implementar uma fila, agora modifique o programa anterior mudando a logica de fila para pilha

```bash
DIGITE O QUE FAZER:
1. Adicionar tarefa
2. Executar fila de tarefas
3. Sair

Escolha uma opção: 1
Digite a descrição da tarefa: Limpar a cozinha

Escolha uma opção: 1
Digite a descrição da tarefa: Fazer compras

Escolha uma opção: 2
Executando: Fazer compras

Escolha uma opção: 2
Executando: Limpar a cozinha

Escolha uma opção: 3

```