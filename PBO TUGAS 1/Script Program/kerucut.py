print('Aplikasi menghitung luas dan volume Kerucut')
print('-------------------------------------------------')

s = float(input('Masukan s : '))
tinggi = float(input('Masukan tinggi : '))
jari_jari = float(input('Masukan jari jari : '))

phi = 3.14

#rumus
luas = (phi*jari_jari*jari_jari) + (phi*jari_jari*s)
volume = phi*jari_jari*jari_jari*tinggi/3

print('\nLuasnya = ',str("%.2f" % luas))
print('Volumenya = ',str("%.2f" % volume))