from PIL import Image
import numpy as np
import time
from . import performRecognition
from .models import Student, Worksheet

NUM_PROBLEMS = 15
ROWS = 3
WIDTH, HEIGHT = 612, 792
BOX_WIDTH, BOX_HEIGHT = 80, 38 

def parse_attempt(im, num):
	x,y = num%ROWS, num//ROWS
	x_pixel = WIDTH*(.25 + .25*x)
	y_pixel = HEIGHT*(.2272 + .1548*y)
	if y == 0:
		y_pixel += HEIGHT * 0.003

	sub = im.crop((x_pixel-BOX_WIDTH/2, y_pixel-BOX_HEIGHT/2, x_pixel+BOX_WIDTH/2, y_pixel+BOX_HEIGHT/2))
	text = performRecognition.readNum(np.array(sub))
	return text.strip()


def parse_image(filename):
	im = Image.open(filename)
	return [parse_attempt(im, num) for num in range(NUM_PROBLEMS)]

def grade_image(filename):
	name = filename[-4] # cut off the .png
	student = Student.objects.get(name=name)
	Worksheet = Worksheet.objects.get(student=student)
	attempts = parse_image(filename)

#im = cv2.imread("static/athena/Samantha Jones.png")
#print(parse_image("static/athena/Samantha Jones.png"))
