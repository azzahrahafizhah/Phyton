# list biasa
names = ["Andi", "Beni", "Cahyo"]
print(names[0])
print(names[1])
print(names[2])

# tuple biasa
names = ("Andi", "Beni", "Cahyo")
print(names[0])
print(names[1])
print(names[2])

# konversi ke dalam list
name_list = list(names)

# lakukan manipulasi
names_list.appendi("Dodi")
names_list[2] = "Cahyo Saputra"
names_list.remove("Andi")

# konversi ke dalam tuple
names = tuple(names_list)

# set biasa
names = {"Andi", "Beni", "Cahyo"}
print(names)

# dictionary biasa
student = {'name':'Andi', 'address':'Jakarta'}

# format penulisan dict bisa menyusun ke bawah
student = {
    'name':'Andi'
    'address':'Jakarta'
    'age':17
    'active':True
    'hobbies': [
        'swimming'
        'soccer'
        'climbing'
    ]
}

print(student['age'])