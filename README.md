# IA Nivelamento - MBA Engenharia de IA Full Cycle

Este repositório contém os exercícios e projetos de nivelamento para o MBA de Engenharia de IA da Full Cycle. O projeto foi desenvolvido para consolidar os conceitos fundamentais de Inteligência Artificial, com foco em frameworks modernos como LangChain e integração com modelos de linguagem.

## 📚 Estrutura do Projeto

### 1. Fundamentos (`1-fundamentos/`)

- **1-hello-world.py**: Primeiro contato com APIs de IA
- **2-init-chat-bot.py**: Implementação básica de chatbot
- **3-prompt-template.py**: Uso de templates de prompt
- **4-chat-prompt-template.py**: Templates específicos para chat

### 2. Chains e Processamento (`2-chains-e-processamento/`)

- **1-iniciando-com-chain.py**: Introdução ao conceito de chains
- **2-chains-com-decorators.py**: Implementação avançada com decorators

### 3. Gerenciamento de Memória (`4-Gerencia-de-memoria/`)

- **1-armazenamento-historico.py**: Sistema de persistência de histórico de conversas

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **LangChain**: Framework principal para desenvolvimento de aplicações de IA
- **OpenAI API**: Integração com modelos GPT
- **Google Generative AI**: Integração com modelos Gemini
- **SQLAlchemy**: ORM para gerenciamento de banco de dados
- **Docker**: Containerização da aplicação

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11+
- Docker (opcional)
- Chaves de API para OpenAI e/ou Google AI

### Instalação Local

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd IA-Nivelamento
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

```bash
# Crie um arquivo .env na raiz do projeto
OPENAI_API_KEY=sua_chave_openai
GOOGLE_API_KEY=sua_chave_google
```

5. Execute os scripts:

```bash
# Exemplo: executar o hello world
python 1-fundamentos/1-hello-world.py

# Exemplo: executar chains com decorators
python 2-chains-e-processamento/2-chains-com-decorators.py
```

### Execução com Docker

1. Construa a imagem:

```bash
docker build -t ia-nivelamento .
```

2. Execute o container:

```bash
docker run -e OPENAI_API_KEY=sua_chave -e GOOGLE_API_KEY=sua_chave ia-nivelamento
```

Ou use o script de conveniência:

```bash
chmod +x docker-run.sh
./docker-run.sh
```

## 📖 Conteúdo dos Exercícios

### Fundamentos

- **Hello World**: Primeira interação com APIs de IA
- **Chat Bot**: Implementação de um chatbot básico
- **Prompt Templates**: Criação e reutilização de templates
- **Chat Templates**: Templates específicos para conversas

### Chains e Processamento

- **Chains Básicas**: Conceitos fundamentais de chains no LangChain
- **Chains com Decorators**: Implementação avançada usando decorators Python

### Gerenciamento de Memória

- **Armazenamento Histórico**: Sistema para persistir e recuperar histórico de conversas

## 🔧 Configuração

### Variáveis de Ambiente Necessárias

```env
# OpenAI (opcional)
OPENAI_API_KEY=sua_chave_openai_aqui

# Google AI (opcional)
GOOGLE_API_KEY=sua_chave_google_aqui

# Configurações do banco de dados (para gerenciamento de memória)
DATABASE_URL=sqlite:///chat_history.db
```

## 🧪 Qualidade de Código

Este projeto utiliza ferramentas de linting e formatação de código:

- **Black**: Formatação automática de código
- **isort**: Organização de imports
- **Flake8**: Detecção de erros e problemas de estilo
- **MyPy**: Verificação de tipos (opcional)

### Executar Linting Local

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Execute o script de linting
python lint.py

# Ou use o script bash
./run-lint.sh
```

### Corrigir Problemas Automaticamente

```bash
# Formatar código
black .

# Organizar imports
isort .
```

Para mais detalhes, consulte [LINTING.md](LINTING.md).

## 📝 Objetivos de Aprendizado

Este projeto de nivelamento visa:

1. **Consolidar conceitos fundamentais** de IA e processamento de linguagem natural
2. **Praticar integração** com APIs de modelos de linguagem
3. **Implementar padrões** de desenvolvimento com LangChain
4. **Gerenciar estado** e persistência em aplicações de IA
5. **Containerizar aplicações** para deploy e distribuição

## 🎯 Próximos Passos

Após completar este nivelamento, os alunos estarão preparados para:

- Desenvolver aplicações mais complexas de IA
- Implementar RAG (Retrieval-Augmented Generation)
- Trabalhar com embeddings e vector databases
- Construir sistemas de IA em produção

## 📞 Suporte

Para dúvidas ou problemas relacionados ao projeto, consulte:

- Documentação oficial do [LangChain](https://python.langchain.com/)
- [Full Cycle Community](https://fullcycle.com.br/)

---

**Desenvolvido para o MBA de Engenharia de IA - Full Cycle** 🚀
