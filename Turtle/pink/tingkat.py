from turtle import *

getscreen()
bgcolor("pink")

fillcolor("purple")
begin_fill()

init_size = 10
for i in range(10):
    circle(init_size)
    init_size += 10

end_fill()

shape("arrow")

done()