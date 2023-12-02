from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar
from gtts import gTTS
import os

def text_to_speech():
    selected_text = text_entry.get()
    selected_language = language_var.get()
    languages = {
        'Bahasa Inggris': 'en',
        'Bahasa Spanyol': 'es',
        'Bahasa Prancis': 'fr',
        'Bahasa Jawa'   : 'jw',

        # Tambahkan bahasa lain di sini sesuai kebutuhan
    }
    language_code = languages[selected_language]

    try:
        tts = gTTS(text=selected_text, lang=language_code, slow=False)
        tts.save("text_audio.mp3")
        os.system("start text_audio.mp3")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

root = Tk()
root.title("Konversi Teks ke Ucapan")

text_label = Label(root, text="Masukkan teks yang ingin diucapkan:")
text_label.pack()

text_entry = Entry(root, width=50)
text_entry.pack()

language_var = StringVar(root)
language_var.set('Bahasa Inggris')  # Bahasa Inggris sebagai pilihan default
language_label = Label(root, text="Pilih Bahasa:")
language_label.pack()

language_option = OptionMenu(root, language_var, 'Bahasa Inggris', 'Bahasa Spanyol', 'Bahasa Prancis', 'Bahasa Jawa'
)
language_option.pack(pady=20)

convert_button = Button(root, text="Konversi Teks ke Ucapan", command=text_to_speech)
convert_button.pack(pady=10)

root.mainloop()
