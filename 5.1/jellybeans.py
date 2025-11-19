from PIL import Image
def colour(r, g, b):
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return ("yellow")

jbean = Image.open("5.1/jelly_beans.jpg").load()

 
image_output = Image.open("5.1/jelly_beans.jpg")

width = image_output.width
height = image_output.height

for x in range(width):
    for y in range(height):
        r_ = jbean[x, y][0]
        g_ = jbean[x, y][1]
        b_ = jbean[x, y][2]

        if colour(r_, g_, b_) == "yellow":
            image_output.putpixel((x,y), (255, 255, 255))

image_output.save("output1.png", "png")