import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import os
from PIL import Image, ImageTk
import pyperclip
import random
import string


root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("500x400")# dimensões do programa

# cria uma pasta que vai armazenar arquivos txt. com as senhas geradas
pasta_senhas = os.path.join("senhas geradas")

# verifica se a pasta ja foi gerada, para não gera-la novamente
try:
    os.mkdir(pasta_senhas)
    print(f"Pastas criadas com sucesso! {pasta_senhas}")
except Exception as a:
    print(f"erro ao criar a pasta: {a}")


# layout do programa utilizando o tk.Canvas
layout = tk.Canvas(root, width=500, 
                height=480, 
                bg="#ebf5f7")
layout.pack()

# frame que vai servir como container para adcionar os widgets ao layout e ter um design melhor
frame1 = tk.Frame(root, borderwidth=1, 
                    relief="flat", bg="#ebf5f7",)
#relief (flat, raised, sunken, solid)
frame1.place(x=10, y=25, 
            width=480, 
            height=67 ) # move o frame no canvas

# onde estão todos os botões
frame2 = tk.Frame(root, borderwidth=1, 
                    relief="flat", bg="#ebf5f7")
#relief (flat, raised, sunken, solid)
frame2.place(x=10, y=180, 
            width=480, 
            height=210 )

#frame onde está o resultado da senha que é gerada
frame3 = tk.Frame(root, borderwidth=1, 
                    relief="sunken", 
                    background="#7aebff",
                    highlightbackground="#c8cbcc", 
                    highlightcolor="#c8cbcc", 
                    highlightthickness=1)
#relief (flat, raised, sunken, solid)
frame3.place(x=10, y=100, 
            width=480, 
            height=50 )


#layout.create_line(10, 50, 290, 50) # topo horizontal
#layout.create_line(10, 50, 10, 440) # esquerdo vertical
#layout.create_line(290, 50, 290, 440) # direito vertical
#layout.create_line(290, 440, 10, 440) # baixo horizontal



# estilo dos botões utilizando o ttk
style = ttk.Style()
style.theme_use('clam')

# label que cria um texto
titulo1 = tk.Label(frame1, text="Gerador de Senhas", 
                  fg="black",
                  bg="#ebf5f7", 
                  font=("Arial", 18, "bold"), 
                  )
titulo1.place(x=125, y=9)
#subtitulo
titulo2 = tk.Label(frame1, text="Crie sua senha simples e forte em um clique!", 
                  fg="black",
                  bg="#ebf5f7", 
                  font=("Arial", 10), 
                  )
titulo2.place(x=110, y=40)


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


# busca e carrega a imagem   
img1 = Image.open(r"C:\Users\ericC\OneDrive\Documentos\Gerador_Senhas\icons\\copiar.png")
img1 = img1.resize((22, 22))
img1_tk = ImageTk.PhotoImage(img1)

def copiar():
    global senha_atual
    pega = senha_atual
    pyperclip.copy(pega)
    messagebox.showinfo(f"Senha copiada!", f"Senha copiada para área de transferência")

     
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
style.configure("botao_copia.TButton", background="#7aebff")


# configura o estilo da animação do cursor ao passar pelo botão
style.map("TButton",
          background=[("active", "#66c9e7")], 
          foreground=[("active", "white")]
         )


botão_copia = ttk.Button(frame3, image=img1_tk, 
                            command=copiar,
                            style="botao_copia.TButton")
botão_copia.place(x=1, y=0)

# botão que chama a função que faz imprimir a senha gerada no layout
botão_gerar = ttk.Button(frame2, text="Gerar senha", 
                         command=atualiza_senha, 
                         style="TButton")
botão_gerar.place(x=20, y=15)

#botão que faz salvar a senha gerada
botão_salvar = ttk.Button(frame2, text="Salvar senha",
                            command=arquivo_senha,
                            style="TButton")
botão_salvar.place(x=178, y=15)

# faz fechar programa
botão_sair = ttk.Button(frame2, text="Sair",
                            command=fechar_app,
                            style="botao_sair.TButton")
botão_sair.place(x=335, y=15)


# label com a configuração do texto da senha gerada
label_resultado = tk.Label(frame3, 
                           font=("Arial", 14, "bold"), 
                           fg="#00008B", 
                           bg="#7aebff",
                           wraplength=280)
label_resultado.place(rely=0.5, relx=0.5, anchor="center")



root.mainloop()