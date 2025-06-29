import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Lê os códigos do arquivo
with open('codigos.txt', 'r', encoding='utf-8') as f:
    codigos = [linha.strip() for linha in f if linha.strip()]

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.warframe.com/pt-br/promocode')
    wait = WebDriverWait(driver, 20)
    erros = []

    # 1. Clicar no botão 'Entrar' (busca robusta)
    try:
        print('Tentando encontrar o botão Entrar pelo texto...')
        botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Entrar') or contains(., 'ENTRAR')]")))
    except:
        try:
            print('Tentando encontrar o botão Entrar pelo href...')
            botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/pt-br/login']")))
        except Exception as e:
            print('Não foi possível encontrar o botão Entrar:', e)
            driver.quit()
            return
    print('Botão Entrar encontrado! Clicando...')
    botao_entrar.click()

    # 2. Preencher email e senha
    try:
        campo_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @placeholder='Endereço de E-mail']")))
        campo_email.clear()
        campo_email.send_keys(EMAIL)
        campo_senha = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password' or @placeholder='Senha']")))
        campo_senha.clear()
        campo_senha.send_keys(SENHA)
        time.sleep(1)
        # Usa TAB 5 vezes e ENTER para submeter o formulário
        for _ in range(5):
            campo_senha.send_keys(Keys.TAB)
            time.sleep(0.1)
        campo_senha.send_keys(Keys.ENTER)
        print('Pressionado TAB 5x e ENTER para login.')
    except Exception as e:
        print('Erro ao preencher login:', e)
        driver.quit()
        return

    # 3. Esperar redirecionamento para a tela de resgate e garantir elementos prontos
    try:
        wait.until(EC.presence_of_element_located((By.ID, "promoCode-input")))
        wait.until(EC.presence_of_element_located((By.ID, "promoCode-submit")))
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.ID, "promoCode-input")))
        wait.until(EC.presence_of_element_located((By.ID, "promoCode-submit")))
    except Exception as e:
        print('Não foi possível acessar a tela de resgate:', e)
        print('URL atual:', driver.current_url)
        driver.quit()
        return

    # 4. Processo de resgate dos códigos
    for codigo in codigos:
        try:
            # Garante que o campo está visível e focado
            input_codigo = wait.until(EC.element_to_be_clickable((By.ID, 'promoCode-input')))
            input_codigo.click()
            input_codigo.clear()
            input_codigo.send_keys(codigo)
            time.sleep(0.2)
            # Foca no botão e pressiona ENTER
            botao_aplicar = wait.until(EC.element_to_be_clickable((By.ID, 'promoCode-submit')))
            botao_aplicar.send_keys(Keys.ENTER)
            print(f'Código {codigo} enviado.')
            # Aguarda o modal de sucesso OU mensagem de erro
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Código Reivindicado') or contains(text(), 'CÓDIGO REIVINDICADO')]")), 5)
                time.sleep(0.5)
                # Pressiona TAB 1x e ENTER para fechar o modal
                body = driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.TAB)
                time.sleep(0.1)
                body.send_keys(Keys.ENTER)
                time.sleep(1)
            except:
                # Se não aparecer o modal de sucesso, verifica se apareceu mensagem de erro
                try:
                    erro_resgate = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'inválido') or contains(text(), 'resgatado anteriormente') or contains(text(), 'LIMITE DE UM POR CLIENTE')]")), 3)
                    print(f'Código {codigo} já resgatado ou inválido, pulando para o próximo.')
                    # Fecha o alerta se possível
                    try:
                        botao_fechar_erro = driver.find_element(By.XPATH, "//button[contains(@class, 'close') or contains(text(), '×')]")
                        botao_fechar_erro.click()
                        time.sleep(0.5)
                    except:
                        pass
                    continue
                except:
                    erros.append(f"{codigo}: Erro desconhecido ao tentar resgatar.")
                    continue
        except Exception as e:
            erros.append(f"{codigo}: {str(e)}")
            continue
    if erros:
        with open('erros_resgate.txt', 'w', encoding='utf-8') as f:
            for erro in erros:
                f.write(erro + '\n')
    driver.quit()
    print('Processo finalizado.')

if __name__ == '__main__':
    main()