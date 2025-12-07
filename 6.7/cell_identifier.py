from PIL import Image

file1 = Image.open("6.7/astaxanthincells.png.png")
file2 = Image.open("6.7/hepatocytes.jpg.jpg")
file3 = Image.open("6.7/redbloodcells.jpg.jpg")
file4 = Image.open("6.7/melanocytes.jpg.jpg")
file5 = Image.open("6.7/adipocytes.jpg.jpg")
file6 = Image.open("6.7/retina.jpg.jpg")
file7 = Image.open("6.7/hemo.png.png")
file8 = Image.open("6.7/LutealCells.jpg.jpg")
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

    # ✔️ Keep YOUR original width/height code exactly unchanged
    width = files[i].width
    height = files[i].height

    pixels = files[i].load()

    for x in range(width):
        for y in range(height):
            pixel_r = pixels[x, y][0]
            pixel_g = pixels[x, y][1]
            pixel_b = pixels[x, y][2]

            cell = classify_cell(pixel_r, pixel_g, pixel_b)

            # ✔️ IF STATEMENTS UNCHANGED
            if cell == "yellow":
                yellow_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "green":
                green_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "blue":
                blue_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "red":
                red_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "black":
                black_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "purple":
                purple_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "brown":
                brown_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "yellow_orange":
                yellow_orange_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "brown_rich":
                brown_rich_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "pink":
                pink_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            if cell == "other":
                other_pixels.append(pixels[x,y])
                files[i].putpixel((x,y), (255, 255, 255))

            

   
 

