# NIM/Nama: Nicholas Wise Saragih Sumbayak
# Tanggal: 21/11/2024
# Deskripsi : Program menghitung diskriminan

'''
a, b, c, det, x2, x1, k, determinan: int
determinan(), output(): function
'''
#Masukkan nilai a, b, dan c
a = int(input('Masukkan nilai a: ')) 
b = int(input('Masukkan nilai b: '))
c = int(input('Masukkan nilai c: '))

def determinan(x2,x1,k): #subprogram fungsi untuk menghitung dan mengembalikan nilai determinan 
    det = (x1 ** 2) - (4 * x2 * k) #x2 sebagai a, x1 sebagai b, k sebagai c menyesuaikan dengan bentuk persamaan x kuadrat, x, dan konstanta
    return det

def output(determinan): #subprogram prosedur untuk output nilai determinan serta output kondisi akar berdasarkan nilai determinan
    print('Nilai diskriminan: ' + str(determinan))
    if determinan > 0: #melakukan print berdasarkan petunjuk determinan yang diberikan di soal
        print('Persamaan kuadrat memiliki akar berbeda')
    elif determinan < 0: 
        print('Persamaan kuadrat tidak memiliki akar real')
    else: 
        print('Persamaan kuadrat memiliki akar kembar')
        
output(determinan(a, b, c)) #memanggil prosedur output hasil perhitungan dari fungsi determinan