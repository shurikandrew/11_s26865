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