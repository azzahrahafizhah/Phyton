# membuat file dan menulis isi
file = open("data.txt", "w")
file.write("Halo, Semangat belajar Fiqh!")
file.close

# membaca isi file
file = open ("data.txt", "r")
print("isi file:")
print(file.read())
file.close()

# menambahkan isi baru ke file
file = open("data.txt", "a")
file.write("\nsemangat\nyah!")
file.close()

# \n itu untuk menambahkan baris baru
# kenapa kita harus belajar file handling?
# karena file handling ini digunakan untuk menyimpan data secara permanen walaupun programnyaa ditutup.
# working directory