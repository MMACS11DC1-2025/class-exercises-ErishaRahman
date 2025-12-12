from PIL import Image

file1 = Image.open("6.7/astaxanthin.png.png")
file2 = Image.open("6.7/hepatocytes.jpg.jpg")
file3 = Image.open("6.7/redbloodcells.jpg.jpg")
file4 = Image.open("6.7/melanocyte.jpg.jpg")
file5 = Image.open("6.7/RetinalRodCells.jpg.jpg")
file6 = Image.open("6.7/retina.jpg.jpg")
file7 = Image.open("6.7/hemo.png.png")
file8 = Image.open("6.7/LutealCells.jpg")
file9 = Image.open("6.7/chromaffin.png")
file10 = Image.open("6.7/fatcells.jpg.jpg")

files = [file1, file2, file3, file4, file5, file6, file7, file8, file9, file10]

def classify_cell(r, g, b):
    if 180 <= r <= 220 and 0 <= g <= 40 and 0 <= b <= 40:
        return "red"
    if 20 <= r <= 60 and 10 <= g <= 40 and 5 <= b <= 30:
        return "black"
    if 230 <= r <= 255 and 210 <= g <= 240 and 80 <= b <= 120:
        return "yellow"
    if 40 <= r <= 80 and 150 <= g <= 200 and 40 <= b <= 90:
        return "green"
    if 50 <= r <= 100 and 70 <= g <= 120 and 170 <= b <= 220:
        return "blue"
    if 120 <= r <= 170 and 40 <= g <= 80 and 140 <= b <= 200:
        return "purple"
    if 150 <= r <= 190 and 100 <= g <= 130 and 40 <= b <= 70:
        return "brown"
    if 220 <= r <= 255 and 150 <= g <= 190 and 40 <= b <= 70:
        return "yellow_orange"
    if 90 <= r <= 130 and 60 <= g <= 100 and 30 <= b <= 60:
        return "brown_rich"
    if 200 <= r <= 255 and 80 <= g <= 120 and 120 <= b <= 170:
        return "pink"
    return "other"


for i in range(10):
    '''
    pix = files[i].load()
    '''
    yellow_pixels = []
    green_pixels = []
    blue_pixels = []
    red_pixels = []
    other_pixels = []
    black_pixels = []
    purple_pixels = []
    brown_pixels = []
    yellow_orange_pixels = []
    brown_rich_pixels = []
    pink_pixels = []
    width = files[i].width
    height = files[i].height

    

    for x in range(width):
        for y in range(height):
            pixel_r = files[i].getpixel((x, y))[0]
            pixel_g = files[i].getpixel((x, y))[1]
            pixel_b = files[i].getpixel((x, y))[2]

            cell = classify_cell(pixel_r, pixel_g, pixel_b)

         
            if cell == "yellow":
                yellow_pixels.append(files[i].getpixel((x, y)))
             

            if cell == "green":
                green_pixels.append(files[i].getpixel((x, y)))
            

            if cell == "blue":
                blue_pixels.append(files[i].getpixel((x, y)))
            

            if cell == "red":
                red_pixels.append(files[i].getpixel((x, y)))
            

            if cell == "black":
                black_pixels.append(files[i].getpixel((x, y)))
            

            if cell == "purple":
                purple_pixels.append(files[i].getpixel((x, y)))
           

            if cell == "brown":
                brown_pixels.append(files[i].getpixel((x, y)))
           

            if cell == "yellow_orange":
                yellow_orange_pixels.append(files[i].getpixel((x, y)))
              

            if cell == "brown_rich":
                brown_rich_pixels.append(files[i].getpixel((x, y)))
              

            if cell == "pink":
                pink_pixels.append(files[i].getpixel((x, y)))
            
#rid of white cells input that or smth
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
            

            

   
 

