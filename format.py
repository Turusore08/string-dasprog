format0 = "Halo aku mau ngomong kalau {} {} {}".format('aku','suka','kamu')
format1 = "{2} {1} {0}".format ('aku','suka','kamu')
format2 = "{a} {s} {k}".format(a='aku',s='suka',k='kamu')
print('format untuk menginputkan suatu string ke dalam string ')
print(format0)
print(format1)
print(format2)

# menggunakan operator untuk menginput string dan bilangan

nama = 'ji'
banyak = 1

print('halo %s tuko o bubur %d'%(nama,banyak))

#menggunakan f untuk memasukkan string dan integer

print (f'halo {nama}beli o bubur {banyak}')

#menggunakan format untuk menulis biner dan lain lain

print (f'bilangan biner dari 16 adalah {16:b}')
print (f'hasil dari 1/6 adalah {1/6:.2f}')


#format untuk meletakkan di samping atau center string
print (f'|{'hai':<10}|{'|namaku':^10}|{'owi|':>10}')

