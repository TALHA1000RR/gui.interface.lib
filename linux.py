from io import StringIO
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog, messagebox
import subprocess
import shutil
import os
import struct
import datetime
import sys
import struct

SECTOR_SIZE = 2048
MAX_ENTRIES = 12

# Função para criar um setor vazio
def create_empty_sector():
    return bytearray(SECTOR_SIZE)

# Função para criar o Primary Volume Descriptor (PVD)
def create_pvd(volume_name, total_sectors):
    pvd = bytearray(SECTOR_SIZE)
    pvd[0] = 1  # Tipo de descritor (1 = PVD)
    pvd[1:6] = b'CD001'  # Identificador ISO 9660
    pvd[6] = 1  # Versão do descritor
    pvd[40:72] = volume_name.ljust(32).encode('ascii')  # Nome do volume
    pvd[80:84] = struct.pack('<I', total_sectors)  # Número total de setores (little-endian)
    pvd[120] = 17  # Setor do diretório raiz
    return pvd

# Função para criar um registro de diretório
def create_directory_record(name, start_sector, size, is_file=True):
    record_length = 34 + len(name)
    record = bytearray(record_length)
    record[0] = record_length  # Tamanho do registro
    record[2:6] = struct.pack('<I', start_sector)  # Setor inicial
    record[10:14] = struct.pack('<I', size)  # Tamanho do arquivo
    record[25] = 1 if is_file else 2  # Flags (1 = arquivo, 2 = diretório)
    record[32] = len(name)  # Comprimento do nome
    record[33:33 + len(name)] = name.encode('ascii')  # Nome
    return record

# Função para criar o diretório raiz
def create_root_directory(file_records):
    root_dir = bytearray(SECTOR_SIZE)
    index = 0

    # Adiciona os registros . e ..
    entries = create_directory_record(".", 17, SECTOR_SIZE, is_file=False) + \
              create_directory_record("..", 17, SECTOR_SIZE, is_file=False)
    index += len(entries)
    root_dir[0:len(entries)] = entries

    # Adiciona os registros dos arquivos
    for record in file_records:
        if index + len(record) > SECTOR_SIZE:
            print("Erro: Limite de entradas no diretório excedido.")
            break
        root_dir[index:index + len(record)] = record
        index += len(record)

    return root_dir

# Função para alinhar o conteúdo em setores
def create_data_area(content):
    data = bytearray(SECTOR_SIZE)
    data[0:len(content)] = content.encode('ascii')
    return data

# Função principal para criar a ISO
def create_iso_from_files(file_list, iso_output="output.iso"):
    total_sectors = 16 + 1  # Reservados + PVD
    current_sector = 18  # Setor após diretório raiz
    file_records = []
    file_data_sectors = []

    # Lê os arquivos e cria registros
    for file_path in file_list:
        try:
            with open(file_path, "r") as f:
                content = f.read()
        except Exception as e:
            print(f"Erro ao ler {file_path}: {e}")
            continue

        file_size = len(content)
        needed_sectors = (file_size + SECTOR_SIZE - 1) // SECTOR_SIZE
        file_records.append(create_directory_record(os.path.basename(file_path), current_sector, file_size))

        # Prepara os dados dos arquivos alinhados por setor
        for i in range(needed_sectors):
            start = i * SECTOR_SIZE
            chunk = content[start:start + SECTOR_SIZE]
            file_data_sectors.append(create_data_area(chunk))

        current_sector += needed_sectors
        total_sectors += needed_sectors

    # Cria o arquivo ISO
    with open(iso_output, "wb") as iso_file:
        # 16 setores reservados
        for _ in range(16):
            iso_file.write(create_empty_sector())

        # Setor 16: PVD
        iso_file.write(create_pvd("MYISO", total_sectors))

        # Setor 17: Diretório raiz
        iso_file.write(create_root_directory(file_records))

        # Setores de dados dos arquivos
        for sector_data in file_data_sectors:
            iso_file.write(sector_data)

    print(f"ISO '{iso_output}' criado com sucesso!")

# Função de entrada do usuário

class FSProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("work station python")
        self.root.geometry("400x200")
        self.root.configure(bg="yellow")
        
        # Dados carregados do arquivo .fs
        self.system_config=""
        self.system_name=""
        self.files_to_exe=b''
        self.files_to_process = None        
                
        # Botão para criar arquivo .iso
        self.save_button = tk.Button(
            root, text="open as .iso", command=self.load_fs_file, bg="black", fg="yellow"
        )
        self.save_button.pack(pady=10)
        
        # Rótulo de status
        self.status_label = tk.Label(
            root, text="", bg="yellow", fg="black", wraplength=350
        )
        self.status_label.pack(pady=10)
    def load_fs_file(self):
        file_list_path = filedialog.askopenfilename(
            filetypes=[("c Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_list_path:
            return None

        temp_directory = "./tmp"
        file_list_paths=file_list_path.replace(".txt",".iso")
         
        
        with open(file_list_path, "r") as f:
            file_list = [line.strip() for line in f if line.strip()]
    
        print("Arquivos encontrados:")
        for idx, file in enumerate(file_list, 1):
            print(f"{idx}: {file}")

        create_iso_from_files(file_list,file_list_paths)

    
if __name__ == "__main__":
    root = tk.Tk()
    app = FSProcessorApp(root)
    root.mainloop()

