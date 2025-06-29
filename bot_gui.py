import time
import threading
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class BotFrameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('TennoCodeHunter 🤖')
        self.geometry('900x780')
        self.resizable(False, False)

        # Background image
        self.bg_image = ctk.CTkImage(Image.open('thumb-1920-1197499.jpg'), size=(900, 780))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Overlay frame for content (com leve transparência)
        self.overlay = ctk.CTkFrame(self, fg_color=("#181c25", "#181c25"), corner_radius=24, width=860, height=740)
        self.overlay.place(relx=0.5, rely=0.5, anchor='center')

        # Header
        self.header = ctk.CTkLabel(self.overlay, text='TennoCodeHunter 🤖🚀', font=('Segoe UI Black', 32, 'bold'), text_color='#00eaff')
        self.header.pack(pady=(18, 2))
        self.subheader = ctk.CTkLabel(self.overlay, text='Automatize o resgate de códigos promocionais do Warframe', font=('Segoe UI', 17), text_color='#e0e0e0')
        self.subheader.pack(pady=(0, 18))

        # Frame de login
        self.login_frame = ctk.CTkFrame(self.overlay, fg_color='#23283a', corner_radius=16)
        self.login_frame.pack(pady=10, padx=10, fill='x')
        ctk.CTkLabel(self.login_frame, text='E-mail:', font=('Segoe UI', 15, 'bold')).grid(row=0, column=0, padx=10, pady=7, sticky='e')
        self.email_entry = ctk.CTkEntry(self.login_frame, width=340, font=('Segoe UI', 15))
        self.email_entry.grid(row=0, column=1, padx=10, pady=7)
        ctk.CTkLabel(self.login_frame, text='Senha:', font=('Segoe UI', 15, 'bold')).grid(row=1, column=0, padx=10, pady=7, sticky='e')
        self.senha_entry = ctk.CTkEntry(self.login_frame, width=340, font=('Segoe UI', 15), show='*')
        self.senha_entry.grid(row=1, column=1, padx=10, pady=7)

        # Seleção de arquivo de códigos
        self.file_frame = ctk.CTkFrame(self.overlay, fg_color='#23283a', corner_radius=16)
        self.file_frame.pack(pady=10, padx=10, fill='x')
        self.file_label = ctk.CTkLabel(self.file_frame, text='Arquivo de códigos: Nenhum selecionado', font=('Segoe UI', 13), text_color='#e0e0e0')
        self.file_label.pack(side='left', padx=10)
        self.file_button = ctk.CTkButton(self.file_frame, text='Selecionar arquivo', font=('Segoe UI', 13, 'bold'), command=self.select_file, fg_color='#00eaff', hover_color='#1565c0', text_color='#181c25')
        self.file_button.pack(side='right', padx=10)
        self.codigos = []
        self.codigos_status = []

        # Status, progresso e timer
        self.status_label = ctk.CTkLabel(self.overlay, text='Aguardando início...', font=('Segoe UI', 18, 'bold'), text_color='#00eaff')
        self.status_label.pack(pady=(18, 2))
        self.progress = ctk.CTkProgressBar(self.overlay, width=820, height=26, progress_color='#00eaff')
        self.progress.pack(pady=10)
        self.progress.set(0)
        self.timer_label = ctk.CTkLabel(self.overlay, text='⏱ Tempo: 00:00', font=('Segoe UI', 15, 'bold'), text_color='#e0e0e0')
        self.timer_label.pack(pady=(0, 8))
        self.start_time = None

        # Log visual
        self.log_box = ctk.CTkTextbox(self.overlay, width=820, height=320, font=('Consolas', 15), fg_color='#181c25', text_color='#e0e0e0', border_width=2, border_color='#00eaff')
        self.log_box.pack(pady=10)
        self.log_box.insert('end', '[INFO] Pronto para iniciar o resgate dos códigos.\n')
        self.log_box.configure(state='disabled')

        # Frame para o botão iniciar, fixo no rodapé
        self.button_frame = ctk.CTkFrame(self.overlay, fg_color='transparent')
        self.button_frame.pack(side='bottom', fill='x', pady=(0, 18))
        self.start_button = ctk.CTkButton(self.button_frame, text='Iniciar Bot', font=('Segoe UI', 18, 'bold'), command=self.start_bot_thread, fg_color='#00eaff', hover_color='#1565c0', text_color='#181c25', corner_radius=12, width=180, height=40)
        self.start_button.pack(pady=0)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if file_path:
            self.file_label.configure(text=f'Arquivo de códigos: {file_path.split("/")[-1]}')
            with open(file_path, 'r', encoding='utf-8') as f:
                self.codigos = [linha.strip() for linha in f if linha.strip()]
            self.codigos_status = ['🔴' for _ in self.codigos]
            self.log('[INFO] Lista de códigos carregada com sucesso.')
            self.update_codigos_output()
        else:
            self.log('[WARN] Nenhum arquivo selecionado.')

    def start_bot_thread(self):
        if not self.email_entry.get() or not self.senha_entry.get():
            self.log('[ERRO] Preencha o e-mail e a senha.')
            return
        if not self.codigos:
            self.log('[ERRO] Selecione um arquivo de códigos.')
            return
        self.start_button.configure(state='disabled')
        self.start_time = time.time()
        self.update_timer()
        threading.Thread(target=self.run_bot, daemon=True).start()

    def update_timer(self):
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            mins, secs = divmod(elapsed, 60)
            self.timer_label.configure(text=f'⏱ Tempo: {mins:02d}:{secs:02d}')
            self.after(1000, self.update_timer)

    def log(self, msg, tipo='INFO'):
        self.log_box.configure(state='normal')
        if tipo == 'INFO':
            self.log_box.insert('end', f'🛈 {msg}\n')
        elif tipo == 'SUCESSO':
            self.log_box.insert('end', f'✔️ {msg}\n')
        elif tipo == 'ERRO':
            self.log_box.insert('end', f'❌ {msg}\n')
        elif tipo == 'WARN':
            self.log_box.insert('end', f'⚠️ {msg}\n')
        else:
            self.log_box.insert('end', f'{msg}\n')
        self.log_box.see('end')
        self.log_box.configure(state='disabled')

    def set_status(self, msg):
        self.status_label.configure(text=msg)

    def set_progress(self, value):
        self.progress.set(value)

    def update_codigos_output(self):
        self.log_box.configure(state='normal')
        self.log_box.insert('end', '\n[LISTA DE CÓDIGOS]\n')
        for idx, (codigo, status) in enumerate(zip(self.codigos, self.codigos_status), 1):
            if status == '🟢':
                self.log_box.insert('end', f'{status} {codigo}\n', 'green')
            elif status == '🔴':
                self.log_box.insert('end', f'{status} {codigo}\n', 'red')
            else:
                self.log_box.insert('end', f'{status} {codigo}\n')
        self.log_box.insert('end', '\n')
        self.log_box.tag_config('green', foreground='#00FF00')
        self.log_box.tag_config('red', foreground='#FF5555')
        self.log_box.see('end')
        self.log_box.configure(state='disabled')

    def run_bot(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        codigos = self.codigos
        self.set_status('Iniciando navegador...')
        self.log('Iniciando navegador...')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.warframe.com/pt-br/promocode?code=')
        wait = WebDriverWait(driver, 20)
        erros = []
        total = len(codigos)
        try:
            # Login
            self.set_status('Realizando login...')
            self.log('Clicando em Entrar...')
            try:
                botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Entrar') or contains(., 'ENTRAR')]")))
            except:
                botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/pt-br/login']")))
            botao_entrar.click()
            campo_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @placeholder='Endereço de E-mail']")))
            campo_email.clear()
            campo_email.send_keys(email)
            campo_senha = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password' or @placeholder='Senha']")))
            campo_senha.clear()
            campo_senha.send_keys(senha)
            time.sleep(1)
            for _ in range(5):
                campo_senha.send_keys(Keys.TAB)
                time.sleep(0.1)
            campo_senha.send_keys(Keys.ENTER)
            self.log('Login enviado, aguardando tela de resgate...')
            wait.until(EC.presence_of_element_located((By.ID, "promoCode-input")))
            wait.until(EC.presence_of_element_located((By.ID, "promoCode-submit")))
            time.sleep(2)
            driver.refresh()
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, "promoCode-input")))
            wait.until(EC.presence_of_element_located((By.ID, "promoCode-submit")))
            self.set_status('Resgatando códigos...')
            self.log('Iniciando resgate dos códigos...')
            # Resgate dos códigos
            for idx, codigo in enumerate(codigos, 1):
                try:
                    input_codigo = wait.until(EC.element_to_be_clickable((By.ID, 'promoCode-input')))
                    input_codigo.click()
                    input_codigo.clear()
                    input_codigo.send_keys(codigo)
                    time.sleep(0.2)
                    botao_aplicar = wait.until(EC.element_to_be_clickable((By.ID, 'promoCode-submit')))
                    botao_aplicar.send_keys(Keys.ENTER)
                    self.set_status(f'Resgatando código {idx}/{total}: {codigo}')
                    self.log(f'[{idx}/{total}] Resgatando: {codigo}...', tipo='INFO')
                    # Aguarda modal de sucesso ou erro
                    try:
                        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Código Reivindicado') or contains(text(), 'CÓDIGO REIVINDICADO')]")), 5)
                        time.sleep(0.5)
                        body = driver.find_element(By.TAG_NAME, 'body')
                        body.send_keys(Keys.TAB)
                        time.sleep(0.1)
                        body.send_keys(Keys.ENTER)
                        time.sleep(1)
                        self.log(f'🟢 {codigo} RESGATADO COM SUCESSO!', tipo='SUCESSO')
                        self.codigos_status[idx-1] = '🟢'
                    except:
                        # Verifica erro
                        try:
                            erro_resgate = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'inválido') or contains(text(), 'resgatado anteriormente') or contains(text(), 'LIMITE DE UM POR CLIENTE')]")), 3)
                            self.log(f'🔴 {codigo} JÁ RESGATADO OU INVÁLIDO.', tipo='WARN')
                            self.codigos_status[idx-1] = '🔴'
                            try:
                                botao_fechar_erro = driver.find_element(By.XPATH, "//button[contains(@class, 'close') or contains(text(), '×')]")
                                botao_fechar_erro.click()
                                time.sleep(0.5)
                            except:
                                pass
                        except:
                            self.log(f'🔴 {codigo} ERRO DESCONHECIDO.', tipo='ERRO')
                            self.codigos_status[idx-1] = '🔴'
                            erros.append(f"{codigo}: Erro desconhecido ao tentar resgatar.")
                    self.set_progress(idx/total)
                    self.update_codigos_output()
                except Exception as e:
                    msg = str(e)
                    if "element click intercepted" in msg:
                        self.log(f'🔴 {codigo} FALHA: Não foi possível clicar no campo de código. Feche pop-ups ou banners e tente novamente.', tipo='ERRO')
                    else:
                        self.log(f'🔴 {codigo} FALHA: {msg.splitlines()[0]}', tipo='ERRO')
                    self.codigos_status[idx-1] = '🔴'
                    erros.append(f"{codigo}: {msg}")
                    self.set_progress(idx/total)
                    self.update_codigos_output()
            self.set_status('Processo finalizado.')
            self.log('Processo finalizado.', tipo='SUCESSO')
            if erros:
                with open('erros_resgate.txt', 'w', encoding='utf-8') as f:
                    for erro in erros:
                        f.write(erro + '\n')
        except Exception as e:
            self.set_status('Erro fatal. Veja o log.')
            self.log(f'Erro fatal: {str(e)}', tipo='ERRO')
        finally:
            driver.quit()
            self.start_time = None

if __name__ == '__main__':
    app = BotFrameApp()
    app.mainloop() 