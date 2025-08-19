@echo off
echo 🔹 Instalando dependências...
C:\Users\ribei\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming\Python\Scripts\poetry install

echo 🔹 Limpando build anterior...
rmdir /S /Q dist
rmdir /S /Q build

echo 🔹 Gerando executável...
C:\Users\ribei\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming\Python\Scripts\poetry run pyinstaller --onefile main.py --name piadas_chuck

echo ✅ Build concluído! Executável em dist\piadas_chuck.exe