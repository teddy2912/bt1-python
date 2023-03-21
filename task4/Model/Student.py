from Model.Person import Person

class Student(Person):
    def __init__(self, id, code, firstName, lastName, birthOfDate, math, physics, chemistry):
        super().__init__(id, code, firstName, lastName, birthOfDate)
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        