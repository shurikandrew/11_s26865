#Task 3 : Classes
#Create a class called SquareGenerator that has a method
#to generate squares for a given range of numbers.
from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    @abstractmethod
    def generate(self, start, end):
        pass