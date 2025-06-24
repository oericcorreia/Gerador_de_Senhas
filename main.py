import tkinter as tk
from tkinter import ttk
import random
import string


root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("300x400")

style = ttk.Style()
style.theme_use('clam')

titulo = tk.Label(root, text="Gerador de Senhas", 
                  fg="red", 
                  font=("Georgia", 18, "bold"), 
                  bg="lightgreen")
titulo.pack(pady=45)

def senha_gerada():
    tamanho = 8
    aleatorio = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choices(aleatorio, k=tamanho))
    return senha
    
    
def atualiza():
    nova_senha = senha_gerada()
    label_resultado.config(text=f"{nova_senha}")
    

style.configure("TButton", font=("Arial", 13, "bold"),
                foreground="white", # Cor do texto
                background="#0BCA6B", # Cor de fundo
                padding=10, # Adiciona um preenchimento interno ao botão
                relief="flat" # Aparência plana
               )


style.map("TButton",
          background=[("active", "#66c9e7")], 
          foreground=[("active", "white")]
         )


botão_gerar = ttk.Button(root, text="Gerar senha", 
                         command=atualiza, 
                         style="TButton")
botão_gerar.pack(pady=20)


label_resultado = tk.Label(root, text="",
                           font=("Courier", 14, "bold"), 
                           fg="#00008B", 
                           bg="lightgreen", 
                           wraplength=280)
label_resultado.pack(pady=5, before=botão_gerar)



root.mainloop()