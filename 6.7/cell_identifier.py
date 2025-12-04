from PIL import Image

def colour(r, g, b):
    if r < 25 and r >= 0 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return "green"
    
    if r < 25 and r >= 0 and g < 25 and g >= 0 and b > 230 and b <= 255:
        return "blue"
    
    if r > 230 and r <= 255 and g < 25 and g >= 0 and b < 25 and b >= 0:
        return "red"
    
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b > 230 and b <= 255:
        return "white"
    
    if r < 25 and r >= 0 and g < 25 and g >= 0 and b < 25 and b >= 0:
        return "black"
    
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return "yellow"
    
    if r > 230 and r <= 255 and g < 25 and g >= 0 and b > 230 and b <= 255:
        return "magenta"
    else:
        return "other"
   
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()
"""
print(jb_image[0,0])
print(colour(jb_image[0,0][0], jb_image[0,0][1], jb_image[0,0][2]))
"""
yellow_pixels = []
green_pixels = []
blue_pixels = []
red_pixels = []
other_pixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "green":
            green_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "blue":
            blue_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "red":
            red_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "other":
            other_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

num_yellow = len(yellow_pixels)

num_yellow = len(green_pixels)

num_yellow = len(blue_pixels)

num_yellow = len(red_pixels)

num_yellow = len(other_pixels)

total_pixels = width*height
file.save("output.png", "png")

yellow_ratio = num_yellow / total_pixels

green_ratio = num_yellow / total_pixels

blue_ratio = num_yellow / total_pixels

red_ratio = num_yellow / total_pixels

other_ratio = num_yellow / total_pixels

print(len(yellow_pixels))
print(len(green_pixels))
print(len(blue_pixels))
print(len(red_pixels))
print(len(other_pixels))
print(width*height)

