import math

#Task 1: List Comprehensions
#Write a Python program that generates a list of squares of numbers
#from 1 to 10 using list comprehensions.ares)

squares_list = [number**2 for number in range(1,11)]
print("List of squares: ",squares_list)

#Task 2: Functions
#Expand the previous program by defining a function that takes a range of numbers as input
#and returns a list of squares for that range.e_squares(start,end))

def e_squares(start, end):
    return [number**2 for number in range(start,end+1)]

print("List from e_squares function: ",e_squares(3,20))


#Task 3 : Classes
#Create a class called SquareGenerator that has a method
#to generate squares for a given range of numbers.

class SquareGenerator:
    def generate(self, start, end):
        return [number ** 2 for number in range(start, end + 1)]


generator = SquareGenerator()
class_generator_list = generator.generate(7, 25)
print("List from SquareGenerator class: ", class_generator_list)

#Task 4 : Libraries

square_root_list = [int(math.sqrt(number)) for number in class_generator_list]
print("List of square roots from squares: ", square_root_list)