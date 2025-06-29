# Guia de Contribuição 🤝

Obrigado por considerar contribuir com o TennoCodeHunter! Este documento fornece diretrizes para contribuições.

## 🚀 Como Contribuir

### 1. Fork e Clone
1. Faça um fork do repositório
2. Clone seu fork localmente:
   ```bash
   git clone https://github.com/seu-usuario/TennoCodeHunter.git
   cd TennoCodeHunter
   ```

### 2. Configurar Ambiente
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure o ambiente de desenvolvimento:
   ```bash
   cp config_example.py config_local.py
   # Edite config_local.py conforme necessário
   ```

### 3. Desenvolvimento
1. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
2. Faça suas alterações
3. Execute os testes:
   ```bash
   python -m pytest test_utils.py -v
   ```
4. Formate o código:
   ```bash
   black .
   ```

### 4. Commit e Push
1. Adicione suas alterações:
   ```bash
   git add .
   ```
2. Faça commit com mensagem descritiva:
   ```bash
   git commit -m "feat: adiciona nova funcionalidade X"
   ```
3. Push para seu fork:
   ```bash
   git push origin feature/nova-funcionalidade
   ```

### 5. Pull Request
1. Abra um Pull Request no GitHub
2. Descreva suas alterações
3. Aguarde revisão

## 📋 Padrões de Código

### Python
- Use Python 3.7+
- Siga PEP 8
- Use type hints quando possível
- Adicione docstrings para funções

### Commits
Use o padrão Conventional Commits:
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` documentação
- `style:` formatação
- `refactor:` refatoração
- `test:` testes
- `chore:` manutenção

### Estrutura de Arquivos
```
TennoCodeHunter/
├── bot_gui.py          # Interface principal
├── bot.py              # Script CLI
├── config.py           # Configurações
├── utils.py            # Utilitários
├── test_utils.py       # Testes
├── requirements.txt    # Dependências
├── README.md          # Documentação
└── .gitignore         # Git ignore
```

## 🐛 Reportando Bugs

1. Verifique se o bug já foi reportado
2. Use o template de issue
3. Inclua:
   - Sistema operacional
   - Versão do Python
   - Passos para reproduzir
   - Logs de erro

## 💡 Sugerindo Melhorias

1. Descreva a funcionalidade desejada
2. Explique o benefício
3. Se possível, forneça mockup ou exemplo

## 🧪 Testes

### Executar Testes
```bash
# Todos os testes
python -m pytest

# Testes específicos
python -m pytest test_utils.py -v

# Com cobertura
python -m pytest --cov=utils
```

### Adicionar Testes
- Teste novas funcionalidades
- Mantenha cobertura > 80%
- Use fixtures quando apropriado

## 📝 Documentação

### Atualizar README
- Documente novas funcionalidades
- Atualize instruções de instalação
- Adicione exemplos de uso

### Docstrings
```python
def minha_funcao(param1: str, param2: int) -> bool:
    """
    Descrição da função.
    
    Args:
        param1: Descrição do parâmetro 1
        param2: Descrição do parâmetro 2
    
    Returns:
        Descrição do retorno
    
    Raises:
        ValueError: Quando algo dá errado
    """
    pass
```

## 🔒 Segurança

- Nunca commite credenciais
- Use variáveis de ambiente
- Valide entrada do usuário
- Sanitize dados

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.

## 🎉 Reconhecimento

Contribuidores serão listados no README e releases.

---

**Obrigado por contribuir! 🚀** 