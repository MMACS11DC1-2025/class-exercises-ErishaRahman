from PIL import Image
def colour(r, g, b):
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return "yellow"

jbean = Image.open("5.1/jelly_beans.jpg").load()

image_output = Image.open("5.1/jelly_beans.jpg")

width = image_output.width
height = image_output.height

foundYellow = -1
for x in range(width):
    for y in range(height):
        r_ = jbean[x, y][0]
        g_ = jbean[x, y][1]
        b_ = jbean[x, y][2]

        if colour(r_, g_, b_) == "yellow":
            print("yellow pixel")
            print(r_, g_, b_ )
            foundYellow = 0
            image_output.putpixel((x,y), (255, 255, 255))
        else:
            if 0 <= foundYellow <= 100:
                foundYellow += 1
                print(r_, g_, b_ )

image_output.save("output1.png", "png")