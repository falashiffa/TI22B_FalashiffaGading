from tkinter import *
from tkinter import messagebox

def reset_entry():
    umur_tf.delete(0,'end')
    tinggibadan_tf.delete(0,'end')
    beratbadan_tf.delete(0,'end')

def calculate_bmi():
    kg = int(beratbadan_tf.get())
    m = int(tinggibadan_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):

    if bmi < 18.5 :
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi}  kekurangan berat badan')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi}  Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi}  kelebihan berat badan')
    elif (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi}  Obesitas')
    else:
        messagebox.showinfo('bmi-pythonguides', 'something went wrong!')

ws = Tk()
ws.title('Timbangan Berat Badan Ideal')
ws.geometry('400x300')
ws.config(bg='#D2B48C')

var = IntVar

frame = Frame(ws,padx=10,pady=10,bg='#F5DEB3')
frame.pack(expand=True)


umur_lb=Label(frame,text="Masukan Umur")
umur_lb.grid(row=1,column=1)

umur_tf=Entry(frame,)
umur_tf.grid(row=1,column=2,pady=5)

gen_lb=Label(frame,text='Pilih Jenis Kelamin')
gen_lb.grid(row=2,column=1)

frame2=Frame(frame)
frame2.grid(row=2,column=2,pady=5)

pria_rb = Radiobutton(frame2,text='Pria',variable=var,value=1)
pria_rb.pack(side=LEFT)

wanita_rb = Radiobutton(frame2,text='Wanita',variable=var,value=2)
wanita_rb.pack(side=RIGHT)

tinggibadan_lb=Label(frame,text="Masukan Tinggi Badan(cm) ")
tinggibadan_lb.grid(row=3,column=1)

beratbadan_lb=Label(frame,text="Masukan Berat Badan(kg) ")
beratbadan_lb.grid(row=4,column=1)

tinggibadan_tf= Entry(frame,)
tinggibadan_tf.grid(row=3,column=2,pady=5)

beratbadan_tf=Entry(frame,)
beratbadan_tf.grid(row=4,column=2,pady=5)

frame3=Frame(frame,)
frame3.grid(row=5,columnspan=3,pady=10)

cal_btn=Button(frame3,text='Hitung',command=calculate_bmi)
cal_btn.pack(side=LEFT)

reset_btn=Button(frame3,text='Reset',command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn=Button(frame3,text='Exit',command=lambda:ws.destroy())
exit_btn.pack(side=RIGHT)

ws.mainloop()
