# Property Decorator: Allows you to define a method but use it as an attribute. You can call the method by calling it
# 					  as an attribute. Syntax is "@property";
# Setter Decorator: Allows you to set attributes using properties. Use the name of the property that you want to
# 					change followed by ".setter" and then write the setter method with that same property's
# 					name i.e. "@method.setter";
# Deleter Decorator: This will delete the values of any attributes. You can set the new values to " " or None or any
# 					 other value that you want to use. In oder to call the deleter and it's respective deleter method
# 					 you use ... "del instance.full_name". Make sure the deleter is named after an attribute or
# 					 property that you have made;

class Employee:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	# We erased the email attribute in the  "__init__" method and made it into an attribute;
	@property
	def email(self):
		return "{0.first}.{0.last}@company.com".format(self)

	# We changed the "full_name" method into an attribute;
	@property
	def full_name(self):
		return "{0.first} {0.last}".format(self)

	@full_name.setter
	def full_name(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@full_name.deleter
	def full_name(self):
		self.first = None
		self.last = None
		print("Deleted name!")


emp_1 = Employee("John", "Smith", 50000)

emp_1.first = "Jim"

# If you were to print the object's first name, it would show up as "Jim" but the email would show "John". This is
# because when the object was created, the email attribute used the initial argument. We deleted that email
# attribute and used a property decorator to be able to use the new first name in the email without breaking the code
# for all the instances;
print("=" * 40, "Property Decorator", "=" * 60)
print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name) # Because "full_name" is now an attribute, we don't need to call it as a function;


# The setter will set the first and last name equal to these values and then the other methods will use these NEW
# values as their attributes;
emp_1.full_name = "Corey Schafer"

print("=" * 40, "Setter Decorator", "=" * 60)
print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

# The deleter will act as a clean up code that wants to delete certain attributes;
print("=" * 40, "Deleter Decorator", "=" * 60)
del emp_1.full_name
print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)



