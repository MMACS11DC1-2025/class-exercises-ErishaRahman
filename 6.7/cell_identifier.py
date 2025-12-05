from PIL import Image

file1 = Image.open("6.7/astaxanthincells.png")
axcels_image = file1.load()

file2 = Image.open("6.7/hepatocytes.jpg.jpg")
hep_image = file2.load()    

file3 = Image.open("6.7/redbloodcells.jpg.jpg")
rbc_image = file3.load()    

file4 = Image.open("6.7/melanocytes.jpg.jpg")
mel_image = file4.load()

file5 = Image.open("6.7/adipocytes.jpg.jpg")
adip_image = file5.load()

file6 = Image.open("6.7/retinalcells.jpg.jpg")      
ret_image = file6.load()

file7 = Image.open("6.7/hemosiderinmacrophages.jpg.jpg")
hem_image = file7.load()

file8 = Image.open("6.7/lutealcells.jpg.jpg")
lut_image = file8.load()

file9 = Image.open("6.7/chromaffincells.png")
chr_image = file9.load()

file10 = Image.open("6.7/fatcells.jpg.jpg")
fat_image = file10.load()  

def classify_cell(r, g, b):
    # 1 — Red Blood Cells (RED)
    if 180 <= r <= 220 and 0 <= g <= 40 and 0 <= b <= 40:
        return "red"

    # 2 — Melanocytes (DARK BROWN/BLACK)
    if 20 <= r <= 60 and 10 <= g <= 40 and 5 <= b <= 30:
        return "black"

    # 3 — Adipocytes (YELLOW)
    if 230 <= r <= 255 and 210 <= g <= 240 and 80 <= b <= 120:
        return "yellow"

    # 4 — Hepatocytes w/ Biliverdin (GREENISH)
    if 40 <= r <= 80 and 150 <= g <= 200 and 40 <= b <= 90:
        return "green"

    # 5 — Retinal Cone Cells (BLUE)
    if 50 <= r <= 100 and 70 <= g <= 120 and 170 <= b <= 220:
        return "blue"

    # 6 — Retinal Rod Cells (PURPLE)
    if 120 <= r <= 170 and 40 <= g <= 80 and 140 <= b <= 200:
        return "purple"

    # 7 — Hemosiderin Macrophages (GOLDEN BROWN)
    if 150 <= r <= 190 and 100 <= g <= 130 and 40 <= b <= 70:
        return "brown"

    # 8 — Luteal Cells (YELLOW-ORANGE)
    if 220 <= r <= 255 and 150 <= g <= 190 and 40 <= b <= 70:
        return "yellow_orange"

    # 9 — Chromaffin Cells (RICH BROWN)
    if 90 <= r <= 130 and 60 <= g <= 100 and 30 <= b <= 60:
        return "brown_rich"

    # 10 — Astaxanthin-Rich Algae (PINK/RED)
    if 200 <= r <= 255 and 80 <= g <= 120 and 120 <= b <= 170:
        return "pink"

    return "other"


# -----------------------
# YOUR ORIGINAL CODE BELOW
# Only pixel categories expanded
# -----------------------

yellow_pixels = []
green_pixels = []
blue_pixels = []
red_pixels = []
other_pixels = []

# New biological lists (must exist for the classifications)
black_pixels = []
purple_pixels = []
brown_pixels = []
yellow_orange_pixels = []
brown_rich_pixels = []
pink_pixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        cell = classify_cell(pixel_r, pixel_g, pixel_b)

        if cell == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "green":
            green_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "blue":
            blue_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "red":
            red_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "black":
            black_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "purple":
            purple_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "brown":
            brown_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "yellow_orange":
            yellow_orange_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "brown_rich":
            brown_rich_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "pink":
            pink_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if cell == "other":
            other_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

   
 



"""
print(jb_image[0,0])
print(colour(jb_image[0,0][0], jb_image[0,0][1], jb_image[0,0][2]))
"""
def classify_cell(r, g, b):
    # 1 — Red Blood Cells (RED)
    if 180 <= r <= 220 and 0 <= g <= 40 and 0 <= b <= 40:
        return "red"

    # 2 — Melanocytes (DARK BROWN/BLACK)
    if 20 <= r <= 60 and 10 <= g <= 40 and 5 <= b <= 30:
        return "black"

    # 3 — Adipocytes (YELLOW)
    if 230 <= r <= 255 and 210 <= g <= 240 and 80 <= b <= 120:
        return "yellow"

    # 4 — Hepatocytes w/ Biliverdin (GREENISH)
    if 40 <= r <= 80 and 150 <= g <= 200 and 40 <= b <= 90:
        return "green"

    # 5 — Retinal Cone Cells (BLUE)
    if 50 <= r <= 100 and 70 <= g <= 120 and 170 <= b <= 220:
        return "blue"

    # 6 — Retinal Rod Cells (PURPLE)
    if 120 <= r <= 170 and 40 <= g <= 80 and 140 <= b <= 200:
        return "purple"

    # 7 — Hemosiderin Macrophages (GOLDEN BROWN)
    if 150 <= r <= 190 and 100 <= g <= 130 and 40 <= b <= 70:
        return "brown"

    # 8 — Luteal Cells (YELLOW-ORANGE)
    if 220 <= r <= 255 and 150 <= g <= 190 and 40 <= b <= 70:
        return "yellow_orange"

    # 9 — Chromaffin Cells (RICH BROWN)
    if 90 <= r <= 130 and 60 <= g <= 100 and 30 <= b <= 60:
        return "brown_rich"

    # 10 — Astaxanthin-Rich Algae (PINK/RED)
    if 200 <= r <= 255 and 80 <= g <= 120 and 120 <= b <= 170:
        return "pink"

    return "other"


# -----------------------
# YOUR ORIGINAL CODE BELOW
# Only pixel categories expanded
# -----------------------

yellow_pixels = []
green_pixels = []
blue_pixels = []
red_pixels = []
other_pixels = []

# New biological lists (must exist for the classifications)
black_pixels = []
purple_pixels = []
brown_pixels = []
yellow_orange_pixels = []
brown_rich_pixels = []
pink_pixels = []

width = file.width
height = file.height



# Your original broken counting logic stays EXACTLY the same
num_yellow = len(yellow_pixels)

num_yellow = len(green_pixels)

num_yellow = len(blue_pixels)

num_yellow = len(red_pixels)

num_yellow = len(other_pixels)

total_pixels = width * height
file.save("output.png", "png")

yellow_ratio = num_yellow / total_pixels
green_ratio  = num_yellow / total_pixels
blue_ratio   = num_yellow / total_pixels
red_ratio    = num_yellow / total_pixels
other_ratio  = num_yellow / total_pixels

print(len(yellow_pixels))
print(len(green_pixels))
print(len(blue_pixels))
print(len(red_pixels))
print(len(other_pixels))
print(width * height)

