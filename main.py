import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
import subprocess

root = ctk.CTk()
root.geometry("450x500")
root.title("cURL GUI")
root.config(bg="black")
root.resizable(False, False)

# Variaveis
url = ""

def aboutFunc():
    messagebox.showinfo("Sobre", "cURL GUI 0.1 - Uma ferramenta simples de código aberto")

def baixar():
    url = entryURL.get()
    try:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")  # eu nem sabia disso, mas vou usar kekekekeke
        os.chdir(download_path)
        print("Pasta de Downloads Acessada")
        messagebox.showinfo("Quer baixar?", "Clique em OK para iniciar")
        subprocess.run(["curl", "-O", url], check=True)
        messagebox.showinfo("Baixado", "Salvo na pasta Downloads!")
    except subprocess.CalledProcessError:
        messagebox.showinfo("Erro", "Ocorreu um erro!")

initFrame = ctk.CTkFrame(root, bg_color="black", fg_color="gray10", corner_radius=15, width=440, height=490)
initFrame.place(x=5, y=5)

title = ctk.CTkLabel(initFrame, bg_color="gray10", text="cURL GUI", font=("default", 50))
title.place(x=110, y=9)

digiteLabel = ctk.CTkLabel(initFrame, bg_color="gray10", text="Digite a url:", font=("default", 20))
digiteLabel.place(x=10, y=100)

entryURL = ctk.CTkEntry(initFrame, width=350, height=30, font=("default", 30))
entryURL.place(x=10, y=130)

submitBtn = ctk.CTkButton(initFrame, width=150, height=50, fg_color="purple", text="Baixar", font=("default", 25), command=baixar)
submitBtn.place(x=10, y=185)

aboutBtn = ctk.CTkButton(initFrame, width=150, height=50, fg_color="purple", text="Sobre...", font=("default", 25), command=aboutFunc)
aboutBtn.place(x=10, y=425)

root.mainloop()