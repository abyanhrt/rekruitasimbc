while True:
    print("=========================================================")
    print("==============PROGRAM KALKULATOR SEDERHANA===============")
    print("======================HADIAH 1 MBC=======================")
    print("===============by Muhammad Abyan Harits==================")
    print()

    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print()

    pilihan = int(input("Masukkan pilihan operasi: "))
    num1 = float(input("Angka pertama: "))
    num2 = float(input("Angka kedua: "))
    print()

    if pilihan == 1:
        print("Hasil dari", num1, "+", num2, "=", round(num1 + num2, 2))
    elif pilihan == 2:
        print("Hasil dari", num1, "-", num2, "=", round(num1 - num2, 2))
    elif pilihan == 3:
        print("Hasil dari", num1, "*", num2, "=", round(num1 * num2, 2))
    elif pilihan == 4:
        print("Hasil dari", num1, "/", num2, "=", round(num1 / num2, 2))
    else:
        print("Maaf, pilihan menu tidak tersedia")

    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if ulangi.lower() != "ya":
        break



