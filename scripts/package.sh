#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="dist"
rm -rf "${OUT_DIR}"
mkdir -p "${OUT_DIR}"

ZIP_NAME="${OUT_DIR}/piadas_chuck_project-$(date +%Y%m%d%H%M%S).zip"
echo "=> Criando pacote ${ZIP_NAME}"
zip -r "${ZIP_NAME}" . -x ".git/*" "dist/*" "tests/*"

echo "=> Pacote criado em ${ZIP_NAME}"
ls -l "${OUT_DIR}"
