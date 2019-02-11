# Class variables

# Class variables: Variables that are shared amongst all instances of a class;
# Instance variables: Variables specific to the instance, in this example (first,last, pay, email)


class Employee:

	# We create some class variables
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
		Employee.num_of_emps += 1 # "__init__" runs every time an instance is created, so we put the change inside it.

	def full_name(self):
		return "{0.first} {0.last}".format(self)

	def apply_raise(self):
		# We keep the instance raise_amount in case we only want to target the instance only, not all the instances
		self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# Python looks for an attribute inside an instance, if it can't find it then it looks in the class for that attribute
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# The instance doesn't have the attribute "raise_amount"
print(emp_1.__dict__)
# The class DOES have the attribute "raise_amount"
print(Employee.__dict__)

print("=" * 80, "Creating an instance variable", "=" * 220)
# This example creates the attribute "raise_amount" for emp_1 instance. This is not a class variable.
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print("Number of employees: {0.num_of_emps}".format(Employee))

# This will increase the pay of emp_1 to 5%.
emp_1.apply_raise()
print(emp_1.pay)

emp_2.apply_raise()
print(emp_2.pay)


