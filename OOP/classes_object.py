class Person:

    profession = "Employee"
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def full_name(self):
        return self.fname+" "+self.lname



p = Person("ritesh", "jadhav")

print(p.full_name())
