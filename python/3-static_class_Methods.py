# Class Methods: Methods that use the argument "cls" (class). They're dependent on the class;
# Regular Methods: Methods that use the "self" argument. They're dependent on the instance;
# Static Methods: Methods that use neither the "cls" or "self" arguments.
#             These methods are independent of both classes and instances but have some logical connection to the class;


class Employee:

	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
		Employee.num_of_emps += 1

	def full_name(self):
		return "{0.first} {0.last}".format(self)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# We create a class method using the decorator "@classmethod" and passing first the "cls" argument;
	# Here, you are working with the class instead of the instance;
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	# Using a class method as constructors;
	# You can use them as a way to create objects.
	@classmethod
	def from_string(cls, string_emp):
		first, last, pay = string_emp.split("-")
		return cls(first, last, pay)

	# We create a static method;
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


import datetime

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# We use the class method to change the class variable "raise_amount";
Employee.set_raise_amount(1.05)

print("=" * 80, " After the class method ", "=" * 200)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# We will use these strings for the constructor defined as a class method above;
str_emp_1 = "John-Doe-70000"
str_emp_2 = "Steve-Smith-30000"
str_emp_3 = "Jane-Doe-90000"

# We create new instances with the constructor in the class.
new_emp_1 = Employee.from_string(str_emp_1)
new_emp_2 = Employee.from_string(str_emp_2)
new_emp_3 = Employee.from_string(str_emp_3)

print("=" * 80, " Using a class method as a constructor ", "=" * 200)
print(new_emp_1.email)
print(new_emp_2.email)
print(new_emp_3.email)

print("=" * 80, " Check if a day is a workday ", "=" * 200)
my_date = datetime.date(2018, 11, 9)
print("Is 1989-9-15 a workday? ", Employee.is_workday(my_date))


today_date = datetime.datetime.today()
print("Is today a workday? ", Employee.is_workday(today_date))
