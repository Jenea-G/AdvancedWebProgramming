class StudentRecord:
    def __init__(self, name, gpa, credits):
        if (self.is_valid(name)):
            self.name = name
        if(self.is_gpa_valid(gpa)):
           self.__gpa = gpa
        if(self.is_credits_valid(credits)):
            self.__credits = credits

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
    def is_credits_valid(gpa):
        if(credits > 0):
            return True
        else:
            return False
    