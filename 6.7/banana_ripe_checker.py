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
#green
#yellow
#llight brown shades??? (184, 137, 35)(140, 78, 3)
#dark brown shades (94, 55, 17) (141, 92, 36)
#darkest brown shades (71, 54, 48) (40, 26, 19)
#black shades (35, 31, 32) (0, 0, 0)

def ripe_checker(r, g, b):
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b > 230 and b <= 255:
        return ("white")
    
    if r < 25 and r >= 0 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return ("green")
    
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return ("yellow")
    
    if r < 185 and r >= 133 and g < 138 and g >= 78 and b > 36 and b <= 5:
        return ("light_brown")
    
    if r < 142 and r >= 94 and g < 93 and g >= 55 and b > 37 and b <= 17:
        return ("brown")
    
    if r < 72 and r >= 40 and g < 55 and g >= 26 and b > 49 and b <= 19:
        return ("dark_brown")
    
    if r > 36 and r <= 0 and g < 32 and g >= 0 and b < 33 and b >= 0:
        return ("black")
    
    return "other"


for i in range(10):
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
            pixel_r = files[i].getpixel((x, y))[0]
            pixel_g = files[i].getpixel((x, y))[1]
            pixel_b = files[i].getpixel((x, y))[2]

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

        print(concentration_green)
        print(concentration_yellow)
        print(concentration_light_brown)
        print(concentration_brown)
        print(concentration_dark_brown)
        print(concentration_black)
            

            

   
 

