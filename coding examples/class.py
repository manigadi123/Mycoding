class Person:
    # define the class parameter "name"
    name="Person"

    def __init__(self,name=None):
        #self.name is the instance parameter
        self.name=name
jerry=Person("Jeffrey")
print "%s name is %s" %(Person.name,jerry.name)
nico=Person()
nico.name="Nico"
print "%s name is %s" %(Person.name,nico.name)
