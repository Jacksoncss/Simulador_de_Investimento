import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from tkinter import filedialog

historico = []

# Janela principal

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Simulador De Investimentos")
janela.geometry("900x700")

def calcular_investimento(inicial, aporte, taxa, meses):
    montantes = []
    saldo = inicial
    total = inicial
    for _ in range(meses):
        saldo = saldo * (1 + taxa) + aporte
        total += aporte
        montantes.append(saldo)
    return montantes, saldo, total
def simular():
    valor_inicial = float(entry_inicial.get())  # type: ignore
    aporte = float(entry_aporte.get()) # type: ignore
    taxa = float(entry_taxa.get()) / 100 # type: ignore
    meses = int(entry_meses.get()) # type: ignore
    inflacao = float(entry_inflacao.get() or 0) / 100 # type: ignore

    valor_inicial_b = float(entry_inicial_b.get()) # type: ignore
    aporte_b = float(entry_aporte_b.get()) # type: ignore
    taxa_b = float(entry_taxa_b.get()) / 100 # type: ignore
    meses_b = int(entry_meses_b.get()) # type: ignore
    inflacao_b = float(entry_inflacao_b.get() or 0) / 100 # type: ignore

    # Cauculo Do Investimento
    montantes_a,final_a,investido_a = calcular_investimento(valor_inicial,aporte,taxa,meses)
    montantes_b,final_b,investido_b = calcular_investimento(valor_inicial_b,aporte_b,taxa_b,meses_b)
    valor_corrigido_a = final_a / ((1 + inflacao)** meses)   
    valor_corrigido_b = final_b / ((1 + inflacao)** meses)

    # Criando Historico pra o Usuario ver seus ultimos investimentos
    historico.append({
            "valor_final_a": final_a,
            "valor_corrigido_a": valor_corrigido_a,
            "total_investido_a": investido_a,
            "meses_a": meses,
            "taxa_a": taxa,
            "valor_final_b": final_b,
            "valor_corrigido_b": valor_corrigido_b,
            "total_investido_b": investido_b,
            "meses_b": meses_b,
            "taxa_b": taxa_b
        })