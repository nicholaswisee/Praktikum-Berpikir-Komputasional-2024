# NIM/Nama  : 19624066 / Nicholas Wise Saragih Sumbayak
# Tanggal   : 17 Oktober 2024
# Deskripsi : Soal Praktikum #2

""" 
input_digit, digit4, digit3, digit2, digit1, sum_digit = int
"""

input_digit = int(input("Masukkan sebuah bilangan: "))

digit4 = input_digit % 10 #mencari angka satuan
digit3 = int((input_digit % 100 - digit4) / 10) #mencari angka puluhan
digit2 = int((input_digit % 1000 - digit3 * 10 - digit4) / 100) #mencari angka ratusan
digit1 = int((input_digit - (digit2 * 100) - (digit3 * 10) - digit4) / 1000) #mencari angka ribuan

sum_digit = digit1 + digit2 + digit3 + digit4 #mencari sum/total dari masing-masing angka


if (digit1 != digit2) and (digit1 != digit3) and (digit1 != digit4) and (digit2 != digit3) and (digit2 != digit4) and (digit3 != digit4) and (sum_digit % 2 != 0): #mengecek apakah ada bilangan duplikat
    if ((digit1 > digit4) and (input_digit % 2 == 0)) or ((digit1 > digit4) and (digit2 + digit3 > digit1)) or ((input_digit % 2 == 0) and (digit2 + digit3 > digit1)): #mengecek harus memenuhi setidaknya 2 dari 3 syarat menggunakan kombinasi
        print("Bilangan tersebut adalah bilangan Super Unik.")
    else: 
        print("Bilangan tersebut adalah bilangan Unik")
else:
    print("Bilangan tersebut adalah bilangan biasa.")