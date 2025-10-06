def topla(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    return sonuc

def cikar(sayi1, sayi2):
    sonuc = sayi1 - sayi2
    a = 1
    return sonuc

while True:
    sayi1 = int(input("Birinci sayı: "))
    sayi2 = int(input("İkinci sayı: "))

    islem = input("Toplama için 1, çıkarma için 2, çıkmak için 3'e basın")
    if islem == "1":
        print(topla(sayi1, sayi2))
    elif islem == "2":
        print(cikar(sayi1, sayi2))
    elif islem == "3":
        break
    else:
        print("Lütfen geçerli bir giriş yap")