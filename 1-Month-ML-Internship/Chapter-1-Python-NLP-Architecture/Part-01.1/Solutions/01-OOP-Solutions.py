"""
Solutions for Exercise Set 1: Object-Oriented Programming Fundamentals
"""

# ===== BEGINNER SOLUTIONS =====

class Person:
    """Simple Person class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"{self.name} is {self.age} years old")

class Dog:
    """Dog class with methods"""
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday to {self.name}!"

# ===== INTERMEDIATE SOLUTIONS =====

class BankAccount:
    """Bank account with deposit/withdraw"""
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def print_statement(self):
        print(f"Account: {self.account_holder}, Balance: ${self.balance:.2f}")

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# ===== ADVANCED SOLUTIONS =====

class MLModel:
    """Base class for ML models"""
    def __init__(self, model_name, parameters=None):
        self.model_name = model_name
        self.parameters = parameters or {}
    
    def __str__(self):
        return f"MLModel({self.model_name})"
    
    def get_params(self):
        return self.parameters.copy()
    
    def set_params(self, **kwargs):
        self.parameters.update(kwargs)
        return self

if __name__ == "__main__":
    person = Person("Alice", 25)
    person.display_info()
    
    dog = Dog("Rex", "Labrador", 3)
    print(dog.bark())
    print(dog.birthday())
