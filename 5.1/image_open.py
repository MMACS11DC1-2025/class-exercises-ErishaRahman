from PIL import Image
import coolcolours

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()
"""
def colour(r, g, b):
    if r <= 24 and g >= 230 and b <= 24:
        return ("green")
    if r <= 24 and g <= 24 and b >= 230:
        return ("blue")
    if r >= 230 and g <= 24 and b <= 24:
        return ("red")


print(colour(r + g + b))   #green
print(colour(0, 0, 255))   #blue
print(colour(255, 0, 0))   #red   
"""

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for x in range(width):
    for y in range(height):
        r = image_green[x, y][0]
        g = image_green[x, y][1]
        b = image_green[x, y][2]

if coolcolours.colour(r, g, b):
    beach_colour = image_beach[x, y]
    image_output.putpixel((x, y), beach_colour)

image_output.save("output.png", "png")