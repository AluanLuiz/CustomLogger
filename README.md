
# Custom Logger 📜

## 📌 Sobre | About
O **Custom Logger** foi criado com o intuito de poupar tempo nos projetos, fornecendo diretórios e arquivos pré-definidos, com possibilidade de modificações, para facilitar o gerenciamento de logs.

The **Custom Logger** was created to save time on projects by providing predefined directories and files, with the ability to make modifications, to streamline log management.

O **Custom Logger** é uma ferramenta flexível para gerar e armazenar logs em diferentes níveis (`INFO`, `ERROR`, `WARNING`, etc.), permitindo que você organize registros de eventos em seus projetos de forma eficiente.

The **Custom Logger** is a flexible tool for generating and storing logs at different levels (`INFO`, `ERROR`, `WARNING`, etc.), allowing you to organize event records in your projects efficiently.

---

## 🚀 Funcionalidades | Features
✅ Suporte a múltiplos níveis de logs: `INFO`, `ERROR`, `DEBUG`, `WARNING`.  
✅ Armazena logs em arquivos organizados (`userLog.log`, `errors.log`, etc.).  
✅ Criação automática da pasta de logs.  
✅ Testes automatizados com `pytest`.  

✅ Supports multiple log levels: `INFO`, `ERROR`, `DEBUG`, `WARNING`.  
✅ Stores logs in organized files (`userLog.log`, `errors.log`, etc.).  
✅ Automatically creates the logs folder.  
✅ Automated testing with `pytest`.  

---

## 📂 Estrutura do Projeto | Project Structure
```plaintext
custom_logger/
│── logger/                    # Pacote principal do logger
│   ├── __init__.py
│   ├── logger.py              # Código principal do logger
│── test/                       # Pasta de testes automatizados
│   ├── test_logger.py
│── logs/                       # Diretório onde os logs serão armazenados
│── LICENSE                     # Licença do projeto
│── pyproject.toml             # Configuração do projeto
│── README.md                  # Documentação do projeto
│── .gitignore                 # Ignora arquivos desnecessários no repositório
```

---

## 🔧 Instalação | Installation

### 🐍 Pré-requisitos | Prerequisites
- Python 3.8+  
- `pip` instalado  

### 📥 Instale via GitHub | Install via GitHub
```bash
git clone https://github.com/AluanLuiz/CustomLogger.git
cd custom_logger
```

---

## 🛠️ Como Usar | How to Use

### Exemplo de uso básico | Basic usage example
```python
from logger.logger import create_logger

# Criando um logger para erros | Creating an error logger
error_logger = create_logger("error_logger", "error")
error_logger.error("⚠️ Um erro ocorreu! | An error occurred!")

# Criando um logger para atividades do usuário | Creating a user activity logger
user_logger = create_logger("user_logger", "user")
user_logger.info("🔑 Usuário fez login! | User logged in!")
```

---

## ✅ Como Executar Testes | Running Tests

🔹 Instale o pytest | Install pytest  
```bash
pip install pytest
```

🔹 Rode os testes | Run the tests  
```bash
pytest test/
```

Para um relatório mais detalhado:  
For a more detailed report:
```bash
pytest -v
```

---

## ⚖️ Licença | License
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## ✨ Contribuição | Contribution
Sinta-se à vontade para contribuir! Se encontrar algum problema ou tiver sugestões, abra uma issue ou envie um pull request.

Feel free to contribute! If you find any issues or have suggestions, open an issue or submit a pull request.
