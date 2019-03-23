# Classes and instances

# Class: A blueprint (mold) for creating instances of a class;
# Instance: A unique set of data created from a class. Also known as an 'object';
# All regular methods pass the instance itself automatically when they are called. You don't need, and shouldn't
# specify it when calling them;


class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

	def full_name(self):
		return "{0.first} {0.last}".format(self)


# We create 2 instances from the class Employee:
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)
print(emp_2.email)

# Here the method passes the instance as the argument automatically "full_name(emp_1)" that's why we need the "self"
print(emp_1.full_name())

# Here we use the method on the class and then pass the instance as an argument. This is actually what the
# previous method is doing in the background;
print(Employee.full_name(emp_2))