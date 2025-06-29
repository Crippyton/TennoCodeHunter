"""
Configurações centralizadas para o TennoCodeHunter
"""

# Configurações da interface
GUI_CONFIG = {
    'title': 'TennoCodeHunter 🤖',
    'geometry': '900x780',
    'theme': 'dark',
    'color_theme': 'blue'
}

# Configurações do navegador
BROWSER_CONFIG = {
    'timeout': 20,  # Timeout em segundos para elementos
    'implicit_wait': 10,  # Espera implícita
    'page_load_timeout': 30,  # Timeout para carregamento de página
    'headless': False,  # Executar em modo headless (sem interface)
    'window_size': (1200, 800),  # Tamanho da janela do navegador
}

# Configurações de delays (em segundos)
DELAYS = {
    'between_codes': 0.2,  # Delay entre tentativas de códigos
    'after_login': 1.0,  # Delay após login
    'after_submit': 0.5,  # Delay após submeter código
    'tab_navigation': 0.1,  # Delay entre navegação por TAB
    'page_refresh': 2.0,  # Delay após refresh da página
}

# URLs
URLS = {
    'promocode_page': 'https://www.warframe.com/pt-br/promocode',
    'login_page': 'https://www.warframe.com/pt-br/login'
}

# Seletores CSS/XPath
SELECTORS = {
    'login_button': "//a[contains(., 'Entrar') or contains(., 'ENTRAR')]",
    'login_button_alt': "//a[@href='/pt-br/login']",
    'email_field': "//input[@type='email' or @placeholder='Endereço de E-mail']",
    'password_field': "//input[@type='password' or @placeholder='Senha']",
    'promo_input': 'promoCode-input',
    'promo_submit': 'promoCode-submit',
    'success_message': "//*[contains(text(), 'Código Reivindicado') or contains(text(), 'CÓDIGO REIVINDICADO')]",
    'error_message': "//*[contains(text(), 'inválido') or contains(text(), 'resgatado anteriormente') or contains(text(), 'LIMITE DE UM POR CLIENTE')]",
    'close_button': "//button[contains(@class, 'close') or contains(text(), '×')]"
}

# Configurações de log
LOG_CONFIG = {
    'error_file': 'erros_resgate.txt',
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'max_log_size': 1024 * 1024,  # 1MB
    'backup_count': 3
}

# Configurações de retry
RETRY_CONFIG = {
    'max_retries': 3,  # Máximo de tentativas por código
    'retry_delay': 1.0,  # Delay entre tentativas
    'retry_on_errors': ['timeout', 'element_not_found', 'network_error']
}

# Configurações de validação
VALIDATION = {
    'min_code_length': 3,
    'max_code_length': 50,
    'allowed_chars': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
} 