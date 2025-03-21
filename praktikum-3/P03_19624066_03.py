# NIM/Nama: Nicholas Wise Saragih Sumbayak
# Tanggal: 21/11/2024
# Deskripsi : Menghitung jumlah elemen dalam list untuk permainan Nona Deb dan Nona Sal

'''
target, kartu_deb, kartu_sal, total, max, i: int
arr_deb, arr_sal, arr, deb, sal = array
buat_array(num), sum_arr(arr): fungsi
permainan(deb, sal, max): prosedur
'''
#masukkan input untuk target, kartu_deb, kartu_sal
target = int(input('Masukkan target poin: '))
kartu_deb = int(input('Kartu nona deb: '))
kartu_sal = int(input('Kartu nona sal: '))


def buat_array(num): #membuat sebuah fungsi yang membuat array dari angka yang dimasukkan untuk memudahkan perhitungan
    return [(num // 1000), ((num // 100) % 10), (num % 100) // 10, (num % 10)]

#membuat array dari angka-angka yang telah dimasukkan
arr_deb = buat_array(kartu_deb)
arr_sal = buat_array(kartu_sal)

def sum_arr(arr): #membuat sebuah fungsi untuk memudahkan perhitungan total untuk setiap elemen dalam array
    total = 0
    for i in range(4):
        total += arr[i]
    return total

def permainan(deb, sal, max): #prosedur yang menerima array nona deb, nona sal, serta targetnya
    i = 1 #giliran ke-
    while sum_arr(deb) < max and sum_arr(sal) < max:
        giliran = input('Giliran ' + str(i) + ' (tambah / tukar): ')
        posisi = int(input('Pada posisi kartu ke: '))
        
        if i % 2 != 0: #karena nona deb dahulu, maka untuk setiap giliran ganjil, giliran tersebut giliran nona deb
            if giliran == 'tambah': #langsung menambahkan untuk posisi yang dipilih
                deb[posisi] += 1
            elif giliran == 'tukar': 
                placeholder = deb[posisi] #placeholder ini adalah variable untuk menyimpan nilai dari salah satu array supaya dapat ditukar
                deb[posisi] = sal[posisi]
                sal[posisi] = placeholder
        elif i % 2 == 0: #setiap giliran genap adalah giliran nona sal
            if giliran == 'tambah':
                sal[posisi] += 1
            elif giliran == 'tukar':
                placeholder = sal[posisi]
                sal[posisi] = deb[posisi]
                deb[posisi] = placeholder
                
    #mengecek siapa yang memenangkan permainan, dan print sesuai hasil tersebut
    if sum_arr(deb) >= max:
        print('Nona Deb memenangkan permainan') 
    elif sum_arr(sal) >= max:
        print('Nona Sal memenangkan permainan')
        
permainan(arr_deb, arr_sal, target) #memanggil fungsi dengan memasukkan array nona deb, nona sal, serta target