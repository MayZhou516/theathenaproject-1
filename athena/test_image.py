from PIL import Image, ImageFont, ImageDraw

im = Image.new('RGB', (850, 1100), 'white')
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('Arial.ttf', 16)
draw.text((10,10), 'Hello World!', (0,0,0), font=font)
im.show()

