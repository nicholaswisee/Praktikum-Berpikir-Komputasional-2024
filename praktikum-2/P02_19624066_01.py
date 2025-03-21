# NIM/Nama : 19624066/Nicholas Wise Saragih Sumbayak
# Tanggal : 31 Oktober 2024
# Deskripsi : Program mencari angka yang dapat dibagi angka terakhirnya

'''
Kamus:
A, B, count: int
'''

A = int(input('Masukkan Nilai A: '))
B = int(input('Masukkan Nilai B: '))

count = 0

for num in range(A, B + 1):
    if num % 10 != 0:
        if (num % (num % 10) == 0):
            count += 1
        
print(f'Terdapat {count} angka yang memenuhi sifat tersebut.')

