import tkinter as tk
from tkinter import font, messagebox

class TelaCPF:
    def __init__(self, root):
        self.root = root
        root.title("Validador de CPF")
        root.geometry("400x200")
        root.resizable(False, False)

        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_entrada = font.Font(family="Arial", size=14)

        frame = tk.Frame(root)
        frame.pack(pady=18)

        tk.Label(root, text="Digite um CPF:", font=self.fonte_label).pack(pady=10)

        # Validação de entrada: máximo 11 dígitos e só números
        vcmd = root.register(self.limitar_caracteres)
        self.entry = tk.Entry(
            root,
            font=self.fonte_entrada,
            width=15,
            justify="center",
            validate="key",
            validatecommand=(vcmd, "%P")
        )
        self.entry.pack()

        self.botao = tk.Button(root, text="Validar", font=self.fonte_label, command=self.validar)
        self.botao.pack(pady=15)

    def limitar_caracteres(self, texto):
        return texto.isdigit() and len(texto) <= 11

    def validar(self):
        cpf = self.entry.get()
        from main import verifie  # importa a função do arquivo main.py
        valido = verifie(cpf)
        if valido:
            messagebox.showinfo("Resultado", "CPF válido")
        else:
            messagebox.showerror("Resultado", "CPF inválido")
