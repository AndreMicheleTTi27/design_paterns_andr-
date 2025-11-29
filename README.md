# Design Paterns
# RPG Engine: Portfólio de Padrões de Projeto

> **Disciplina:** Engenharia de Software  
> **Aluno:** André Alevato Micheletti
> **RA:** 2727463

---

## Sobre o Projeto

Este repositório apresenta a aplicação prática de três **Padrões de Projeto clássicos (GoF)**, utilizados para resolver problemas arquiteturais no desenvolvimento de um jogo de RPG.

---

## Organização dos Módulos

O projeto está estruturado em três diretórios principais, cada um focado em uma categoria distinta de padrões aplicada a uma mecânica do jogo:

1.  **Builder (Criacional):**
    * *Aplicação:* Sistema de criação de personagens (Heróis) passo a passo.
2.  **Facade (Estrutural):**
    * *Aplicação:* Interface simplificada para inicializar a *Game Engine* (Vídeo, Áudio e Rede).
3.  **Strategy (Comportamental):**
    * *Aplicação:* Sistema de combate dinâmico com troca de armas em tempo real.

---

## 📦 Conteúdo dos Diretórios

Cada pasta deste repositório funciona como um módulo independente contendo:
* 🐍 **Código Fonte (.py):** A implementação funcional do padrão em Python.
* 📄 **Documentação Dedicada (README):** Um guia explicativo contendo:
    * **Cenário:** O problema específico do RPG que precisava ser resolvido.
    * **Solução:** Como o padrão resolve o problema.
    * **Diagrama UML:** Representação visual da estrutura das classes.
    * **Análise de Código:** Explicação detalhada bloco a bloco.

---

## 📚 Referências e Créditos

* **Fonte Teórica:** Todo o embasamento conceitual, definições e modelos de diagramas UML foram baseados no catálogo do [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns).
* **Implementação:** Código desenvolvido com auxílio de ferramentas de LLM (Google Gemini) para refatoração e revisão de boas práticas.
