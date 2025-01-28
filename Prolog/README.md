# 📚 Registro Pessoal de Estudos em Prolog

Este repositório é um registro pessoal da minha jornada de estudos em **Prolog**. Aqui, compartilho exemplos, exercícios e anotações que estou criando enquanto aprendo essa linguagem de programação. O objetivo é documentar meu progresso e, ao mesmo tempo, servir como um guia de referência para quem também está começando a explorar o mundo da lógica de programação.

Para me guiar nessa jornada, estou seguindo a playlist de aulas disponível no YouTube:  
👉 [Playlist de Aulas de Prolog](https://www.youtube.com/playlist?list=PLZ-Bk6jzsb-OScKa7vhpcQXoU2uxYGaFx)

---

## 🔧 Pré-requisitos

Antes de começar, você precisará:

1. **Instalar o SWI-Prolog**  
   Baixe e instale a versão estável do SWI-Prolog pelo link oficial:  
   👉 [SWI-Prolog Download](https://www.swi-prolog.org/download/stable/bin/swipl-9.2.9-1.x64.exe.envelope)

   **⚠️ Atenção:** Durante a instalação, certifique-se de marcar a opção **"Adicionar ao PATH" (Add to PATH)** para que o Prolog funcione no terminal.

2. (Opcional) **Extensão Prolog no VS Code**  
   Você pode instalar a extensão "Prolog" no Visual Studio Code para suporte a sintaxe, mas ela **não é necessária para executar o programa**.

---

## 🚀 Como Executar Programas Prolog

Siga os passos abaixo para rodar seus programas Prolog no VS Code:

1. **Abra o Terminal no VS Code**

   - No menu, clique em **Terminal > Novo Terminal** ou use o atalho `Ctrl + '`.

2. **Inicie o SWI-Prolog**

   - No terminal, digite o comando abaixo e pressione Enter:
     ```bash
     swipl
     ```
   - Isso abrirá o interpretador do Prolog no terminal.

3. **Carregue o Arquivo `.pl`**

   - Use o comando `consult` para carregar o arquivo com seu programa Prolog:
     ```prolog
     ?- consult('nome_do_arquivo.pl').
     ```
   - **Importante:** Termine o comando com um **`.`** (ponto) antes de pressionar Enter.

4. **Faça Consultas**
   - Após carregar o arquivo, você pode executar consultas, como:
     ```prolog
     ?- fato_ou_regra(X).
     ```
   - Não se esqueça do **`.`** ao final das consultas.

---