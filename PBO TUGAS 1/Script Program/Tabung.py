print('Aplikasi menghitung luas dan volume Tabung')
print('-------------------------------------------------')


tinggi = float(input('Masukan tinggi : '))
jari_jari = float(input('Masukan jari jari : '))

phi = 3.14

#rumus
luas = (2*phi*jari_jari*jari_jari)+(2*phi*jari_jari*tinggi)
volume = phi*jari_jari*jari_jari*tinggi

print('\nLuasnya = ',str("%.2f" % luas))
print('Volumenya = ',str("%.2f" % volume))
