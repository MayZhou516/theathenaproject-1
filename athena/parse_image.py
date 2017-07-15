from PIL import Image
import pytesseract
import performRecognition
import numpy as np
import time

NUM_PROBLEMS = 15
ROWS = 3
WIDTH, HEIGHT = 612, 792
BOX_WIDTH, BOX_HEIGHT = 80, 38  # I dunno lol


def parse_attempt(im, num):
	x,y = num%ROWS, num//ROWS
	#x_pixel = WIDTH*(.20+.3*x)
	#y_pixel = HEIGHT*(.271+.159*y)
	x_pixel = WIDTH*(.25 + .25*x)
	y_pixel = HEIGHT*(.2272 + .1548*y)
	if y == 0:
		y_pixel += HEIGHT * 0.003

	sub = im.crop((x_pixel-BOX_WIDTH/2, y_pixel-BOX_HEIGHT/2, x_pixel+BOX_WIDTH/2, y_pixel+BOX_HEIGHT/2))
	#sub.show()
	#if num == 2:
	#	sub.save('three.png')
	#text = pytesseract.image_to_string(sub)
	text = performRecognition.readNum(np.array(sub))
	#print(text)
	return text.strip()


def parse_image(filename):
	im = Image.open(filename)
	return [parse_attempt(im, num) for num in range(NUM_PROBLEMS)]

print(parse_image('template_done.png'))
#print('<'+pytesseract.image_to_string(Image.open('three.png'))+'>')
