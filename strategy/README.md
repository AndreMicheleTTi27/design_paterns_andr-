# Padrão de Projeto: Strategy

> **Padrão Comportamental**
>
> O Strategy é um padrão de projeto comportamental que permite definir uma família de algoritmos, colocar cada um deles em uma classe separada e fazer com que seus objetos sejam intercambiáveis.
> O Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

---

## Cenário 

No jogo temos o combate, onde o nosso herói ciado precisa lutar, e dentro dessa luta temos objetos e magias para usar,como(Espadas,Bolas de fogo e Arco e flecha).

Sendo assim, colocar toda a lógica de ataque dentro da classe `Hero`, teríamos um método cheio de condicionais.

---

## Explicação do Código

Temos uma interface - CombatStrategy:

Define o contrato que todas as estratégias devem seguir. Em Python, usamos uma Classe Abstrata (ABC):

from abc import ABC, abstractmethod

class CombatStrategy(ABC):
    @abstractmethod
    def execute_attack(self, enemy_name: str) -> str:
        pass

Estratégias Concretas
São as implementações reais dos algoritmos de ataque:

class MeleeAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Acertou {enemy_name} com a espada!"

class MagicAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Lançou uma bola de fogo em {enemy_name}!"

class BowAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Disparou uma flecha em {enemy_name}!"

O contexto - HeroCombatContext
É a classe que interage com o jogo. Ela recebe uma estratégia e pode trocá-la a qualquer momento:

class HeroCombatContext:
    def __init__(self, strategy: CombatStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CombatStrategy):
        self._strategy = strategy

    def attack(self, enemy: str):
        print(self._strategy.execute_attack(enemy))


