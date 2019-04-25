class A():
    pass
class B():
    pass
class C(B,A):
    def drive(self):
        print("good thing")
        return "mani"
    
class D(C,B,A):
    pass

d=D()
d.drive()



        
