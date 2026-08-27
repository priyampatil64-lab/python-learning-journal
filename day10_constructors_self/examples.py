# Day 10 - Constructors and the self Keyword Examples

# ---------- __init__() constructor + self ----------
class Person:
    def __init__(self, name, age):
        self.name = name   # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


person1 = Person("Arjun", 22)
person1.introduce()
# Output: My name is Arjun and I am 22 years old.

# ---------- Multiple objects with different attributes ----------
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: Rs.{self.price}")


laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)
laptop1.show_info()
laptop2.show_info()

# ---------- Optional (default) parameters in constructors ----------
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")


book1 = Book("Python Programming")               # author defaults to "Unknown"
book2 = Book("Machine Learning", "Andrew Ng")     # author explicitly given
book1.show_book()
book2.show_book()


# ============================================================
# Homework
# ============================================================

# ---------- Homework 1: Movie class ----------
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def show_movie(self):
        print(f"Movie: {self.title}, Rating: {self.rating}")


movie1 = Movie("Inception", 8.8)
movie2 = Movie("Interstellar", 8.6)
movie1.show_movie()
movie2.show_movie()


# ---------- Homework 2: Employee class with default salary ----------
class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def show_employee(self):
        print(f"Name: {self.name}, Designation: {self.designation}, Salary: Rs.{self.salary}")


emp1 = Employee("Priyam", "Software Engineer Intern")          # uses default salary
emp2 = Employee("Ravi", "Senior Developer", 85000)               # overrides default salary
emp1.show_employee()
emp2.show_employee()
