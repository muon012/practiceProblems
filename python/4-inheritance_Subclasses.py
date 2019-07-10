# Subclass: A class that inherits all the methods, data, and attributes of another "parent" class.
# Method Resolution Order: The order by which python looks for certain methods in a class/object that may be inherited;

# -------------- super() BEST PRACTICE ------------------
# super() enables you to access the methods and members of a parent class without referring to the parent class by name.
# For a single inheritance situation the first argument to super() should be the name of the current child class
# calling super(), and the second argument should be self, that is, a reference to the current object calling super().


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


class Developer(Employee):
	# This attribute overrides the attribute from Employee, however, it doesn't change the Employee class at all;
	raise_amount = 1.10

	def __init__(self, first, last, pay, language):
		super().__init__(first, last, pay) # This says to make the Employee class handle the first three parameters;
		# Employee.__init__(self, first, last, pay) # This is another way to inherit from the parent class Employee;
		self.language = language


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		"""This method uses the Employee class as its parent class and passes a new parameter in the form of a list"""
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_employees(self):
		if not self.employees:
			print("No employees to manage.")
		else:
			for employee in self.employees:
				print("--->", employee.full_name())


# Check this print to see the method resolution order of the class Developer
print(help(Developer))

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Mike", "Spears", 60000, "c++")
dev_3 = Developer("Jim", "Petterson", 50000, "Python")

# These Developer objects, inherit the __init__ method from the Employee class;
print(dev_1.email)
print(dev_2.email)

# This let us see all the things inherited for the subclass Developer;
help(Developer)

# The raise of pay comes from the Developer class and not the Employee class;
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print("=" * 140)

# We print the developer's programming languages;
print(dev_1.language)
print(dev_2.language)


print("=" * 140)

# We create Manager objects;
manager_1 = Manager("Jay", "Bagadonuts", 90000)
manager_2 = Manager("Rich", "Evans", 90000, [dev_1, dev_2])

print(manager_1.email)
manager_1.print_employees()

print("=" * 140)

# We use the methods in the Manager class;
manager_2.print_employees()
manager_2.add_employee(dev_3)
print("=" * 80, " We add an employee ", "=" * 200)
manager_2.print_employees()
manager_2.remove_employee(dev_1)
print("=" * 80, " We remove an employee ", "=" * 200)
manager_2.print_employees()


# Checking if certain objects are instances of a class, and if classes are subclasses of another class;
print("=" * 65, " Check if an object is an instance of a class", "=" * 1850)
print("Is manger_1 an instance of Manager?: {}".format(isinstance(manager_1, Manager)))
print("Is manager_1 an instance of Employee?: {}".format(isinstance(manager_1, Employee)))
print("Is manager_1 an instance of Developer?: {}".format(isinstance(manager_1, Developer)))
print("Is Manager an instance of Employee?: {}".format(isinstance(Manager, Employee)))

print("=" * 65, " Check if a class is a subclass of another class", "=" * 1850)
print("Is Developer a subclass of Employee?: {}".format(issubclass(Developer, Employee)))
print("Is Manager a subclass of Employee?: {}".format(issubclass(Manager, Employee)))
print("Is Manager a subclass of Developer?: {}".format(issubclass(Manager, Developer)))
print("Is Developer a subclass of Manager?: {}".format(issubclass(Developer, Manager)))

