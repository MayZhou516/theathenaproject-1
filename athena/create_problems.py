from .models import Student, History, Worksheet
from . import generate_image
import random

EASY, MEDIUM, HARD = 0, 1, 2
ADD, SUB, MUL, DIV = 0, 1, 2, 3
OPS = '+-*/'

def createWorksheets():
	all_students = Student.objects.all()
	for student in all_students:
		# gets list of generated problems
		problems = getProblems(student)
		# sends to worksheet image generator
		generate_image.make_homework(student.name, problems)

def getProblems(student):
	skills = [student.skill_add, student.skill_sub, student.skill_mul, student.skill_div]
	best = skills.index(max(skills))

	# 3 problems for best category, 4 for rest
	problems = []
	for i in range(4):
		if i == best:
			for j in range(3):
				problems.append(getProblemBySkill(best, skills[best]))
		else:
			for j in range(4):
				problems.append(getProblemBySkill(i, skills[i]))

	# get levels, solutions, and categories from list of problems and save
	lists = list(zip(*problems))
	database_values = lists[1:]
	csvs = [','.join(str(value) for value in values) for values in database_values]
	Worksheet.objects.create(student=student, solutions=csvs[0], categories=csvs[1], levels=csvs[2])
	# send list of problems only back
	return lists[:1]

# randomly generate level of problem based on current skill
def getProblemBySkill(category, skill):
	if skill <= 20:
		return getProblem(category, EASY)
	elif skill <= 25:
		return getProblem(category, EASY) if random.random() < 0.66 else getProblem(category, MEDIUM)
	elif skill <= 30:
		return getProblem(category, EASY) if random.random() < 0.5 else getProblem(category, MEDIUM)
	elif skill <= 40:
		return getProblem(category, EASY) if random.random() < 0.33 else getProblem(category, MEDIUM)
	elif skill <= 45:
		return getProblem(category, MEDIUM)
	elif skill <= 65:
		return getProblem(category, MEDIUM) if random.random() < 0.66 else getProblem(category, HARD)
	elif skill <= 75:
		return getProblem(category, MEDIUM) if random.random() < 0.5 else getProblem(category, HARD)
	elif skill <= 80:
		return getProblem(category, MEDIUM) if random.random() < 0.33 else getProblem(category, HARD)
	else:
		return getProblem(category, HARD)

def getProblem(category, level):
	num1 = random.randint(1, 9) if level != HARD else random.randint(10, 99)
	num2 = random.randint(1, 9) if level == EASY else random.randint(10, 99)
	if category == ADD:
		solution = num1 + num2
	elif category == SUB:
		if num1 < num2:
			num1, num2 = num2, num1
		solution = num1 - num2
	elif category == MUL:
		solution = num1 * num2
	else:
		solution = num1
		num1 = num1 * num2
	return (str(num1) + OPS[category] + str(num2) + '=', solution, category, level)

print('Doing stuff')
createWorksheets()

	