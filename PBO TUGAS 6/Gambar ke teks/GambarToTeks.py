import tkinter as tk
from tkinter import filedialog, image_names

def open_image():
    file_path = filedialog.askopenfilename()
    image = image_names.open(file_path)
    text = image_to_text(image)
    text_area.insert(tk.END, text)

def image_to_text(image):
    # Proses gambar menjadi teks di sini
    # Anda dapat menggunakan library seperti pytesseract untuk mengubah gambar menjadi teks

    return "Teks hasil konversi gambar"

root = tk.Tk()
root.title("Gambar ke Teks")

open_button = tk.Button(root, text="Buka Gambar", command=open_image)
open_button.pack()

text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack()

root.mainloop()
