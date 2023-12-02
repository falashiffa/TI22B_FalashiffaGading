print('Aplikasi menghitung luas dan volume Bola')
print('-------------------------------------------------')


jari_jari = float(input('Masukan jari jari : '))

phi = 22/7

#rumus
luas = 4*phi*jari_jari*jari_jari
volume = 4/3*phi*jari_jari*jari_jari*jari_jari

print('\nLuasnya = ',str("%.2f" % luas))
print('Volumenya = ',str("%.2f" % volume))