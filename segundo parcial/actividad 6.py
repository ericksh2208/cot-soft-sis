import turtle
class TurtleForNoobs:
    def cuadrado(self):
        SKK = turtle.Turtle()
        for i in range(4):
            SKK.forward(50)
            SKK.right(90)
        turtle.done()
        
    def estrella(self):
            star = turtle.Turtle()
            star.right(75)
            star.forward(100)
            for i in range(4):
                star.right(144)
                star.forward(100)
            turtle.done()
    def ks(self, length, d):
         if d == 0:
              turtle.forward(length)
         else:
              length = length / 3
              d = d - 1
              self.ks(length, d)
              turtle.right(60)
              self.ks(length, d)
              turtle.left(120)
              self.ks(length, d)
              turtle.right(60)
              self.ks(length, d)
    
    def snowflake(self):
         turtle.reset()
         turtle.ht()
         #colors = ["red", "orange", "pink"]
         for i in range(3):
              #turtle.color(colors[1])
              self.ks(200, 3)
              turtle.left(120)
         turtle.update()
         turtle.done()

t = TurtleForNoobs()
t.snowflake()
