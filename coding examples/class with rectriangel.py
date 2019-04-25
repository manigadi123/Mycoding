class Rectangle(object):
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.l*self.w

rect=Rectangle(3,4)
print rect.area()
