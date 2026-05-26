from enum import Enum

class StudentLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class Student:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if not isinstance(value, StudentLevel):
            raise ValueError(f"Student level should be a part of StudentLevel enum. Sudent {self.name} wasn't created")
        self.__level = value

    def display_info(self):
        print(f"Student {self.name} has {self.level.value} level")

try:
    s1 = Student ("Paul", "beginner")
    s1.display_info()
except ValueError as e:
    print("Error:", e)

try:
    s2 = Student ("Sally", StudentLevel.INTERMEDIATE)
    s2.display_info()
except ValueError as e:
    print("Error:", e)