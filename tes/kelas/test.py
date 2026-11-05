angka = int (input ("masukan angka: "))

if angka > 0:
    print ("angka positif")
elif angka == 0:
    print ("angka nol")
else:
    print ('angka negatif')

umur = 18 
status = "dewasa" if umur >= 18 else "belum dewasa"
print (status)
