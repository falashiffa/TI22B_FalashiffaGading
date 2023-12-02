# file_utama.py
import tkinter as tk
from Kalkulator_Bangun_Ruang import CalculatorApp,calculate

# Menggunakan fungsi dari modul_tambahan
calculate()

# Membuat instance dari kelas modul
objek_modul = CalculatorApp()

# Menggunakan tkinter
root = tk.Tk()
label = tk.Label(root)
label.pack()
root.mainloop()
