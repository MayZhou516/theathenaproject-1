from django.shortcuts import render
import random

EASY, MEDIUM, HARD = 1, 2, 3
ADD, SUB, MUL, DIV = 1, 2, 3, 4
OPS = '+-*/'

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
	return (str(num1) + OPS[category-1] + str(num2) + '=', solution)
