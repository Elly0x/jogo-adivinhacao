import tkinter as tk
from tkinter import messagebox
import random

# Lista de filmes e dicas
filmes = [
    {"titulo": "Interestelar", "dicas": ["Viagem no tempo", "Buraco negro", "Christopher Nolan"]},
    {"titulo": "Clube da Luta", "dicas": ["Sociedade secreta", "Regra número 1", "Brad Pitt"]},
    {"titulo": "Matrix", "dicas": ["Realidade simulada", "Pílula vermelha", "Keanu Reeves"]},
]

# Escolhe um filme aleatório
filme_atual = random.choice(filmes)
dicas_exibidas = 0
historico = []

# Função para verificar a resposta
def verificar_resposta():
    resposta = entrada.get().strip()
    if resposta.lower() == filme_atual["titulo"].lower():
        messagebox.showinfo("Parabéns!", "Você acertou!")
        janela.quit()
    else:
        historico.append(resposta)
        atualizar_historico()
        entrada.delete(0, tk.END)

# Função para exibir a próxima dica
def mostrar_dica():
    global dicas_exibidas
    if dicas_exibidas < len(filme_atual["dicas"]):
        dicas_lista.insert(tk.END, f"Dica {dicas_exibidas + 1}: {filme_atual['dicas'][dicas_exibidas]}")
        dicas_exibidas += 1
    else:
        messagebox.showinfo("Dicas", "Você já viu todas as dicas!")

# Função para atualizar o histórico
def atualizar_historico():
    historico_lista.delete(0, tk.END)
    for tentativa in historico:
        historico_lista.insert(tk.END, tentativa)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Adivinhe o Filme")
janela.geometry("400x500")
janela.configure(bg="#121212")  # Fundo escuro

# Estilização
cor_texto = "#00A2FF"
fonte_padrao = ("Arial", 12)

# Título
titulo = tk.Label(janela, text="🎬 Adivinhe o Filme!", font=("Arial", 16, "bold"), fg=cor_texto, bg="#121212")
titulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela, font=fonte_padrao, bg="#1E1E1E", fg="white", insertbackground="white")
entrada.pack(pady=5, padx=20, fill=tk.X)

# Botões
btn_verificar = tk.Button(janela, text="Verificar", font=fonte_padrao, command=verificar_resposta, bg="#007BFF", fg="white")
btn_verificar.pack(pady=5)

btn_dica = tk.Button(janela, text="Mostrar Dica", font=fonte_padrao, command=mostrar_dica, bg="#FFC107", fg="black")
btn_dica.pack(pady=5)

# Lista de dicas
dicas_lista = tk.Listbox(janela, font=fonte_padrao, bg="#1E1E1E", fg="white", height=3)
dicas_lista.pack(pady=5, padx=20, fill=tk.X)

# Histórico de tentativas
tk.Label(janela, text="📜 Histórico de Tentativas:", font=fonte_padrao, fg=cor_texto, bg="#121212").pack()
historico_lista = tk.Listbox(janela, font=fonte_padrao, bg="#1E1E1E", fg="white", height=5)
historico_lista.pack(pady=5, padx=20, fill=tk.X)

# Rodando a aplicação
janela.mainloop()