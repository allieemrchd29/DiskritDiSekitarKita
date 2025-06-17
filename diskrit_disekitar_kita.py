# Nama: Aliya Marcelia Dewi
# NIM: 2404082
# Kelas: 2B PSTI

import tkinter as tk
from tkinter import messagebox
import random

def bagi_kelompok():
    input_nama = entry_nama.get("1.0", tk.END).strip().split("\n")
    try:
        jumlah_kel = int(entry_jumlah.get())
    except ValueError:
        messagebox.showerror("Error, Jumlah kelompok harus berupa angka!")
        return

    if jumlah_kel <= 0:
        messagebox.showerror("Error, Jumlah kelompok harus lebih dari 0!")
        return

    if len(input_nama) < jumlah_kel:
        messagebox.showerror("Error, Jumlah nama harus lebih banyak dari jumlah kelompok!")
        return

    random.shuffle(input_nama)
    hasil_kelompok = [[] for _ in range(jumlah_kel)]

    for i, nama in enumerate(input_nama):
        hasil_kelompok[i % jumlah_kel].append(nama)

    hasil_box.config(state="normal")
    hasil_box.delete("1.0", tk.END)
    for i, kelompok in enumerate(hasil_kelompok):
        hasil_box.insert(tk.END, f"Kelompok {i+1}:\n")
        for nama in kelompok:
            hasil_box.insert(tk.END, f"  - {nama}\n")
        hasil_box.insert(tk.END, "\n")
    hasil_box.config(state="disabled")

root = tk.Tk()
root.title("Pembagian Kelompok Otomatis")
root.geometry("550x600")

tk.Label(root, text="Masukkan Daftar Nama (satu per baris):").pack(pady=5)
entry_nama = tk.Text(root, height=10, width=60)
entry_nama.pack()

tk.Label(root, text="Jumlah Kelompok:").pack(pady=5)
entry_jumlah = tk.Entry(root, width=10)
entry_jumlah.pack()

tk.Button(root, text="Bagi Kelompok", command=bagi_kelompok).pack(pady=10)

tk.Label(root, text="Hasil Pembagian Kelompok:").pack(pady=5)
hasil_box = tk.Text(root, height=15, width=60, state="disabled", font=("Courier", 10))
hasil_box.pack(pady=10)

root.mainloop()