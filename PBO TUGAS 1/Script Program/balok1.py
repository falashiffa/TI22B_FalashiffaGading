print('Aplikasi menghitung luas dan volume Balok')
print('-------------------------------------------------')

panjang = int(input('Masukan panjang : '))
lebar = int(input('Masukan lebar : '))
tinggi = int(input('Masukan tinggi : '))

luas =(2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi)
volume =  panjang*lebar*tinggi
print('\nLuasnya = ',str(luas))
print('volumenya= ',str(volume))