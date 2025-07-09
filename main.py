import tkinter as tk
from tela import TelaCPF

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCPF(root)
    root.mainloop()

def verifie(cpf):
    # Primeiro dígito verificador
    cont = 10
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * cont
        cont -= 1

    dig1 = (soma * 10) % 11
    if dig1 == 10:
        dig1 = 0

    # Segundo dígito verificador
    cont = 11
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * cont
        cont -= 1

    dig2 = (soma * 10) % 11
    if dig2 == 10:
        dig2 = 0

    if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
        return True
    else:
        return False
