import turtle as t



class MagicBrush:


    def draw_square(self):
        t.color('green')
        for i in range(4):
            t.forward(100)
            t.right(90)

    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)   
    
    def go(self):
        t.forward(200)

    def turn(self):
        t.right(90)
        

#m1 = MagicBrush()
#m2 = MagicBrush()

brad = t.Turtle()
brad.shape('turtle')
brad.speed(10000)
for i in range(100):
    for i in range(5):
        brad.color('red')
        brad.forward(50)
        brad.right(180*4/5)

    brad.left(30)


for i in range(100):
    for i in range(5):
        brad.color('green')
        brad.forward(150)
        brad.right(180*4/5)

    brad.left(30)

for i in range(100):
    for i in range(5):
        brad.color('blue')
        brad.forward(250)
        brad.right(180*4/5)

    brad.left(30)

for i in range(100):
    for i in range(5):
        brad.color('pink')
        brad.forward(350)
        brad.right(180*4/5)

    brad.left(30)


t.mainloop()