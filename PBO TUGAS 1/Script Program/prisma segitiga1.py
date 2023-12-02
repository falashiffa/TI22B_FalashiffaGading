print('Aplikasi menghitung luas dan volume Prisma segitiga')
print('-------------------------------------------------')

sisi = int(input('Masukan sisi : '))
alas= int(input('Masukan alas : '))
tinggi = int(input('Masukan tinggi : '))
Tinggi_prisma = int(input('Masukan Tinggi Prisma : '))

Keliling_segitiga = (sisi+sisi+sisi)
Luas_segitiga = alas*tinggi/2
Luas_sisi1 = Keliling_segitiga*Tinggi_prisma
Luas_sisi2 = 2*Luas_segitiga
luas =  Luas_sisi1 + Luas_sisi2
volume = alas*tinggi*Tinggi_prisma/2

print('\nLuasnya = ',str(luas))
print('Volumenya = ',str(volume))