# Padrão de Projeto: Builder

> **Padrão Criacional (Creational)**
>
> O Builder é um padrão de projeto criacional que permite a você construir objetos complexos passo a passo. O padrão permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.

---

## ⚔️ Cenário (O Problema)
Em um jogo de RPG, o personagem (**Hero**) é uma entidade complexa. Ele tem:
* Nome
* Classe (Mago, Guerreiro, Arqueiro)
* Arma (pode ser nenhuma)
* Armadura (pode ser nenhuma)
* Nível, XP, Inventário, Habilidades...

Isso cria a necessidade de uma classe `HeroBuilder`, dedicada exclusivamente para montar o seu herói passo a passo, evitando construtores gigantes e confusos.

---

### 📐 Diagrama UML
A estrutura de classes abaixo demonstra como o `HeroBuilder` isola a complexidade da criação do `Hero`:

```mermaid
classDiagram
    class Hero {
        +name: str
        +role: str
        +weapon: str
        +armor: str
        +__str__()
    }

    class HeroBuilder {
        -hero: Hero
        +set_name(name)
        +set_role(role)
        +equip_weapon(weapon)
        +equip_armor(armor)
        +build() : Hero
    }

    HeroBuilder ..> Hero : Cria (Dependency)
