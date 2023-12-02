print('Aplikasi menghitung luas dan volume Limas Segiempat')
print('-------------------------------------------------')

sisi = int(input('Masukan sisi : '))
alas= int(input('Masukan alas : '))
tinggi = int(input('Masukan tinggi : '))

luas_sisi = 4*alas*tinggi
luas_alas = sisi*sisi
luas =  luas_sisi + luas_sisi + luas_sisi + luas_sisi + luas_sisi
volume = luas_alas*tinggi/3

print('\nLuasnya = ',str(luas))
print('Volumenya = ',str(volume))