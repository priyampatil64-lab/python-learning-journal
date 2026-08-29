# Day 11 - Pillars of OOP: Abstraction & Encapsulation Examples

# ---------- Abstraction (conceptual example) ----------
# When using a built-in method, we don't see or care about its internal implementation.
my_list = [3, 1, 2]
my_list.sort()          # we just know it sorts - we don't need to know HOW
print(my_list)           # [1, 2, 3]

class CoffeeMachine:
    def make_coffee(self):
        self.__boil_water()
        self.__add_coffee_powder()
        self.__pour_into_cup()
        print("Coffee is ready!")

    def __boil_water(self):        # internal detail, hidden from the user
        print("Boiling water...")

    def __add_coffee_powder(self):  # internal detail, hidden from the user
        print("Adding coffee powder...")

    def __pour_into_cup(self):      # internal detail, hidden from the user
        print("Pouring into cup...")


machine = CoffeeMachine()
machine.make_coffee()   # user only interacts with make_coffee(), not the internal steps

# ---------- Encapsulation: public vs protected vs private ----------
class Student:
    def __init__(self, name, marks):
        self.name = name            # public - freely accessible
        self._school = "ABC School"  # protected - convention only, still accessible
        self.__marks = marks         # private - name-mangled, harder to access directly


student = Student("Priyam", 88)
print(student.name)             # works fine - public
print(student._school)          # works, but the underscore signals "internal use"

# print(student.__marks)        # this would raise an AttributeError - private attribute
print(student._Student__marks)  # only works because of name-mangling - NOT the intended way to access it

# ---------- Encapsulation with getter and setter methods ----------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def get_balance(self):         # getter - safe way to READ the value
        return self.__balance

    def set_balance(self, amount): # setter - safe way to UPDATE the value, with validation
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")


account = BankAccount(1000)
print(account.get_balance())    # 1000

account.set_balance(1500)
print(account.get_balance())    # 1500

account.set_balance(-500)       # rejected by the setter's validation
print(account.get_balance())    # still 1500, unchanged

# ---------- Combined example: Employee with encapsulated salary ----------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary     # private, protected from direct outside changes

    def get_salary(self):
        return self.__salary

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"{self.name}'s new salary: Rs.{self.__salary}")
        else:
            print("Raise amount must be positive.")


emp = Employee("Ravi", 30000)
print(emp.get_salary())    # 30000
emp.give_raise(5000)       # Ravi's new salary: Rs.35000
emp.give_raise(-1000)      # Raise amount must be positive.
