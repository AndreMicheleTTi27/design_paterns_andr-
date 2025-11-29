Padrão de Projeto: Builder 

> **Padrão Criacional (Creational)**
>
> O Builder é um padrão de projeto criacional que permite a você construir objetos complexos passo a passo. O padrão permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.

---

## Cenário 
Imagine que estamos criando um jogo de RPG. Um personagem (**Hero**) é uma entidade complexa. Ele tem:
* Nome
* Classe (Mago, Guerreiro, Arqueiro)
* Arma (pode ser nenhuma)
* Armadura (pode ser nenhuma)
* Nível, XP, Inventário, Habilidades...

Criando uma classe HeroBuilder, dedicada exclusivamente para montar o seu herói. 

Tendo assim uma classe para hero: 

class Hero:
    def __init__(self):
        # Inicializa tudo como vazio (None)
        self.name = None
        self.role = None
        self.weapon = None
        self.armor = None

    def __str__(self):
        # Método para imprimir o herói bonitinho no terminal
        return f"Herói [{self.name}] | Classe: {self.role} | Arma: {self.weapon} | Armadura: {self.armor}"

Uma classe para modelar seu herói:

class HeroBuilder:
    def __init__(self):
        self.hero = Hero()
        
Para solucionar isso, utilizamos a classe HeroBuilder. A classe utiliza utiliza métodos que retornam o próprio objeto (self) a cada etapa,
permitindo a configuraçao das características do herói passo a passo, de forma organizada e legível:

class HeroBuilder:
    def __init__(self):
        self.hero = Hero() # O objeto começa vazio

    # Métodos que configuram e retornam o próprio construtor (self)
    def set_name(self, name: str):
        self.hero.name = name
        return self

    def set_role(self, role: str):
        self.hero.role = role
        return self

    def build(self) -> Hero:
        result = self.hero
        self.hero = Hero() 
        return result
        
Permitindo criar heróis de forma legível:

# Uso final limpo e claro:
builder = HeroBuilder()
meu_heroi = builder.set_name("Otavio").set_role("Mago").build()
