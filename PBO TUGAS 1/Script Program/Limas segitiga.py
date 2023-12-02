print('Aplikasi menghitung luas dan volume Limas segitiga')
print('-------------------------------------------------')


alas= int(input('Masukan alas : '))
tinggi = int(input('Masukan tinggi : '))
Tinggi_prisma = int(input('Masukan Tinggi Prisma : '))

luas_alas = alas*tinggi/2
luas_sisi = alas*tinggi/2
luas = luas_sisi+luas_sisi+luas_sisi+luas_sisi
volume = luas_alas*Tinggi_prisma/3

print('\nLuasnya = ',str(luas))
print('Volumenya = ',str(volume))
