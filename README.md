# 🥊 Sistema de Gestão de Alunos de Muay Thai

Este é um projeto que simula uma **escola de Muay Thai**, permitindo que um instrutor/professor gerencie seus alunos de forma simples e eficiente, utilizando menus interativos e lógica pura.

## 📋 Funcionalidades

- ✅ **Cadastrar aluno**  
  Registre um novo aluno informando:
  - Nome
  - E-mail
  - Faixa atual
  - Data de nascimento
  - Quantidade de aulas restantes até a próxima faixa

- 📄 **Listar todos os alunos cadastrados**  
  Veja todos os alunos registrados no sistema.

- 📆 **Cadastrar uma aula feita**  
  - Através do e-mail do aluno, selecione a quantidade de aulas realizadas.
  - O sistema reduz automaticamente a quantidade de aulas restantes até a próxima faixa.

- 📊 **Ver progresso do aluno**  
  - Consulte o progresso de um aluno utilizando seu e-mail.

- ✏️ **Atualizar dados do aluno**  
  - Com o `ID` único (auto incremental), altere:
    - Nome
    - E-mail
    - Faixa
    - Data de nascimento

## 🎯 Objetivo

O objetivo do projeto é simular a rotina de um instrutor de Muay Thai, permitindo o controle e acompanhamento dos alunos e suas evoluções apenas com **lógica de programação**, sem o uso de banco de dados ou frameworks externos.

---

## 🛠 Tecnologias utilizadas

- Python
- Menu interativo via terminal
- Estrutura baseada em listas, dicionários e lógica condicional

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
    ```
2. Acesse a pasta:
   ```bash
   cd nome-do-projeto:
   ```
3. (Opcional) Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/macOS
    .venv\Scripts\activate      # Windows
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o projeto:
    ```base
    python main.py
    ```