## Piadas do Chuck Norris

Aplicação simples em **Python** que consome a [API pública do Chuck Norris](https://api.chucknorris.io/) para exibir piadas aleatórias no terminal.  
O projeto utiliza **[Poetry](https://python-poetry.org/)** para gerenciamento de dependências e **PyInstaller** para gerar um executável final.

##

### 📌 Funcionalidades
- Buscar uma piada aleatória da API do Chuck Norris.
- Exibir diretamente no terminal.

##

### 🚀 Tecnologias utilizadas
- [Python 3.10+](https://www.python.org/)
- [Poetry](https://python-poetry.org/) — gerenciamento de dependências e build
- [Requests](https://pypi.org/project/requests/) — consumo da API
- [PyInstaller](https://pyinstaller.org/) — criação do executável

##

### ⚙️ Pré-requisitos

Antes de começar, você precisa ter instalado:
- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

> Para instalar o Poetry no Windows:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

```
##

### 🛠️ Configuração do projeto 

Clone este repositório:
```powershell
git clone https://github.com/laviniaribeiro/piadas_chuck.git
cd piadas_chuck

```

Instale as dependências com o Poetry:
```powershell
poetry install

```

Ative o ambiente virtual do Poetry:
```powershell
poetry shell

```

### ▶️ Executando o projeto

Rodar o app diretamente pelo Poetry:
```powershell
poetry run python piadas_chuck/main.py

```

Exemplo de saída
```powershell
--- Piada do Chuck Norris ---
Chuck Norris counted to infinity. Twice.

```

##


### ❌ Erros de Merge
Durante a execução do projeto, foram gerados propositalmente erros de merge, pois houveram alterações simultaneas na mesma linha. 
O conflito foi resolvido alterando novamente a linha e deixando comum aos dois contribuintes.


##

## Testes e regressões

Para garantir que a suíte de testes unitários está funcionando corretamente, criamos alguns casos de **regressão intencional**:

- Uma alteração foi feita propositalmente na função `obter()` para gerar um erro.
- Ao rodar os testes com:

```bash
python -m unittest test_chucknorris.py

```

##


### 👩‍💻 Feito por
[Lavínia V. Ribeiro Amaral](https://github.com/laviniaribeiro)



