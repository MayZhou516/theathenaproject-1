from PIL import Image, ImageFont, ImageDraw


WIDTH, HEIGHT = 850, 1100
#im = Image.new('RGB', (WIDTH, HEIGHT), 'white')
im = Image.open('homework_template/Slide1.png')
draw = ImageDraw.Draw(im)
FONT_SIZE = 26
font = ImageFont.truetype('Arial.ttf', FONT_SIZE)
large_font = ImageFont.truetype('Arial.ttf', int(FONT_SIZE*1.8))

ROWS = 3
#problems = ['5+2=']*15
def make_homework(name, problems):
	draw.text((WIDTH*.1, HEIGHT*.05), name, (0,0,0), large_font)
	for num, problem in enumerate(problems):
		x,y = num%ROWS, num//ROWS
		x_pixel = WIDTH*(.206+.255*x) - (FONT_SIZE*len(problem)/2*1.04)
		y_pixel = HEIGHT*(.175+.1385*y)
		draw.text((x_pixel, y_pixel), problem, (0,0,0), font=font)
	im.show()

