#!/usr/bin/env bash
set -euo pipefail

echo "=> Atualizando apt e instalando utilitários..."
sudo apt-get update -y
sudo apt-get install -y zip unzip curl

echo "=> Garantindo pip atualizado..."
python3 -m pip install --upgrade pip || true

echo "=> runner preparado."
