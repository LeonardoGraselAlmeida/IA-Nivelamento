# Guia de Linting

Este projeto utiliza várias ferramentas de linting e formatação de código Python para garantir a qualidade e consistência do código.

## 🛠️ Ferramentas Utilizadas

- **Black**: Formatador de código automático
- **isort**: Organizador de imports
- **Flake8**: Linter para detectar erros e problemas de estilo
- **MyPy**: Verificador de tipos estáticos (opcional)

## 🚀 Como Executar o Linting

### Método 1: Script Python (Recomendado)

```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate

# Execute o script de linting
python lint.py
```

### Método 2: Script Bash

```bash
# Torna o script executável (apenas primeira vez)
chmod +x run-lint.sh

# Execute o script
./run-lint.sh
```

### Método 3: Comandos Individuais

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Verificar formatação com Black
black --check --diff .

# Corrigir formatação automaticamente com Black
black .

# Verificar ordenação de imports
isort --check-only --diff .

# Corrigir ordenação de imports
isort .

# Executar linting com Flake8
flake8 .

# Verificar tipos com MyPy
mypy . --ignore-missing-imports
```

## 🔧 Corrigir Problemas Automaticamente

Para corrigir automaticamente a maioria dos problemas:

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Corrija formatação
black .

# Corrija ordenação de imports
isort .

# Execute o linting novamente para verificar
python lint.py
```

## 📋 Pipeline CI/CD

A pipeline de linting é executada automaticamente no GitHub Actions em:

- Push para branches `main` e `develop`
- Pull requests para branches `main` e `develop`
- Execução manual (workflow_dispatch)

### Arquivo da Pipeline

`.github/workflows/lint.yml`

## ⚙️ Configurações

### Black

- **Arquivo**: `pyproject.toml`
- **Comprimento de linha**: 88 caracteres
- **Python target**: 3.11

### isort

- **Arquivo**: `pyproject.toml`
- **Profile**: black (compatível com Black)
- **Comprimento de linha**: 88 caracteres

### Flake8

- **Arquivo**: `.flake8`
- **Comprimento máximo de linha**: 180 caracteres
- **Complexidade máxima**: 10

### MyPy

- **Arquivo**: `pyproject.toml`
- **Python version**: 3.11
- **Modo**: Não estrito (permite código sem type hints)

## 🎯 Boas Práticas

1. **Execute o linting antes de fazer commit**

   ```bash
   python lint.py
   ```

2. **Corrija problemas automaticamente quando possível**

   ```bash
   black .
   isort .
   ```

3. **Revise manualmente os problemas de Flake8**

   - Alguns problemas requerem correção manual
   - Evite código muito complexo (complexidade > 10)

4. **Type hints são opcionais mas recomendados**
   - MyPy ajuda a detectar erros de tipo
   - Use type hints em funções públicas

## 📝 Ignorando Erros

### Ignorar linha específica no Flake8

```python
resultado = funcao_muito_longa()  # noqa: E501
```

### Ignorar erro específico no MyPy

```python
valor = funcao_sem_tipos()  # type: ignore
```

## 🔍 Verificação de Comentários TODO/FIXME

O script de linting também verifica comentários TODO/FIXME:

- ⚠️ Alerta quando encontrados
- Use para rastrear trabalho pendente
- Resolva antes de fazer merge para produção

## 🐛 Troubleshooting

### Erro: "command not found"

```bash
# Instale as dependências de linting
pip install -r requirements.txt
```

### Erro: Conflitos entre Black e Flake8

- As configurações já estão ajustadas para evitar conflitos
- Black tem prioridade sobre Flake8 em caso de discordância

### MyPy reporta muitos erros

- MyPy está configurado em modo permissivo
- Erros de tipo são apenas avisos (continue-on-error: true)

## 📚 Recursos Adicionais

- [Black Documentation](https://black.readthedocs.io/)
- [isort Documentation](https://pycqa.github.io/isort/)
- [Flake8 Documentation](https://flake8.pycqa.org/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
