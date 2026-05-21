class StudentRecord:
    def __init__(self, name, gpa, credits):
        if (self.is_valid(name)):
            self.name = name
        else:
            raise ValueError("You should provide a valid name")
        self.gpa = gpa
        self.credits = credits
        print(f"The sudent {self.name} have been successfully recorded.")

    @staticmethod
    def is_valid(name):
        if(len(name.strip()) > 0):
            return True
        else:
            return False 
        
    @staticmethod
    def is_gpa_valid(gpa):
        if(0 < gpa <= 4):
            return True
        else:
            return False
    
    @staticmethod
    def are_credits_valid(credits):
        if(credits >= 0):
            return True
        else:
            return False
        
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if(self.is_gpa_valid(value)):
            self.__gpa = value
        else:
            raise ValueError("The value of gpa must be between 0 and 4")
  
    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, value):
        if(self.are_credits_valid(value)):
            self.__credits = value
        else:
            raise ValueError("Credits must always be greater than or equal to 0")
        
    @property
    def academic_status(self):
        if(self.gpa >= 3.5):
            return "Honours"
        if(self.gpa >= 2.0):
            return "Good Standing"
        else:
            return "At Risk"

    def add_credits(self, amount):
        if(amount > 0):
            self.__credits += amount
        else:
            raise ValueError("Only a positive amount can be added")

    def update_gpa(self, value):
        self.gpa = value

    def display_info(self):
        print(f"Student {self.name} has the gpa: {self.gpa} and {self.credits} credits.")

    

    