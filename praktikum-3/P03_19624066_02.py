# NIM/Nama: Nicholas Wise Saragih Sumbayak
# Tanggal: 21/11/2024
# Deskripsi : Subprogram untuk menghitung digit genap dan ganjil pada bilangan

'''
number, n, posisi, sum_ganjil, sum_genap, iterasi, jumlah, count: int
ganjil(), genap(): fungsi
pengubah(): prosedur

'''

number = int(input('Masukkan bilangan: ')) #Masukkan angka 

def ganjil(n): #definisikan fungsi yang akan menghitung jumlah angka pada digit ganjil
    posisi = 1
    sum_ganjil = 0
    while n > 0:
        if posisi % 2 != 0: #jika iterasi ganjil, tambahkan angka terakhir
            sum_ganjil += n % 10
        posisi += 1
        n //= 10
    return sum_ganjil

def genap(n): #definisikan fungsi yang akan menghitung jumlah angka pada digit genap
    posisi = 1
    sum_genap = 0
    while n > 0:
        if posisi % 2 == 0:
            sum_genap += n % 10
        posisi += 1
        n //= 10
    return sum_genap

def pengubah(n): #definisikan prosedur yang akan memproses sebuah angka dan mengolah angka berdasarkan iterasinya
    iterasi = 1 #iterasi ke berapa
    count = 0 #jumlah iterasi yang dibutuhkan
    jumlah = n
    
    if jumlah < 10: #jika hanya 1 angka, maka akan langsung diberikan total jumlah iterasi = 1
        count = 1
    
    while jumlah >= 10:
        if iterasi % 2 == 0: #iterasi genap, panggil fungsi genap
            jumlah = genap(jumlah)
            iterasi += 1
            count += 1

        elif iterasi % 2 != 0: #iterasi ganjil, panggil fungsi ganjil
            jumlah = ganjil(jumlah) 
            iterasi += 1
            count += 1
    
    print('Mesin berhenti setelah ' + str(count) + ' operasi, mengeluarkan angka ' + str(jumlah))
    
pengubah(number) #panggil prosedur pengubah
