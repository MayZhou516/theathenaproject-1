from PIL import Image
import pytesseract

NUM_PROBLEMS = 3
ROWS = 3
WIDTH, HEIGHT = 720, 960
BOX_WIDTH, BOX_HEIGHT = 30, 33 # I dunno lol


def parse_attempt(im, num):
	x,y = num%ROWS, num//ROWS
	x_pixel = WIDTH*(.206+.29*x)
	y_pixel = HEIGHT*(.271+.1387*y)
	print(num, x_pixel, y_pixel)
	sub = im.crop((x_pixel-BOX_WIDTH/2, y_pixel-BOX_HEIGHT/2, x_pixel+BOX_WIDTH/2, y_pixel+BOX_HEIGHT/2))
	sub.show()
	if num == 2:
		sub.save('three.png')
	text = pytesseract.image_to_string(sub)
	return text.strip()


def parse_image(filename):
	im = Image.open(filename)
	return [parse_attempt(im, num) for num in range(NUM_PROBLEMS)]

print(parse_image('lulu_done.png'))
print('<'+pytesseract.image_to_string(Image.open('three.png'))+'>')
