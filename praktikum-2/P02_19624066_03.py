# NIM/Nama : 19624066/Nicholas Wise Saragih Sumbayak
# Tanggal : 31 Oktober 2024
# Deskripsi : Game nona deb

'''
Kamus: 
N, penunjukan, max: int

kue, ditunjuk: array
'''
N = int(input('Banyak pemain: '))

kue = [0 for i in range(N)]

penunjukan = int(input('Jumalh penunjukan: '))

for i in range(N):
    if (i + 1) % 3 == 0:
        kue[i] = 3
    else:
        kue[i] = (i + 1) % 3
        
ditunjuk = [int(input(f'Orang ke-{i + 1} yang ditunjuk: ')) for i in range(penunjukan)]

for i in range(len(ditunjuk)):
    if ((ditunjuk[i] - 1 - kue[ditunjuk[i] - 1]) < len(kue)) and ((ditunjuk[i] - 1 - kue[ditunjuk[i] - 1]) >= 0):
        kue[ditunjuk[i] - 1 - kue[ditunjuk[i] - 1]] -= 1
        kue[ditunjuk[i] - 1] += 1
        if kue[ditunjuk[i] - 1] > 3:
            kue[ditunjuk[i] - 1] = 3
        if kue[ditunjuk[i] - 1 - kue[ditunjuk[i] - 1]] < 0:
            kue[ditunjuk[i] - 1 - kue[ditunjuk[i] - 1]] = 0
    if ((ditunjuk[i] - 1 + kue[ditunjuk[i] -1]) < len(kue)) and ((ditunjuk[i] - 1 + kue[ditunjuk[i] -1]) >= 0):
        kue[ditunjuk[i] - 1 + kue[ditunjuk[i] -1]] -= 1
        kue[ditunjuk[i] - 1] += 1
        if kue[ditunjuk[i] - 1] > 3:
            kue[ditunjuk[i] - 1] = 3
        if kue[ditunjuk[i] - 1 + kue[ditunjuk[i] - 1]] < 0:
            kue[ditunjuk[i] - 1 + kue[ditunjuk[i] - 1]] = 0    
            
    kue[ditunjuk[i] - 1] += 1
    for x in range(len(kue)):
        if kue[x] > 3:
            kue[x] = 3
        if kue[x] < 0:
            kue[x] = 0
        
 
print(kue)
max = 0       
        
for i in range(len(kue)):
    if kue[i] > max:
        max = kue[i]
        
print('Orang yang memiliki kue terbanyak adalah orang ', end=' ')
for i in range(len(kue)):
    if kue[i] == max:
        print(i + 1, end=' ')