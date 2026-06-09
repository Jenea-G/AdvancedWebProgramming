class Helper:
    @staticmethod
    def isValidName(value):
        if(len(value.strip()) > 0):
            return True
        return False
    
    @staticmethod
    def isGreaterThan0(value):
        if value > 0:
            return True
        return False
    
    @staticmethod
    def isPositiveNumber(value):
        if value >= 0:
            return True
        return False