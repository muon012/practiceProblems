# Hackerrank Challenge

if __name__ == '__main__':
	# py_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
	py_students = []
	print("For this program, you will enter the name of the student followed by its grade. All values are separated by"
		" commas. The program will output all the students who have the second lowest grades.")
	for _ in range(int(input("How many students will you enter in this program? "))):
		name = input()
		score = int(input())
		student = [name, score]
		py_students.append(student)

	l = len(py_students)
	for i in range(l):
		for j in range(l - i - 1):
			if py_students[j][1] > py_students[j + 1][1]:
				py_students[j], py_students[j + 1] = py_students[j + 1], py_students[j]

	second_lowest = 0

	for k in range(l):
		if py_students[k][1] > py_students[0][1]:
			second_lowest = py_students[k][1]
			break

	second_lowest_students = []

	for student in py_students:
		if student[1] == second_lowest:
			second_lowest_students.append(student)

	for student in sorted(second_lowest_students):
		print(student[0])
