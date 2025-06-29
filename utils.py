"""
Utilitários para o TennoCodeHunter
"""

import re
import time
import logging
from typing import List, Dict, Optional
from config import VALIDATION, LOG_CONFIG, DELAYS

def setup_logging() -> logging.Logger:
    """Configura o sistema de logging"""
    logger = logging.getLogger('TennoCodeHunter')
    logger.setLevel(getattr(logging, LOG_CONFIG['log_level']))
    
    # Handler para arquivo
    file_handler = logging.FileHandler(LOG_CONFIG['error_file'], encoding='utf-8')
    file_handler.setLevel(logging.ERROR)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formato
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def validate_code(code: str) -> bool:
    """Valida se um código promocional é válido"""
    if not code or not isinstance(code, str):
        return False
    
    code = code.strip().upper()
    
    # Verifica comprimento
    if len(code) < VALIDATION['min_code_length'] or len(code) > VALIDATION['max_code_length']:
        return False
    
    # Verifica caracteres permitidos
    for char in code:
        if char not in VALIDATION['allowed_chars']:
            return False
    
    return True

def load_codes_from_file(filename: str) -> List[str]:
    """Carrega códigos de um arquivo, removendo linhas vazias e comentários"""
    codes = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Ignora linhas vazias e comentários
                if line and not line.startswith('#'):
                    if validate_code(line):
                        codes.append(line.upper())
                    else:
                        print(f"Código inválido ignorado: {line}")
        return codes
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filename}")
        return []
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return []

def save_errors_to_file(errors: List[str], filename: str = None) -> None:
    """Salva erros em arquivo"""
    if not filename:
        filename = LOG_CONFIG['error_file']
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for error in errors:
                f.write(f"{error}\n")
        print(f"Erros salvos em: {filename}")
    except Exception as e:
        print(f"Erro ao salvar arquivo de erros: {e}")

def format_time(seconds: int) -> str:
    """Formata tempo em segundos para formato MM:SS"""
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def calculate_progress(current: int, total: int) -> float:
    """Calcula progresso como valor entre 0 e 1"""
    if total == 0:
        return 0.0
    return min(current / total, 1.0)

def safe_delay(delay_type: str) -> None:
    """Executa delay de forma segura baseado no tipo"""
    delay_value = DELAYS.get(delay_type, 0.1)
    time.sleep(delay_value)

def clean_filename(filename: str) -> str:
    """Remove caracteres inválidos de nomes de arquivo"""
    # Remove caracteres inválidos para Windows
    invalid_chars = r'[<>:"/\\|?*]'
    return re.sub(invalid_chars, '_', filename)

def create_backup_filename(filename: str) -> str:
    """Cria nome de arquivo de backup com timestamp"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = filename.rsplit('.', 1)
    return f"{name}_{timestamp}.{ext}"

def is_valid_email(email: str) -> bool:
    """Valida formato de e-mail"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def sanitize_input(text: str) -> str:
    """Remove caracteres perigosos de entrada do usuário"""
    # Remove caracteres de controle e scripts
    text = re.sub(r'[<>&"\']', '', text)
    return text.strip()

def get_system_info() -> Dict[str, str]:
    """Obtém informações do sistema"""
    import platform
    import sys
    
    return {
        'os': platform.system(),
        'os_version': platform.version(),
        'python_version': sys.version,
        'architecture': platform.architecture()[0]
    } 