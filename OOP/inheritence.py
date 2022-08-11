from classes_object import Person

class Manager(Person):

    profession = "Manager"
    def __init__(self, fn, ln):
        super().__init__(fn, ln)

man = Manager("Kaustubh", "Pathwardhan")
print(man.profession)
print(man.full_name())
