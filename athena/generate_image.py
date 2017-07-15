from PIL import Image, ImageFont, ImageDraw
from django.contrib.staticfiles.templatetags.staticfiles import static
import os

STATIC_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

WIDTH, HEIGHT = 612, 792
#im = Image.new('RGB', (WIDTH, HEIGHT), 'white')


FONT_SIZE = 24
font = ImageFont.truetype('Arial.ttf', FONT_SIZE)
large_font = ImageFont.truetype('Arial.ttf', int(FONT_SIZE*1.8))

ROWS = 3
def make_homework(name, problems):
	im = Image.open(STATIC_DIRECTORY + '/athena/img/template.png')
	draw = ImageDraw.Draw(im)
	draw.text((WIDTH*.12, HEIGHT*.06), name, (0,0,0), large_font)
	for num, problem in enumerate(list(problems[0])):
		x,y = num%ROWS, num//ROWS
		#x_pixel = WIDTH*(.206+.255*x) - (FONT_SIZE*len(problem)/2*1.04)
		#y_pixel = HEIGHT*(.175+.1385*y)
		x_pixel = WIDTH*(.25 + .25*x) - (FONT_SIZE*len(problem)/2*.5)
		y_pixel = HEIGHT*(.15 + .1548*y)
		if y == 0:
			y_pixel += HEIGHT * 0.003
		draw.text((x_pixel, y_pixel), problem, (0,0,0), font=font)
	#im.show()
	im.save(name.replace(' ','')+'.png')

#problems = ['5+2', '55+2', '55+22']*5
#make_homework('Lulu', problems)