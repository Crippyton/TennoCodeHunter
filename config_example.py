"""
Exemplo de configuração de ambiente para TennoCodeHunter
Copie este arquivo para config_local.py e personalize as configurações
"""

# Configurações do navegador
BROWSER_HEADLESS = False
BROWSER_TIMEOUT = 20
BROWSER_WINDOW_SIZE = (1200, 800)

# Delays personalizados (em segundos)
DELAY_BETWEEN_CODES = 0.2
DELAY_AFTER_LOGIN = 1.0
DELAY_AFTER_SUBMIT = 0.5

# Configurações de retry
MAX_RETRIES = 3
RETRY_DELAY = 1.0

# Configurações de log
LOG_LEVEL = 'INFO'
LOG_FILE = 'erros_resgate.txt'

# URLs (não altere a menos que necessário)
WARFRAME_PROMOCODE_URL = 'https://www.warframe.com/pt-br/promocode'
WARFRAME_LOGIN_URL = 'https://www.warframe.com/pt-br/login'

# Configurações avançadas
ENABLE_DEBUG_MODE = False
SAVE_SCREENSHOTS_ON_ERROR = False
SCREENSHOT_DIR = 'screenshots/'

# Configurações de validação
MIN_CODE_LENGTH = 3
MAX_CODE_LENGTH = 50
ALLOWED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' 