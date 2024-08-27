import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import zipfile
import os
import customtkinter as ctk
from datetime import datetime

# Cria a janela principal
root = ctk.CTk()
root.title("Gerador de Arquivos Retroativos EFD")

# Variáveis globais
df = None
use_year_option = tk.BooleanVar(value=False)  # Variável para controlar o uso do ano
year_option = tk.StringVar()  # Variável para armazenar o ano selecionado

# Estilo da barra de rolagem
style = ttk.Style()
style.theme_use('clam')  # Usamos 'clam' como tema base para que as modificações de cor sejam aplicadas corretamente
style.configure("Vertical.TScrollbar", background="#1f538d", troughcolor="#3a3a3a", arrowcolor="#1f538d")

# Função para carregar o CSV
def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, df.to_string(index=False))

# Função para gerar os arquivos
def generate_files():
    global df
    if df is None:
        messagebox.showerror("Erro", "Nenhum arquivo CSV foi carregado.")
        return
    
    output_dir = filedialog.askdirectory()
    if not output_dir:
        return

    # Exibe a barra de progresso
    progress_bar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    progress_bar.start(10)  # Inicia a animação da barra de progresso
    root.update_idletasks()  # Atualiza a interface para mostrar a barra de progresso

    try:
        if use_year_option.get():
            # Se a opção de ano estiver habilitada
            selected_year = int(year_option.get())
            with open(r'C:\Users\PC\Desktop\MODELO.txt', 'r') as model_file:
                model_content = model_file.read()
            
            with zipfile.ZipFile(os.path.join(output_dir, f'EFD_Arquivos_{selected_year}.zip'), 'w') as zipf:
                for month in range(1, 13):
                    # Define o primeiro e último dia do mês
                    start_date = datetime(selected_year, month, 1).strftime('%d/%m/%Y')
                    end_date = datetime(selected_year, month, 1).replace(day=28) + pd.DateOffset(days=4)
                    end_date = (end_date - pd.DateOffset(days=end_date.day)).strftime('%d/%m/%Y')

                    # Cria subpasta para o mês
                    month_folder = os.path.join(output_dir, f"{selected_year}_{month:02d}")
                    os.makedirs(month_folder, exist_ok=True)

                    for index, row in df.iterrows():
                        filename = f"{row['cnpj']}_EFD.txt"
                        filepath = os.path.join(month_folder, filename)
                        
                        # Substitui as variáveis no conteúdo do modelo
                        content = model_content.replace('VARIAVEL_01', str(row['cnpj']))
                        content = content.replace('VARIAVEL_02', str(row['nome']))
                        content = content.replace('VARIAVEL_03', str(start_date))
                        content = content.replace('VARIAVEL_04', str(end_date))

                        # Cria um novo arquivo TXT e grava o conteúdo nele
                        with open(filepath, 'w') as txt_file:
                            txt_file.write(content)
                        
                        # Adiciona o arquivo TXT ao arquivo ZIP
                        zipf.write(filepath, os.path.join(f"{selected_year}_{month:02d}", filename))
                        
                        # Remove o arquivo TXT após adicionar ao ZIP para limpar o diretório
                        os.remove(filepath)
        else:
            # Lógica original para data de início e fim manuais
            start_date = start_date_entry.get()
            end_date = end_date_entry.get()
            
            if not start_date or not end_date:
                messagebox.showerror("Erro", "As datas de início e fim devem ser preenchidas.")
                return
            
            with open('/mnt/data/MODELO.txt', 'r') as model_file:
                model_content = model_file.read()

            with zipfile.ZipFile(os.path.join(output_dir, 'EFD_Arquivos.zip'), 'w') as zipf:
                for index, row in df.iterrows():
                    filename = f"{row['cnpj']}_EFD.txt"
                    filepath = os.path.join(output_dir, filename)
                    
                    # Substitui as variáveis no conteúdo do modelo
                    content = model_content.replace('VARIAVEL_01', str(row['cnpj']))
                    content = content.replace('VARIAVEL_02', str(row['nome']))
                    content = content.replace('VARIAVEL_03', str(start_date))
                    content = content.replace('VARIAVEL_04', str(end_date))

                    # Cria um novo arquivo TXT e grava o conteúdo nele
                    with open(filepath, 'w') as txt_file:
                        txt_file.write(content)
                    
                    # Adiciona o arquivo TXT ao arquivo ZIP
                    zipf.write(filepath, filename)
                    
                    # Remove o arquivo TXT após adicionar ao ZIP para limpar o diretório
                    os.remove(filepath)

        messagebox.showinfo("Sucesso", "Arquivos TXT gerados e compactados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar os arquivos: {str(e)}")
    finally:
        # Para a barra de progresso e esconde após o término
        progress_bar.stop()
        progress_bar.grid_remove()
        root.update_idletasks()  # Atualiza a interface para esconder a barra de progresso

# Checkbox para habilitar a opção de ano
use_year_checkbox = ctk.CTkCheckBox(root, text="Gerar para cada mês do ano", variable=use_year_option)
use_year_checkbox.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada para selecionar o ano
year_entry = ctk.CTkEntry(root, textvariable=year_option, placeholder_text="Ano (ex: 2023)")
year_entry.grid(row=0, column=1, padx=10, pady=10)

# Botão para carregar o CSV
load_button = ctk.CTkButton(root, text="Carregar CSV", command=load_csv)
load_button.grid(row=1, column=0, padx=10, pady=10)

# Frame para a área de texto e barra de rolagem
text_frame = tk.Frame(root)
text_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Área de texto com fundo preto e texto branco
text_widget = tk.Text(text_frame, height=15, width=60, bg='black', fg='white')
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de rolagem para a área de texto com estilo personalizado
scrollbar = ttk.Scrollbar(text_frame, orient="vertical", style="Vertical.TScrollbar", command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Campo de entrada para a data de início
start_date_label = ctk.CTkLabel(root, text="Data de Início (dd/mm/yyyy):")
start_date_label.grid(row=3, column=0, padx=10, pady=5)
start_date_entry = ctk.CTkEntry(root)
start_date_entry.grid(row=3, column=1, padx=10, pady=5)

# Campo de entrada para a data de fim
end_date_label = ctk.CTkLabel(root, text="Data de Fim (dd/mm/yyyy):")
end_date_label.grid(row=4, column=0, padx=10, pady=5)
end_date_entry = ctk.CTkEntry(root)
end_date_entry.grid(row=4, column=1, padx=10, pady=5)

# Botão para gerar arquivos
generate_button = ctk.CTkButton(root, text="Gerar Arquivos", command=generate_files)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Barra de progresso
progress_bar = ttk.Progressbar(root, mode='indeterminate')

root.mainloop()
