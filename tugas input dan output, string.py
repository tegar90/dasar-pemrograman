#!/usr/bin/env python
# coding: utf-8

# In[6]:


nama = input('Isikan nama anda: ')
tanggal = input('Isikan tanggal lahir (dd/mm/yyyy): ')
nim = input('Isikan nim: ')
kelas = input('Isikan kelas: ')
alamat = input('isikan alamat:')

list_biodata = nama.split()
print("Nama Awal:", list_biodata[0])
print("Nama Akhir:", list_biodata[-1])
print("NIM:", nim)
print("Kelas:", kelas)
print("alamat:", alamat)

list_tanggal = tanggal.split("/")
if list_tanggal[1] == "01":
    keterangan = "Januari"
elif list_tanggal[1] == "02":
    keterangan = "Februari"
elif list_tanggal[1] == "03":
    keterangan = "Maret"
elif list_tanggal[1] == "04":
    keterangan = "April"
elif list_tanggal[1] == "05":
    keterangan = "Mei"
elif list_tanggal[1] == "06":
    keterangan = "Juni"
elif list_tanggal[1] == "07":
    keterangan = "Juli"
elif list_tanggal[1] == "08":
    keterangan = "Agustus"
elif list_tanggal[1] == "09":
    keterangan = "September"
elif list_tanggal[1] == "10":
    keterangan = "Oktober"
elif list_tanggal[1] == "11":
    keterangan = "November"
elif list_tanggal[1] == "12":
    keterangan = "Desember"

print("Bulan lahir:", keterangan)
print("Tanggal lahir:", list_tanggal[0])
print("Tahun lahir:", list_tanggal[2])


# In[11]:


kampus = "universitas nusa putra sukabumi"
#a
input_1 = kampus[17:23] + kampus[12:17]
print(input_1)
#b
input_2 = kampus[1:12] + kampus[12:17]
input_2 = kampus.replace("u","")
print(input_2)
#c
input_3 = kampus[23:32] + " " +  kampus[17:23] + kampus[12:17] + kampus[0:12]
print(input_3)
#d
input_4= kampus[0:1] + kampus[12:13] + kampus[17:18] + kampus[23:24]
print(input_4)
#e
input_5= kampus[8:12] , kampus[14:19] ,kampus [27:31]
print(input_5)


# In[ ]:




