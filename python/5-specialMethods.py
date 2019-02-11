# Special Methods: They are the methods that use dunder ("__ method __"), the double underscores
# 				   surrounding the method's name;
# __repr__ method: The goal of this method is to be unambiguous. This method is meant to show whatever function/class
#                  was used to get a certain data i.e. The string "Hello world" would be shown as "Hello world"
# 				   including the quotation marks to show that it is a string.
# __str__ method: The goal of this method is to be readable. This method would not show any unnecessary information,
# 				  but rather to be as user-friendly as possible.
class Employee:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

	def full_name(self):
		return "{0.first} {0.last}".format(self)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# Make sure you at least have this method, even if you don't have __str__ method;
	# We want this method to display info (about this class) more specific to a developer;
	def __repr__(self):
		return "Employee ('{0.first}', '{0.last}', '{0.pay}')".format(self)

	# This method is more arbitrary and can display any type of info, but it should be related to the class, of course;
	def __str__(self):
		return "{} - {}".format(self.full_name(), self.email)

	# We create our own adding method of this class;
	def __add__(self, other):
		return self.pay + other.pay

	# Creating a __len__ method;
	def __len__(self):
		return len(self.full_name())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# These is printing the __str__ method. If it can't find it, it will look for the __repr__ method instead;
print(emp_1)

# These two methods are exactly the same;
print(emp_1.__repr__())
print(repr(emp_1))

# These ones are also the same thing;
print(emp_1.__str__())
print(str(emp_1))

# Using the __add__ method we created inside our class;
print("=" * 30, " Using our __add__ method ", "=" * 40)
print(emp_1 + emp_2)

# STL examples of special methods;
print("=" * 30, " STL Examples ", "=" * 40)
print(str.__add__("a", "b"))
print(int.__add__(1, 2))
print("test".__len__())

print("=" * 30, " Using our own __len__ method ", "=" * 40)
print(len(emp_1))
