from PIL import Image

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
#green
#yellow
#llight brown shades??? (184, 137, 35)(140, 78, 3)
#dark brown shades (94, 55, 17) (141, 92, 36)
#darkest brown shades (71, 54, 48) (40, 26, 19)
#black shades (35, 31, 32) (0, 0, 0)

def ripe_checker(r, g, b):
    # White (Background - high values for all R, G, B)
    if r > 240 and g > 240 and b > 240:
        return "white"

    # Green (Unripe/Tinge)
    if g > r + 20 and g > b + 20 and g > 100:
        return "green"

    # Yellow (Ripe)
    if r > 180 and g > 180 and b < 120:
        return "yellow"

    # Light Brown (Expanded significantly)
    if r > g > b and r >= 150 and g >= 100 and b >= 50:
        return "light_brown"

    # Brown (Expanded significantly)
    if r > g > b and r >= 90 and g >= 60 and b >= 30:
        return "brown"

    # Dark Brown/Black spots (Expanded significantly)
    if r < 80 and g < 80 and b < 80:
        return "black"

    return "other"


for i in range(len(filesb)):
    '''
    pix = files[i].load()
    '''
    white_pixels = []
    green_pixels = []
    yellow_pixels = []
    green_pixels = []
    light_brown_pixels = []
    brown_pixels = []
    dark_brown_pixels = []
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
            
            if cell == "light_brown":
                light_brown_pixels.append(files[i].getpixel((x, y)))

            if cell == "brown":
                brown_pixels.append(files[i].getpixel((x, y)))

            if cell == "dark_brown":
                dark_brown_pixels.append(files[i].getpixel((x, y)))
            
            if cell == "black":
                black_pixels.append(files[i].getpixel((x, y)))
   
            
        #rid of white cells input that or smth
    num_white = len(white_pixels)

    num_green = len(green_pixels)

    num_yellow = len(yellow_pixels)

    num_light_brown = len(light_brown_pixels)

    num_brown = len(brown_pixels)

    num_dark_brown = len(dark_brown_pixels)

    num_black = len(black_pixels)

    total_pixels_banana = (width*height) - num_white

    concentration_green = num_green / total_pixels_banana

    concentration_yellow = num_yellow / total_pixels_banana

    concentration_light_brown = num_light_brown / total_pixels_banana

    concentration_brown = num_brown / total_pixels_banana

    concentration_dark_brown = num_dark_brown / total_pixels_banana

    concentration_black = num_black / total_pixels_banana
    print(files [i].filename)
    print("{:.3f}%".format(concentration_green * 100))
    print("{:.3f}%".format(concentration_yellow * 100))
    print("{:.3f}%".format(concentration_light_brown * 100))
    print("{:.3f}%".format(concentration_brown * 100))
    print("{:.3f}%".format(concentration_dark_brown * 100))
    print("{:.3f}%".format(concentration_black * 100))

            

            

   
 

