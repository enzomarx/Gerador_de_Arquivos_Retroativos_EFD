import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import pandas as pd
import zipfile
import os

def load_csv():
    global df
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        try:
            df = pd.read_csv(csv_file_path)
            if 'cnpj' in df.columns and 'nome' in df.columns:
                # Exibir o conteúdo do csv diretamente na interface
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, df.to_string(index=False))
                messagebox.showinfo("CSV Carregado", "Arquivo CSV carregado com sucesso.")
                return df
            else:
                messagebox.showerror("Erro", "O CSV deve conter as colunas 'cnpj' e 'nome'.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo CSV: {str(e)}")
    return None
    
def generate_files():
    if df is None:
        messagebox.showerror("Erro", "Nenhum arquivo CSV foi carregado.")
        return
    
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    if not start_date or not end_date:
        messagebox.showerror("Erro", "As Datas de inicio e fim devem ser preenchidas.")
        return
        
    output_dir = filedialog.askdirectory()
    if not output_dir:
        return
    
    try:
        # Abrir o arquivo modelo e ler o conteúdo apenas uma vez
        with open(r'C:\Users\PC\Desktop\MODELO.txt', 'r') as model_file:
            model_content = model_file.read()
            
        with zipfile.ZipFile(os.path.join(output_dir, 'EFD_Arquivos.zip'), 'w') as zipf:
            for index, row in df.iterrows():
                filename = f"{row['cnpj']}_EFD.txt"
                filepath = os.path.join(output_dir, filename)
                
                # Substituir as variáveis no conteúdo do modelo
                content = model_content.replace('VARIAVEL_01', str(row['cnpj']))
                content = content.replace('VARIAVEL_02', str(row['nome']))
                content = content.replace('VARIAVEL_03', str(start_date))
                content = content.replace('VARIAVEL_04', str(end_date))
                
                # Criar e escrever no novo arquivo TXT        
                with open(filepath, 'w') as txt_file:
                    txt_file.write(content)
                
                # Adicionar o arquivo ao zip e depois removê-lo    
                zipf.write(filepath, filename)
                os.remove(filepath)
                
        messagebox.showinfo("Sucesso", "Arquivos TXT gerados e compactados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar os arquivos: {str(e)}")

# Configurando a janela principal
app = ctk.CTk()
app.title("Gerador de Arquivos Retroativos EFD")
app.geometry("700x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

df = None # variavel global para armazenar o dataframe

# Elementos da interface
title_label = ctk.CTkLabel(app, text="Gerador de Arquivos Retroativos EFD", font=("Arial", 20))
title_label.pack(pady=20)

upload_button = ctk.CTkButton(app, text="Carregar CSV", command=load_csv)
upload_button.pack(pady=10)

text_box = ctk.CTkTextbox(app, height=150)
text_box.pack(pady=10)

data_frame = ctk.CTkFrame(app)
data_frame.pack(pady=20)

start_date_label = ctk.CTkLabel(data_frame, text="Data de Início:")
start_date_label.grid(row=0, column=1, padx=10)

start_date_entry = ctk.CTkEntry(data_frame)
start_date_entry.grid(row=0, column=1, padx=10)

end_date_entry = ctk.CTkLabel(data_frame, text="Data de Fim:")
end_date_entry.grid(row=0, column=2, padx=10) 

end_date_entry = ctk.CTkEntry(data_frame)
end_date_entry.grid(row=0, column=3, padx=10)            

genrate_button = ctk.CTkButton(app, text="Gerar Arquivos", command=generate_files)
genrate_button.pack(pady=20)

app.mainloop()