#warmUp
# Mendefinisikan fungsi lambda untuk menghitung kuadrat
kuadrat = lambda x: x ** 2

# Lambda dengan argumen 5
hasil = kuadrat(5)
print(hasil) #25

hasil = kuadrat(3)
print(hasil) #9

# Menggunakan map
angka = [1, 2, 3, 4, 5]
hasil_kuadrat_list = list(map(lambda x: x**2, angka))
print(hasil_kuadrat_list) # [1, 4 ,9, 16, 25]

# Applied
belanja = [12000, 5000, 30000, 8000]
mahal = list(filter(lambda x: x>=10000, belanja))
print(mahal) # [12000, 30000]

