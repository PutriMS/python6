import random
import string
import os
print("_"*15, "MEAN", "_"*15)
lanjut = True
angkas = []
while lanjut == True:
    
    angka = int(input("Masukkan angka = "))
    lanjuts = input("lanjut(y/n)= ")
    if lanjuts == 'y':
        angkas.append(angka)
        print(angkas)
        lanjut = True
        os.system('cls')
        continue
    elif lanjuts == 'n':
        angkas.append(angka)
        lanjut = False
        os.system('cls')
        break
    if lanjuts == 'Y':
        angkas.append(angka)
        print(angkas)
        lanjut = True
        os.system('cls')
        continue
    elif lanjuts == 'N':
        angkas.append(angka)
        lanjut = False
        os.system('cls')
        break
    else:
        print('tidak diketahui')
        break
  
def mean () :
    rata = 0
    rata = sum(angkas)/ len(angkas)
    return rata
print(f"Hasil mean {angkas} = {mean()}")
