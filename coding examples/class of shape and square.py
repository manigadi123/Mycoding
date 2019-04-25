class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0

class Sqaure(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.length=l
    def area(self):
        return self.length*self.length

obj=Sqaure(10)
print obj.area()
