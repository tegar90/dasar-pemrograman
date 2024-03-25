#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hitung_tarif_umur_tinggi(umur, tinggi):
    tarif = 0
    
    if umur < 2:
        return "Dilarang masuk"
    elif umur < 4:
        tarif = 30000
        if tinggi > 70:
            tarif += 10000
    elif umur < 7:
        tarif = 40000
        if tinggi > 120:
            tarif += 15000
    elif umur < 10:
        tarif = 50000
        if tinggi > 150:
            tarif += 20000
    else:
        tarif = 80000
    
    return tarif

def main():
    while True:
        try:
            umur = int(input("Masukkan umur anak: "))
            tinggi = int(input("Masukkan tinggi anak (dalam cm): "))
            break
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    
    tarif = hitung_tarif_umur_tinggi(umur, tinggi)
    
    if isinstance(tarif, str):
        print(tarif)
    else:
        print("Tarif yang harus dibayarkan:", tarif)

if __name__ == "__main__":
    main()


# In[ ]:




