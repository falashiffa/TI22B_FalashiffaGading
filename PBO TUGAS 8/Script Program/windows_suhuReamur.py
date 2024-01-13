from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent
        #self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.Keluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text="Reamur:").grid(row=0, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Farenheit:").grid(row=3, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=0, column=1,padx=5, pady=5)
        self.txtCelcius = Entry(mainFrame)
        self.txtCelcius.grid(row=2, column=1,padx=5, pady=5)
        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=3, column=1,padx=5, pady=5)
        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=4, column=1,padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.Hitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang

    def Hitung(self):
        R = int(self.txtReamur.get())
        keCelcius = 5/4 * R
        keFahrenheit = (9/4 * R)+32
        keKelvin = 5/4 * R + 273
        self.txtCelcius.delete(0, END)
        self.txtCelcius.insert(END, str(keCelcius))
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(keFahrenheit))
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(keKelvin))
       

    def Keluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop() 