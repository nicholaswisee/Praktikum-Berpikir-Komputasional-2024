# NIM/Nama  : 19624066 / Nicholas Wise Saragih Sumbayak
# Tanggal   : 17 Oktober 2024
# Deskripsi : Soal Praktikum #3

""" 
kunci_bebek, kunci_ayam, kunci_kupu, clay_merah, clay_biru, clay_ungu = int
"""

kunci_bebek = int(input("Masukkan jumlah pesanan gantungan kunci bunga: ")) #cari jumlah kunci bebek
kunci_ayam = int(input("Masukkan jumlah pesanan gantungan kunci ayam: ")) #cari jumlah kunci ayam
kunci_kupu = int(input("Masukkan jumlah pesanan gantungan kunci kupu-kupu: ")) #cari jumlah kunci kupu

clay_merah = int(input("Masukkan jumlah clay merah: ")) #jumlah clay merah
clay_biru = int(input("Masukkan jumlah clay biru: ")) #jumlah clay biru
clay_ungu = int(input("Masukkan jumlah clay ungu: ")) #jumlah clay ungu

clay_merah = clay_merah - (2 * kunci_bebek) - kunci_ayam - kunci_kupu #mengurangi jumlah clay biru dengan yang diperlukan untuk kunci
clay_biru = clay_biru - kunci_bebek - (2 * kunci_ayam) - kunci_kupu #mengurangi jumlah clay merah biru dengan yang diperlukan untuk kunci

if (clay_merah >= 0) and (clay_biru >= 0): #mengecek apabila biru dan merah sisa
    clay_ungu = clay_ungu - (3 * kunci_kupu) #menghitung jumlah clay ungu yang dibutuhkan
    if clay_ungu < 0: #jika dibutuhkan clay
        if clay_merah == clay_biru: #jika jumlah merah dan biru sama, dapat digabungkan dan membentuk clay ungu dengan menjumlahkannya
            clay_ungu = clay_ungu + (clay_merah + clay_biru)
        elif clay_merah < clay_biru: #jika merah lebih sedikit dari biru, dapat dibuat ungu sejumlah merah dikali 2, dengan biru bersisa
            clay_ungu = clay_ungu + (2 * clay_merah)
        elif clay_merah > clay_biru: #jika biru lebih sedikit dari merah, dapat dibuat ungu sejumlah biru dikali 2, dengan merah bersisa
            clay_ungu = clay_ungu + (2 * clay_biru)
        if clay_ungu >= 0: #sekarang cek clay ungu, jika sudah >= 0 maka sudah dapat dibuat pesanannya, karena ungu sebelumnya negatif karena ungu yang ada dikurangi dengan yang dibutuhkan
            print("Pesanan dapat diterima oleh Nona Sal")
        else:  #jika masih belum cukup, tidak dapat dibuat pesanannya
            print("Pesanan tidak dapat diterima oleh Nona Sal")
    else: #jika tidak butuh clay lagi, maka bisa diterima
        print("Pesanan dapat diterima oleh Nona Sal")
else: #jika biru dan merah kurang dari 0, maka tidak dapat dibuat pesanannya
    print("Pesanan tidak dapat diterima oleh Nona Sal")
            
