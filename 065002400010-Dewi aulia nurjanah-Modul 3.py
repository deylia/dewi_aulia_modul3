import math
print("=====Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan======")
# Meminta input dari user untuk nilai a, b, dan c
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

# Mengecek apakah nilai a bukan nol
if a == 0:
    print("Persamaan bukan persamaan kuadrat, karena nilai A = 0")
else:
    # Menghitung determinan (delta)
    determinan = b**2 - 4*a*c
    print(f"Persamaan kuadrat {a}x^2 + {b}x + {c}")
    print(f"Determinannya = {determinan}")

    # Mengecek jenis akar berdasarkan nilai determinan
    if determinan > 0:
        # Jika determinan positif, ada dua akar real berbeda
        akar1 = (-b + math.sqrt(determinan)) / (2*a)
        akar2 = (-b - math.sqrt(determinan)) / (2*a)
        print("Memiliki Akar Berbeda")
        print(f"Akar x1 = {akar1}")
        print(f"Akar x2 = {akar2}")
    elif determinan == 0:
        # Jika determinan nol, ada satu akar kembar
        akar = -b / (2*a)
        print("Merupakan Akar Kembar")
        print(f"Akar = {akar}")
    else:
        # Jika determinan negatif, ada dua akar imajiner
        real_part = -b / (2*a)
        imag_part = math.sqrt(-determinan) / (2*a)
        print("Merupakan Akar Imajiner")
        print(f"Akar x1 = {real_part} + {imag_part}i")
        print(f"Akar x2 = {real_part} - {imag_part}i")

print("=====Program Selesai=====")