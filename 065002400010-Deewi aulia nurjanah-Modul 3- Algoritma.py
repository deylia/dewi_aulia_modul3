def cek_segitiga(a, b, c):
    # Mengecek apakah ketiga sisi membentuk segitiga
    if a + b > c and b + c > a and c + a > b:
        # Cek jenis segitiga berdasarkan panjang sisi
        if a == b == c:
            return "Segitiga Sama Sisi"
        elif a == b or b == c or a == c:
            return "Segitiga Sama Kaki"
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):    
            return "Segitiga Siku-Siku"
        else:
            return "Segitiga Sembarang"
        
    else:
        return "Tidak dapat membentuk segitiga"
    
try:
    # Input sisi-sisi segitiga
    sisi1 = float(input("Masukkan panjang sisi pertama: "))
    sisi2 = float(input("Masukkan panjang sisi kedua: "))
    sisi3 = float(input("Masukkan panjang sisi ketiga: "))

    #memeriksa hasil
    jenis_segitiga = cek_segitiga(sisi1, sisi2,sisi3)
    print(jenis_segitiga)  
except ValueError:
    print("input tidak valid. silahkan masukkan angka.")