# 🍽️ Sabor Express (Backend em Python)

Projeto desenvolvido em Python durante a trilha de **Back-end com Python da Alura**, com foco em lógica de programação, organização de código e persistência de dados.

Embora o projeto tenha sido proposto pela plataforma, a versão presente neste repositório **não é uma simples cópia do curso**.  
Diversas funcionalidades, validações e melhorias foram implementadas por conta própria, explorando conceitos além do escopo inicial do exercício.

O sistema simula o painel administrativo de um aplicativo de delivery (como iFood), permitindo o gerenciamento de restaurantes via terminal.

---

## 🎯 Objetivo do projeto

Este projeto teve como principais objetivos:

- Praticar lógica de programação em Python
- Desenvolver organização de código e modularização
- Trabalhar com persistência em banco de dados (SQLite)
- Entender operações de CRUD na prática
- Desenvolver autonomia na resolução de problemas
- Simular a base de um sistema backend real

O foco não foi interface gráfica, mas sim **a construção da lógica e estrutura de um sistema funcional**.

---

## 🚀 Funcionalidades

- Cadastrar restaurante (nome e categoria)
- Listar restaurantes cadastrados
- Alterar status do restaurante (ativo/inativo)
- Editar restaurante existente
- Excluir restaurante
- Persistência dos dados com SQLite
- Validação de entradas do usuário
- Mensagens claras de erro (ex: restaurante não encontrado)
- Sistema de menu interativo no terminal
- Estrutura organizada em múltiplos arquivos

---

## 🧠 Evolução além do curso

Durante o desenvolvimento, foram adicionadas funcionalidades que **não estavam presentes no projeto original da trilha**, como por exemplo:

- Implementação completa de CRUD
- Edição e exclusão de registros
- Controle por ID em vez de nome
- Validações para evitar operações inválidas
- Integração real com banco de dados SQLite
- Separação de responsabilidades (estrutura em módulos)
- Tratamento de erros e entradas inválidas
- Melhorias na experiência de uso no terminal
- Separação de responsabilidades funções/interface

Essas decisões foram feitas como parte do processo de aprendizado, explorando conceitos por conta própria e fortalecendo o entendimento da lógica por trás do sistema.

---

## 🗂️ Estrutura do projeto

sabor-express/
├── app.py
│   → Arquivo principal da aplicação
│   → Controla o fluxo do programa e integra UI e Services
│
├── ui.py
│   → Responsável pela interface em terminal (menus, textos e navegação)
│
├── services.py
│   → Contém as regras de negócio e operações de CRUD dos restaurantes
│
├── database.py
│   → Gerencia a conexão com o banco de dados SQLite e criação das tabelas
│
├── banco.db
│   → Banco de dados SQLite gerado automaticamente pela aplicação ao rodar o app.py
│
├── README.md
│   → Documentação do projeto

---

## 🖥️ Como executar o projeto

1. Certifique-se de ter o Python 3 instalado  
2. Clone o repositório  
3. Execute o arquivo principal:


```bash```
python app.py

O banco de dados será criado automaticamente na primeira execução.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLite3
- Programação estruturada
- Modularização de código
- Git e GitHub
- Terminal (CLI)

---

## 📚 Aprendizados aplicados

Este projeto reforçou conceitos importantes como:

- Lógica de programação
- Estruturas de dados (listas, dicionários, tuplas)
- Funções e modularização
- Organização de código
- CRUD (Create, Read, Update, Delete)
- Integração com banco de dados
- Tratamento de exceções
- Boas práticas iniciais de backend
- Pensamento arquitetural de sistemas

---

## 🔮 Próximos passos (futuro)

Este projeto poderá evoluir futuramente para:

- Transformação em API com FastAPI
- Criação de interface web (HTML/CSS)
- Integração com frontend real
- Expansão do domínio (produtos, pedidos, usuários)
- Autenticação e controle de acesso

---

## 👨‍💻 Autor

Desenvolvido por Dablyo Rodimar de Borba Teixeira
Estudante de programação com foco em Back-end Python
Em constante evolução 🚀