from abc import ABC, abstractmethod

class CombatStrategy(ABC):
    @abstractmethod
    def execute_attack(self, enemy_name: str) -> str:
        pass

class MeleeAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Acertou {enemy_name} com a espada!"

class MagicAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Lançou uma bola de fogo em {enemy_name}!"

class BowAttack(CombatStrategy):
    def execute_attack(self, enemy_name: str) -> str:
        return f"Disparou uma flecha em {enemy_name}!"

class HeroCombatContext:
    def __init__(self, strategy: CombatStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CombatStrategy):
        self._strategy = strategy

    def attack(self, enemy: str):
        print(self._strategy.execute_attack(enemy))
