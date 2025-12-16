from PIL import Image
import time

file1 = Image.open("6.7/banana1.PNG")
file2 = Image.open("6.7/banana2.PNG")
file3 = Image.open("6.7/banana3.PNG")
file4 = Image.open("6.7/banana4.PNG")
file5 = Image.open("6.7/banana5.PNG")
file6 = Image.open("6.7/banana6.PNG")
file7 = Image.open("6.7/banana7.PNG")
file8 = Image.open("6.7/banana8.PNG")
file9 = Image.open("6.7/banana9.PNG")
file10 = Image.open("6.7/banana10.PNG")
files = [file1, file2, file3, file4, file5, file6, file7, file8, file9, file10]

fileb1 = file1.load()
fileb2 = file2.load()
fileb3 = file3.load()
fileb4 = file4.load()
fileb5 = file5.load()
fileb6 = file6.load()
fileb7 = file7.load()
fileb8 = file8.load()
fileb9 = file9.load()
fileb10 = file10.load()
filesb = [fileb1, fileb2, fileb3, fileb4, fileb5, fileb6, fileb7, fileb8, fileb9, fileb10]
veryunripe = []
unripe = []
ripe = []
overripe = []
def ripe_checker(r, g, b):
    if r > 235 and g > 235 and b > 235:
        return "white"

    if g > r + 10 and g > b + 10 and g > 60:
        return "green"

    if r > 170 and g > 170 and b < 150:
        return "yellow"
    
    if (
        r > g and g >= b and
        r >= 130 and g >= 90 and b >= 40
    ):
        return "brown"

    if r < 120 and g < 120 and b < 120:
        return "black"

    return "other"
start_time = time.time()

for i in range(len(filesb)):
    white_pixels = []
    green_pixels = []
    yellow_pixels = []
    green_pixels = []
    brown_pixels = []
    black_pixels = []
    width = files[i].width
    height = files[i].height

    for x in range(width):
        for y in range(height):
            pixel_tuple = filesb[i][x, y]
            pixel_r = pixel_tuple[0]
            pixel_g = pixel_tuple[1]
            pixel_b = pixel_tuple[2]
            cell = ripe_checker(pixel_r, pixel_g, pixel_b)

            if cell == "white":
                white_pixels.append(files[i].getpixel((x, y)))

            if cell == "green":
                green_pixels.append(files[i].getpixel((x, y)))

            if cell == "yellow":
                yellow_pixels.append(files[i].getpixel((x, y)))
        
            if cell == "brown":
                brown_pixels.append(files[i].getpixel((x, y)))

            if cell == "black":
                black_pixels.append(files[i].getpixel((x, y)))
   
    num_white = len(white_pixels)
    num_green = len(green_pixels)
    num_yellow = len(yellow_pixels)
    num_brown = len(brown_pixels)
    num_black = len(black_pixels)

    total_pixels_banana = (width*height) - num_white
    concentration_green = num_green / total_pixels_banana
    concentration_yellow = num_yellow / total_pixels_banana
    concentration_brown = num_brown / total_pixels_banana
    concentration_black = num_black / total_pixels_banana

    print(files [i].filename)
    print("{:.3f}%".format(concentration_green * 100))
    print("{:.3f}%".format(concentration_yellow * 100))
    print("{:.3f}%".format(concentration_brown * 100))
    print("{:.3f}%".format(concentration_black * 100))

    veryunripe.append([("{:.3f}%".format(concentration_black * 100)), files [i].filename])
    unripe.append([("{:.3f}%".format(concentration_green * 100)), files [i].filename])
    ripe.append([("{:.3f}%".format(concentration_yellow * 100)), files [i].filename])
    overripe.append([("{:.3f}%".format(concentration_brown * 100)), files [i].filename])

ripeness = [veryunripe, unripe, ripe, overripe]
for i in range(len(ripeness)):

    min_index = i
    for j in range(i+1, len(ripeness)):
        if ripeness[j][0] < ripeness[min_index][0]:
            min_index = j
    ripeness[i], ripeness[min_index] = ripeness[min_index], ripeness[i]

print(ripeness)

end_time = time.time()
print("Program run time: {:.2f} seconds".format(end_time - start_time))


            

            

   
 

