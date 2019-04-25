class Person(object):
    def getGender(self):
        return "unknown"

class Male(Person):
    def getGender(self):
        return "male"
class Female(Person):
    def getGender(self):
        return "Female"

obj=Female()
obj1=Male()
print obj.getGender()
print obj1.getGender()
