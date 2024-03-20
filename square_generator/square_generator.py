#Task 3 : Classes
#Create a class called SquareGenerator that has a method
#to generate squares for a given range of numbers.

class SquareGenerator:
    def generate(self, start, end):
        if start > end:
            return Exception("Incorrect input! start value is smaller than end value")
        else:
            return [number ** 2 for number in range(start, end + 1)]