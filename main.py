import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import os
import random
import string


root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("300x480")# dimensões do programa

# cria uma pasta que vai armazenar arquivos txt. com as senhas geradas
pasta_senhas = os.path.join("senhas geradas")

# verifica se a pasta ja foi gerada, para não gera-la novamente
try:
    os.mkdir(pasta_senhas)
    print(f"Pastas criadas com sucesso! {pasta_senhas}")
except Exception as a:
    print(f"erro ao criar a pasta: {a}")


# layout do programa utilizando o tk.Canvas
layout = tk.Canvas(root, width=300, 
                height=480, 
                bg="#00FFFF")
layout.pack()

# frame que vai servir como container para adcionar os widgets ao layout e ter um design melhor
frame = tk.Frame(layout, bg="#00FFFF")
frame.place(relx=0.5, rely=0.5, anchor="center") # centraliza o frame no canvas

layout.create_line(10, 50, 290, 50) # topo horizontal
layout.create_line(10, 50, 10, 440) # esquerdo vertical
layout.create_line(290, 50, 290, 440) # direito vertical
layout.create_line(290, 440, 10, 440) # baixo horizontal



# estilo dos botões utilizando o ttk
style = ttk.Style()
style.theme_use('clam')

# label que cria um texto
titulo = tk.Label(frame, text="Gerador de Senhas", 
                  fg="red", 
                  font=("Georgia", 18, "bold"), 
                  bg="lightgreen")
titulo.pack(pady=45)


# função principal que contem o código capaz de gerar a senha de forma aleatória
def senha_gerada():
    tamanho = 10
    pontos = "!@#$%&*-_=+?/|" #variavel com pontos unicos
    aleatorio = string.ascii_letters + string.hexdigits + pontos
    senha = "".join(random.choices(aleatorio, k=tamanho))
    return senha


senha_atual = "" # variavel global armazena senha gerada


# função atualiza no layout   
def atualiza_senha():
    global senha_atual 
    senha_atual = senha_gerada() # armazena a senha gerada
    label_resultado.config(text=f"{senha_atual}") # imprime a senha gerada no layout


# função que salva a senha
def arquivo_senha():
    global senha_atual
    if not senha_atual:  # Se não há senha gerada não retorna nada
        return
    
    # Nome único com timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo = os.path.join(pasta_senhas, f"senha_{timestamp}.txt")

    try:
        with open(arquivo, "w") as f:
            f.write(senha_atual)
            print(f"Senha salva com sucesso: {arquivo}")
            messagebox.showinfo(f"Senha salva com sucesso", f"sua senha foi salva em:\n {arquivo} ") # Feedback visual 
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

     
def fechar_app():
    root.quit()

    
# configura o estilo do botão 
style.configure("TButton", font=("Arial", 13, "bold"),
                foreground="white", # Cor do texto
                background="#0BCA6B", # Cor de fundo
                padding=10, # Adiciona um preenchimento interno ao botão
                relief="flat" # Aparência plana
               )


style.configure("botao_sair.TButton", background="red")


# configura o estilo da animação do cursor ao passar pelo botão
style.map("TButton",
          background=[("active", "#66c9e7")], 
          foreground=[("active", "white")]
         )

# botão que chama a função que faz imprimir a senha gerada no layout
botão_gerar = ttk.Button(frame, text="Gerar senha", 
                         command=atualiza_senha, 
                         style="TButton")
botão_gerar.pack(pady=20)

#botão que faz salvar a senha gerada
botão_salvar = ttk.Button(frame, text="Salvar senha",
                            command=arquivo_senha,
                            style="TButton")
botão_salvar.pack(after=botão_gerar)

# faz fechar programa
botão_sair = ttk.Button(frame, text="Sair",
                            command=fechar_app,
                            style="botao_sair.TButton")
botão_sair.pack(pady=20, after=botão_salvar)


# label com a configuração do texto da senha gerada
label_resultado = tk.Label(frame, text="",
                           font=("Courier", 14, "bold"), 
                           fg="#00008B", 
                           bg="lightgreen", 
                           wraplength=280)
label_resultado.pack(pady=5, before=botão_gerar)



root.mainloop()