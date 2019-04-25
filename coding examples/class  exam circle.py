class Circle(object):
    def __init__(self,r):
        self.r=r

    def area(self):
        return self.r**2*3.14

cim=Circle(26)
print cim.area()
