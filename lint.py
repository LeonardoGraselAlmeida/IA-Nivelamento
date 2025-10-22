#!/usr/bin/env python3
"""
Script para executar linting local nos arquivos Python do projeto.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Executa um comando e retorna o resultado."""
    print(f"\n🔍 {description}")
    print(f"Executando: {' '.join(command)}")
    print("-" * 50)

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("✅ Sucesso!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erro encontrado!")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def check_todo_comments():
    """Verifica comentários TODO/FIXME nos arquivos Python."""
    print("\n🔍 Verificando comentários TODO/FIXME")
    print("-" * 50)

    todo_found = False
    for py_file in Path(".").rglob("*.py"):
        if "venv" in str(py_file) or ".venv" in str(py_file):
            continue

        try:
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()
                if "TODO" in content or "FIXME" in content:
                    print(f"⚠️  {py_file}: Encontrados comentários TODO/FIXME")
                    todo_found = True
        except Exception as e:
            print(f"❌ Erro ao ler {py_file}: {e}")

    if not todo_found:
        print("✅ Nenhum comentário TODO/FIXME encontrado")
    return not todo_found


def main():
    """Função principal para executar todos os linters."""
    print("🚀 Iniciando processo de linting...")

    # Verifica se estamos no diretório correto
    if not Path("requirements.txt").exists():
        print("❌ Erro: Execute este script na raiz do projeto")
        sys.exit(1)

    # Lista de comandos para executar
    commands = [
        (["black", "--check", "--diff", "."], "Verificando formatação com Black"),
        (["isort", "--check-only", "--diff", "."], "Verificando ordenação de imports"),
        (["flake8", "."], "Executando linting com Flake8"),
        (["mypy", ".", "--ignore-missing-imports"], "Verificando tipos com MyPy"),
    ]

    # Executa todos os comandos
    all_passed = True
    for command, description in commands:
        if not run_command(command, description):
            all_passed = False

    # Verifica comentários TODO/FIXME
    if not check_todo_comments():
        all_passed = False

    # Resultado final
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 Todos os checks de linting passaram!")
        sys.exit(0)
    else:
        print("❌ Alguns checks de linting falharam. Verifique os erros acima.")
        sys.exit(1)


if __name__ == "__main__":
    main()
