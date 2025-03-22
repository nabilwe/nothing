nilai = int(input("masukkan nilai:"))

if nilai >= 50:
    print("selamat anda lulus")
    if nilai == 100:
        print("nilai anda sempurna")
    elif nilai >= 90:
        print("anda dapat nilai a")
    else:
        print("anda dapat nilai b")
else:
    print("maaf anda tidak lulus")

print("terima kasih sudah menggunakan program ini")