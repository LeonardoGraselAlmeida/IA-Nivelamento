#!/bin/bash

# Script para executar linting local
# Uso: ./run-lint.sh

set -e

echo "🚀 Instalando dependências de linting..."
pip install -r requirements.txt

echo "🔧 Executando linting local..."
python lint.py

echo "✅ Linting concluído!"
