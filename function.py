# function 
def sayHello():
    print("Selamat Datang")
    sayHello()

def sayHello():
    return "Selamat Datang"
print(sayHello())

# function arguments
def sayHello(Lila):
    return "Selamat Datang" + Lila
print(sayHello("Lila"))

def addition(num1 , num2):
    result = num1 + num2 
    print(num1, "+", num2, "=", result)
    addition(15, 16)

# function default arguments
def sayHello(Lila=""):
    return "Selamat Datang" + Lila
print(sayHello())

# function keyword arguments
def fullname(fname, lname= ""):
    return fname + "" + lname

print(fullname(lname="Saputra", fname="Cahyo"))

# *args arbitrary arguments
def addition(*numbers):
    result = 0
    for n in numbers:
        result += n
        return result
    
# **kwargs arbitrary keyword arguments
def fullname(**kwargs):
    values = kwargs.values()
    print("".join(values))

    fullname(a="Ahmad", b="Dwi", c="Santoso")
