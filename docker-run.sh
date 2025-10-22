#!/bin/bash

# Script para facilitar o uso do Docker com o projeto Python

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🐳 Docker Python Project Runner${NC}"
echo "=================================="

# Verificar se Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker não está rodando. Por favor, inicie o Docker primeiro.${NC}"
    exit 1
fi

# Nome da imagem
IMAGE_NAME="ia-nivelamento-python"

# Função para build
build_image() {
    echo -e "${YELLOW}🔨 Construindo imagem Docker...${NC}"
    docker build -t $IMAGE_NAME .
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Imagem construída com sucesso!${NC}"
    else
        echo -e "${RED}❌ Erro ao construir a imagem${NC}"
        exit 1
    fi
}

# Função para executar
run_container() {
    echo -e "${YELLOW}🚀 Executando container...${NC}"
    docker run --rm -it \
        --name ia-nivelamento-container \
        -v "$(pwd):/app" \
        -w /app \
        $IMAGE_NAME
}

# Função para shell interativo
run_shell() {
    echo -e "${YELLOW}🐚 Abrindo shell interativo...${NC}"
    docker run --rm -it \
        --name ia-nivelamento-shell \
        -v "$(pwd):/app" \
        -w /app \
        $IMAGE_NAME \
        /bin/bash
}

# Menu principal
case "${1:-run}" in
    "build")
        build_image
        ;;
    "run")
        build_image
        run_container
        ;;
    "shell")
        build_image
        run_shell
        ;;
    "help"|"-h"|"--help")
        echo "Uso: $0 [comando]"
        echo ""
        echo "Comandos:"
        echo "  build   - Apenas constrói a imagem Docker"
        echo "  run     - Constrói e executa o script Python (padrão)"
        echo "  shell   - Constrói e abre shell interativo"
        echo "  help    - Mostra esta ajuda"
        ;;
    *)
        echo -e "${RED}❌ Comando desconhecido: $1${NC}"
        echo "Use '$0 help' para ver os comandos disponíveis"
        exit 1
        ;;
esac

