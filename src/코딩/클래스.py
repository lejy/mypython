class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def say(self):
        return "hello"

class Circle(Point):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r = r

s = Circle(x=1,y=2,r=3)
print(s.r)
print(s.say())