# NIM/Nama  : 19624066 / Nicholas Wise Saragih Sumbayak
# Tanggal   : 17 Oktober 2024
# Deskripsi : Soal Praktikum #1 

""" 
uang_peng, uang_kom, konversi_peng, konversi_kom, hitung_peng, hitung_kom = int
"""

uang_peng = int(input("Banyak uang Peng yang ditawarkan: ")) #Mata uang peng yang ditawarkan
uang_kom = int(input("Banyak uang Kom yang ditawarkan: ")) #Mata uang kom yang ditawarkan

konversi_peng = int(input("Konversi mata uang Peng ke rupiah: ")) # pengkali untuk konversi mata uang peng ke rupiah
konversi_kom = int(input("Konversi mata uang Kom ke rupiah: "))  # pengkali untuk konversi mata uang kom ke rupiah

hitung_peng = uang_peng * konversi_peng #mengkonversi mata uang peng ke rupiah
hitung_kom = uang_kom * konversi_kom #mengkonversi mata uang kom ke rupiah

if hitung_peng > hitung_kom: #jika lebih besar total uang peng, pilih uang peng
    print("Adik Tuan Leo memilih uang Peng")
else: #jika tidak, pilih uang kom
    print("Adik Tuan Leo memilih uang Kom")





