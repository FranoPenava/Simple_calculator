# Adding class for all of my methods so that there is not a mess in main.py file!

class Calc:
    # Making all of my methods static because there in no need to pass some parameter into my class!
    
    @staticmethod
    def addition(a: int, b: int ):
        return  int(a)+ int(b)
    
    @staticmethod
    def subtraction(a: int, b: int):
        return int(a)- int(b)
    
    @staticmethod
    def multiplication(a: int, b: int):
        return int(a) * int(b)
    
    @staticmethod
    def divide(a: int, b: int):
        return int(a)/int(b)
    
