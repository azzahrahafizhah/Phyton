# format syntax lambda
# lambda arguments : expressions
lambda name : print("Selamat Datang", name) # type: ignore

# membuat lambda
lambda name : print("Selamat Datang", name)

# membuat lambda dalam variable
sayHello = lambda name : print("Selamat Datang", name)

# variable sayHello sudah menjadi sebuah function
sayHello("Siska")

# lambda tanpa argumen
(lambda : print("Selamat Datang"))()

# lambda tanpa argumen
(lambda name : print("Selamat Datang", name))("Siska")

# lambda dengan default argumen
(lambda name="" : print("Selamat Datang", name))()