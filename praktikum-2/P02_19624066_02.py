# NIM/Nama : 19624066/Nicholas Wise Saragih Sumbayak
# Tanggal : 31 Oktober 2024
# Deskripsi : Membuat pesan yang dapat mengubah pesan biasa menjadi pesan rahasia

'''
Kamus:
N, x: int

kamu_biasa, kamus_rahasia, arr_pesan: array

pesan: string
'''

N = int(input('Masukkan jumlah huruf pada kamus rahasia:')) #masukkan jumlah huruf yang ingin dikonversi

kamus_biasa = ['' for i in range(N)] #membuat list kamus biasa dengan item sebanyak n
kamus_rahasia = ['' for i in range(N)] #membuat list kamus rahasia dengan item sebanyak n

for i in range(N): #mengisi tiap elemen dalam list dengan input masing-masing, yang biasa dan rahasia
    kamus_biasa[i] = input(f'Masukkan huruf biasa ke-{i+1}: ')
    kamus_rahasia[i] = input(f'Masukkan huruf rahasia ke-{i+1}: ')

pesan = input('Masukkan pesan yang ingin diubah: ')  #input pesan
arr_pesan = [pesan[i] for i in range(len(pesan))] #membuat setiap huruf dalam pesan menjadi elemen tersendiri dalam list

for i in range(len(pesan)): #untuk setiap huruf i string pesan
    x = 0 #counter mulai dari  0
    while x < N: #untuk setiap x dari 0 sampai 2, jika huruf dengan index i sama dengan huruf dengan index x pada kamus, maka ganti isi array huruf dengan huruf rahasia
        if arr_pesan[i] == kamus_biasa[x]:
            arr_pesan[i] = kamus_rahasia[x]
            x = N #jika sudah ditemukan, buat x = N agar while tidak lanjut
        else: #jika tidak sama, naikkan terus nilai X
            x += 1    

print('Pesan Rahasia nona Sal:')
for letter in range(len(arr_pesan)):
    print(arr_pesan[letter], end='')  #print setiap huruf dalam list secara berturut-turut