# TennoCodeHunter 🤖

Um bot inteligente em Python com interface gráfica moderna para automatizar o resgate de códigos promocionais no site do Warframe.

## ✨ Funcionalidades

- 🎨 **Interface gráfica intuitiva** com tema escuro moderno (CustomTkinter)
- 🤖 **Automação completa** do processo de resgate de códigos
- 📊 **Feedback visual em tempo real**: códigos resgatados (🟢), falhas (🔴)
- 📈 **Barra de progresso** e log detalhado de operações
- 📁 **Seleção de arquivo** `.txt` com lista de códigos
- 🔐 **Login seguro**: usuário informa credenciais na interface
- ⏱️ **Contador de tempo** de execução
- 📝 **Geração de logs** de erros em arquivo
- 🚀 **WebDriver automático** com ChromeDriver Manager

## 🛠️ Requisitos

- Python 3.7+
- Google Chrome instalado
- Conexão com internet

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/TennoCodeHunter.git
   cd TennoCodeHunter
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare seu arquivo de códigos:**
   - Copie `codigos_exemplo.txt` para `codigos.txt`
   - Adicione seus códigos promocionais (um por linha)
   - Remova os comentários (#) das linhas dos códigos

## 🚀 Como usar

1. **Execute a interface gráfica:**
   ```bash
   python bot_gui.py
   ```

2. **Configure o bot:**
   - Preencha seu **e-mail** e **senha** do Warframe
   - Selecione o arquivo `codigos.txt` com seus códigos
   - Clique em **"Iniciar Bot"**

3. **Acompanhe o progresso:**
   - O bot fará login automaticamente
   - Processará cada código da lista
   - Mostrará o status em tempo real
   - Salvará erros em `erros_resgate.txt`

## 📁 Estrutura do Projeto

```
TennoCodeHunter/
├── bot_gui.py          # Interface gráfica principal
├── bot.py              # Script de linha de comando
├── requirements.txt    # Dependências Python
├── codigos_exemplo.txt # Exemplo de arquivo de códigos
├── README.md          # Este arquivo
└── .gitignore         # Arquivos ignorados pelo Git
```

## ⚠️ Importante

- **Arquivo de códigos**: Deve conter um código por linha
- **Credenciais**: Nunca compartilhe seu arquivo `codigos.txt`
- **Uso responsável**: Respeite os termos de uso do Warframe
- **Chrome**: Deve estar instalado no sistema

## 🔧 Configuração Avançada

### Personalizar delays:
Edite o arquivo `bot_gui.py` e ajuste os valores de `time.sleep()` para:
- `time.sleep(0.2)` - Delay entre códigos
- `time.sleep(1)` - Delay após login

### Logs detalhados:
Os logs são salvos em:
- Interface: Log visual em tempo real
- Arquivo: `erros_resgate.txt` (apenas erros)

## 🐛 Solução de Problemas

### Bot não inicia:
- Verifique se o Chrome está instalado
- Confirme se as dependências foram instaladas
- Verifique a conexão com internet

### Login falha:
- Confirme e-mail e senha
- Verifique se a conta não está bloqueada
- Tente fazer login manual no site primeiro

### Códigos não são resgatados:
- Verifique se os códigos são válidos
- Confirme se não foram resgatados anteriormente
- Aguarde alguns segundos entre tentativas

## 📄 Licença

Este projeto é desenvolvido para fins educacionais e uso pessoal. 
Respeite os termos de serviço do Warframe.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

---

**Desenvolvido com ❤️ para a comunidade Warframe** 