from .models import Student, Worksheet, History
from . import parse_image
import datetime

def check_solutions(student, attempts):
	wksheet = Worksheet.objects.get(student=student)
	solutions = wksheet.solutions.split(',')
	levels = wksheet.levels.split(',')
	categories = wksheet.categories.split(',')
	performances = [0]*4
	cnt = 0
	for solution, attempt, level, category in zip(solutions, attempts, levels, categories):
		correct = solution == attempt
		# 1 point for EASY, 2 points for MEDIUM, 3 points for HARD
		points = int(level) + 1 if correct else -(int(level) + 1)
		performances[int(category)] += points
		# count number of correct problems
		if correct:
			cnt += 1
	add, sub, mul, div = performances
	# create History instance and update current skills
	History.objects.create(student=student, performed_add=add, performed_sub=sub, performed_mul=mul, performed_div=div, date=datetime.datetime.now())
	Student.objects.filter(name=student.name).update(skill_add=student.skill_add+add,skill_sub=student.skill_sub+sub, skill_mul=student.skill_mul+mul, skill_div=student.skill_div+div)
	# return (string of grade, list of performances for each category)
	return (str(cnt) + '/' + str(len(solutions)), performances)


def grade_file(filename):
	name = filename.split('/')[-1]
	name = name.split('.')[0] # cut off the .png
	print(name)
	student = Student.objects.get(name=name)
	attempts = parse_image.parse_image(filename)
	return check_solutions(student, attempts)

def grade_all(filenames):
	return [grade_file(filename) for filename in filenames]