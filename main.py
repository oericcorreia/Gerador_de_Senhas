import tkinter as tk
from tkinter import ttk
import random
import string


root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("300x400")# dimensões do programa


# layout do programa utilizando o tk.Canvas
layout = tk.Canvas(root, width=300, 
                height=400, 
                bg="lightblue")
layout.pack(fill="both", expand=True)

# frame que vai servir como container para adcionar os widgets ao layout e ter um design melhor
frame = tk.Frame(layout, height=400, width=300, bg="lightblue")
frame.pack() # centraliza o frame no canvas

layout.create_line(10, 10, 290, 10)


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
    aleatorio = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choices(aleatorio, k=tamanho))
    return senha
    
# função que imprime a senha gerada no layout   
def atualiza():
    nova_senha = senha_gerada()
    label_resultado.config(text=f"{nova_senha}")
    
# configura o estilo do botão 
style.configure("TButton", font=("Arial", 13, "bold"),
                foreground="white", # Cor do texto
                background="#0BCA6B", # Cor de fundo
                padding=10, # Adiciona um preenchimento interno ao botão
                relief="flat" # Aparência plana
               )

# configura o estilo da animação do cursor ao passar pelo botão
style.map("TButton",
          background=[("active", "#66c9e7")], 
          foreground=[("active", "white")]
         )

# botão que chama a função que faz imprimir a senha gerada no layout
botão_gerar = ttk.Button(frame, text="Gerar senha", 
                         command=atualiza, 
                         style="TButton")
botão_gerar.pack(pady=20)

# label com a configuração do texto da senha gerada
label_resultado = tk.Label(frame, text="",
                           font=("Courier", 14, "bold"), 
                           fg="#00008B", 
                           bg="lightgreen", 
                           wraplength=280)
label_resultado.pack(pady=5, before=botão_gerar)



root.mainloop()