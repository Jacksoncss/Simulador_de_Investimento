import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Janela principal

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Simulador De Investimentos")
janela.geometry("1280x720")

def simular():
    valor_inicial = float(entry_inicial.get())  # type: ignore
    aporte = float(entry_aporte.get()) # type: ignore
    taxa = float(entry_taxa.get()) / 100 # type: ignore
    meses = int(entry_meses.get()) # type: ignore

    montantes = []
    total_investido = valor_inicial
    saldo = valor_inicial

    for mes in range(1,meses + 1):
        saldo = saldo * (1+ taxa + aporte)
        total_investido += aporte
        montantes.append(saldo)