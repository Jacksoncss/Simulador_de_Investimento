import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from tkinter import filedialog

historico = []



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Simulador De Investimentos")
janela.geometry("800x600")

# ENTRADAS INVESTIMENTOS A- JACKSON




# ENTRADAS iNVESTIMENTOS B- JACKSON


# Função de calculo do investimento
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

    
    montantes_a,final_a,investido_a = calcular_investimento(valor_inicial,aporte,taxa,meses)
    montantes_b,final_b,investido_b = calcular_investimento(valor_inicial_b,aporte_b,taxa_b,meses_b)
    valor_corrigido_a = final_a / ((1 + inflacao)** meses)   
    valor_corrigido_b = final_b / ((1 + inflacao)** meses)

    
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
    
    resultado.configure(  # type: ignore
        text= f"[A] Final: R$ {final_a:.2f}| Corrigido: R$ {valor_corrigido_a:.2f}\n"
              f"[B] Final: R$ {final_b:.2f}| Corrigido: R$ {valor_corrigido_b:.2f}\n"
    )
    
    for widget in frame_grafico.winfo_children():  # type: ignore
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(range(1, meses + 1), montantes_a, label="Investimento A", color="green")
    ax.plot(range(1, meses_b + 1), montantes_b, label="Investimento B", color="blue")
    ax.set_title("Evolução do Investimento")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Valor (R$)")
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico) # type: ignore
    canvas.draw()
    canvas.get_tk_widget().pack()

except Exception as e:
    resultado.configure(text=f"Erro: {str(e)}") # type: ignore

def mostrar_historico(historico):
    texto = "\n".join([
        f"{i+1}) [A] Final: R${h['valor_final_a']:.2f} | Corrigido: R${h['valor_corrigido_a']:.2f} | Meses: {h['meses_a']}\n"
        f"    [B] Final: R${h['valor_final_b']:.2f} | Corrigido: R${h['valor_corrigido_b']:.2f} | Meses: {h['meses_b']}"
        for i, h in enumerate(historico[-5:])
    ])

    popup = ctk.CTkToplevel(janela)
    popup.geometry("400x300")
    popup.title("Histórico de Simulações")
    label = ctk.CTkLabel(popup, text=texto, justify="left")
    label.pack(padx=10, pady=10)

def exportar_csv():
    if not historico:
        return
    caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if caminho:
        with open(caminho, mode='w' , newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f,fieldnames=historico[0].keys())
            writer.writeheader()
            writer.writerows(historico)
# Botoes - Jackson




# GRAFICO - Jackson 



# iniciar gui - Jackson