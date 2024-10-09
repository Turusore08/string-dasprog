string0 = "Arya Pratama Rhama Putra"
string1 = "5054241026"
string2 = 'Blora'
string3 = "Saya mahasiswa RKA"



print(f"Nama saya adalah {string0}")
print(f"NRP {string1}")
print(f"Asal Daerah {string2}")
print(f"inisial nama saya adalah {string0[0]},{string0[5]},{string0[13]},{string0[19]}")
print(f"Nama belakang {string0[19:]}")
print(f"Nama panggilan {string0[13:18]}")

#menghapus char ditengah kata pada string kota asal
print(f'Blora jika nggak pakai lo jadi apa hayo? jadi {string2[:1]}{string2[3:]}')
