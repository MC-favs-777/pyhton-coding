print("Basic Hesap Makinesi")

sayi1 = float(input("Birinci sayıyı girin: "))
islem = input("İşlemi seçin (+, -, *, /): ")
sayi2 = float(input ("İkinci sayıyı girin: ") )

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2 
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 == 0:
        print("Hata: Sıfıra bölme hatası!")
    else:
        sonuc = sayi1 / sayi2
else:
    print("Geçersiz işlem!")

if islem in ("+", "-", "*", "/") and not (islem == "/" and sayi2 == 0):
    print("Sonuç:", sonuc)