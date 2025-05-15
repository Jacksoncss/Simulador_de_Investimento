import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Janela principal

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Simulador De Investimentos")
janela.geometry("1280x720")