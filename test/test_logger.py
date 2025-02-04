import os
import sys
from logger.logger import create_logger, specificfile

# Adicionando o diretório principal ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_create_error_logger():
    logger = create_logger("error_logger", "error")
    logger.error("Test log: Error occurred! | Teste de log: Erro ocorreu!")

    error_log = specificfile("error")
    assert os.path.exists(error_log)
    
    with open(error_log, "r") as f:
        logs = f.read()
        assert "Test log: Error occurred!" in logs
        assert "Teste de log: Erro ocorreu!" in logs

def test_create_user_logger():
    logger = create_logger("user_logger", "user")
    logger.info("Test log: User login success! | Teste de log: Login do usuário bem-sucedido!")

    user_log = specificfile("user")
    assert os.path.exists(user_log)
    
    with open(user_log, "r") as f:
        logs = f.read()
        assert "Test log: User login success!" in logs
        assert "Teste de log: Login do usuário bem-sucedido!" in logs

def test_create_other_logger():
    logger = create_logger("other_logger", "other")
    logger.warning("Test log: Unusual activity detected! | Teste de log: Atividade incomum detectada!")

    other_log = specificfile("other")
    assert os.path.exists(other_log)
    
    with open(other_log, "r") as f:
        logs = f.read()
        assert "Test log: Unusual activity detected!" in logs
        assert "Teste de log: Atividade incomum detectada!" in logs
