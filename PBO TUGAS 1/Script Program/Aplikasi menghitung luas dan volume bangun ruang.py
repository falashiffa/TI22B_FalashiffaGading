print('Aplikasi Menghitung Luas dan Volume Bangun Ruang')
print('-------------------------------------------------')
print('[1] Luas dan Keliling Persegi panjang')
print('[2] Luas dan Volume Kubus')
print('[3] Luas dan Volume Balok')
print('[4] Luas dan Volume Limas Segiempat')
print('[5] Luas dan Volume Prisma Segitiga')
print('[6] Luas dan Volume Limas Segitiga')
print('[7] Luas dan Volume Kerucut')
print('[8] Luas dan Volume Tabung')
print('[9] Luas dan Volume Bola')
print('-------------------------------------------------')
pilihan = int(input('Pilih yang mana yang akan dihitung luas dan volumenya (1-8) : '))

if pilihan == 1:
    print('Aplikasi menghitung luas dan keliling Persegi Panjang')
    print('-------------------------------------------------')

    panjang = int(input('Masukan panjang : '))
    lebar = int(input('Masukan lebar : '))

    luas = panjang*lebar
    keliling = 2*panjang*lebar

    print('\nLuasnya = ',str(luas))
    print('Kelilingnya = ',str(keliling))

elif pilihan == 2:
    print('Aplikasi menghitung luas dan volume Kubus')
    print('-------------------------------------------------')

    rusuk = int(input('Masukan rusuk : '))


    luas = 6*rusuk*rusuk
    volume = rusuk*rusuk*rusuk

    print('\nLuasnya = ',str(luas))
    print('Volumenya = ',str(volume))

elif pilihan == 3:
    print('Aplikasi menghitung luas dan volume Balok')
    print('-------------------------------------------------')

    panjang = int(input('Masukan panjang : '))
    lebar = int(input('Masukan lebar : '))
    tinggi = int(input('Masukan tinggi : '))

    luas =(2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi)
    volume =  panjang*lebar*tinggi

    print('\nLuasnya = ',str(luas))
    print('volumenya= ',str(volume))

elif pilihan == 4:
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

elif pilihan == 5:
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

elif pilihan == 6:
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

elif pilihan == 7:
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

elif pilihan == 8:
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

elif pilihan == 9:
    print('Aplikasi menghitung luas dan volume Bola')
    print('-------------------------------------------------')


    jari_jari = float(input('Masukan jari jari : '))

    phi = 22/7

    #rumus
    luas = 4*phi*jari_jari*jari_jari
    volume = 4/3*phi*jari_jari*jari_jari*jari_jari

    print('\nLuasnya = ',str("%.2f" % luas))
    print('Volumenya = ',str("%.2f" % volume))
