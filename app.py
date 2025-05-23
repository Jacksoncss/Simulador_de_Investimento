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


entry_inicial = ctk.CTkEntry (janela, placeholder_text="Valor Inicial A (R$)") 
entry_aporte = ctk.CTkEntry(janela, placeholder_text="Aporte Mensal A (R$)") 
entry_taxa = ctk.CTkEntry(janela, placeholder_text="Taxa de Juros A (% ao mês)") 
entry_inflacao = ctk.CTkEntry (janela, placeholder_text="Inflação A (% ao mês)") 
entry_meses = ctk.CTkEntry (janela, placeholder_text="Duração A (meses)") 
entry_inicial.pack(pady=2) 
entry_aporte.pack(pady=2) 
entry_taxa.pack(pady=2) 
entry_inflacao.pack(pady=2) 
entry_meses.pack(pady=2) 

entry_inicial_b = ctk.CTkEntry (janela, placeholder_text="Valor Inicial B (R$)") 
entry_aporte_b = ctk.CTkEntry (janela, placeholder_text="Aporte Mensal B (R$)") 
entry_taxa_b = ctk.CTkEntry(janela, placeholder_text="Taxa de Juros B (% ao mês)") 
entry_inflacao_b = ctk.CTkEntry (janela, placeholder_text="Inflação B (% ao mês)") 
entry_meses_b = ctk.CTkEntry (janela, placeholder_text="Duração B (meses)") 
entry_inicial_b.pack(pady=2) 
entry_aporte_b.pack(pady=2) 
entry_taxa_b.pack(pady=2) 
entry_inflacao_b.pack(pady=2) 
entry_meses_b.pack(pady=2) 

resultado = ctk.CTkLabel(janela, text="", font=("Arial", 16)) 
resultado.pack(pady=10)


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
    try:
        valor_inicial = float(entry_inicial.get())  
        aporte = float(entry_aporte.get()) 
        taxa = float(entry_taxa.get()) / 100 
        meses = int(entry_meses.get()) 
        inflacao = float(entry_inflacao.get() or 0) / 100 

        valor_inicial_b = float(entry_inicial_b.get()) 
        aporte_b = float(entry_aporte_b.get()) 
        taxa_b = float(entry_taxa_b.get()) / 100 
        meses_b = int(entry_meses_b.get()) 
        inflacao_b = float(entry_inflacao_b.get() or 0) / 100 

        
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
        
        resultado.configure(  
            text= f"[A] Final: R$ {final_a:.2f}| Corrigido: R$ {valor_corrigido_a:.2f}\n"
                f"[B] Final: R$ {final_b:.2f}| Corrigido: R$ {valor_corrigido_b:.2f}\n"
        )
        
        for widget in frame_grafico.winfo_children():  
            widget.destroy()
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(range(1, meses + 1), montantes_a, label="Investimento A", color="green")
        ax.plot(range(1, meses_b + 1), montantes_b, label="Investimento B", color="blue")
        ax.set_title("Evolução do Investimento")
        ax.set_xlabel("Meses")
        ax.set_ylabel("Valor (R$)")
        ax.legend()
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico) 
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
            resultado.configure(text=f"Erro: {str(e)}") 

def mostrar_historico():
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

botao_simular = ctk.CTkButton(janela, text="Simular", command=simular) 
botao_simular.pack(pady=10) 
btn_historico = ctk.CTkButton(janela, text="Ver Histórico", command=mostrar_historico) 
btn_historico.pack(pady=5) 
btn_exportar = ctk.CTkButton(janela, text="Exportar CSV", command=exportar_csv) 
btn_exportar.pack(pady=5)

frame_grafico = ctk.CTkFrame (janela) 
frame_grafico.pack(pady=10, fill="both", expand=True) 

janela.mainloop()