# Banana Ripeness Checker
# This program analyzes images of bananas to determine their ripeness based on color
#This will be donw by analyzing the pixel colors in the images
# Blind bakers can use this to sort and find bananas of certain ripeness
#Ripeness can be represented in various concentrations with four main colors
# Green - unripe
# Yellow - ripe
# Brown - overripe
# Black - very unripe


from PIL import Image
import time

#open the image files
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

#list for easy access(for loops)
files = [file1, file2, file3, file4, file5, file6, file7, file8, file9, file10]

#load them for the attributes
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

# another for loop list
filesb = [fileb1, fileb2, fileb3, fileb4, fileb5, fileb6, fileb7, fileb8, fileb9, fileb10]

#lists that will be used for seletion sort and binary search (later!!)
veryunripe = []
unripe = []
ripe = []
overripe = []

#The function that identifies the color of the pixel
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
#start time here cause this is actual running of the code
start_time = time.time()

#loops the pixel checking proccess 10 times for each image to maximize efficiency
for i in range(len(filesb)):
    #all lists start empty each loop so they dont carry over values
    white_pixels = []
    green_pixels = []
    yellow_pixels = []
    green_pixels = []
    brown_pixels = []
    black_pixels = []

    #attributes 
    width = files[i].width
    height = files[i].height


    #start of actual pixel checking
    for x in range(width):
        for y in range(height):
            pixel_tuple = filesb[i][x, y]
            pixel_r = pixel_tuple[0]
            pixel_g = pixel_tuple[1]
            pixel_b = pixel_tuple[2]
            cell = ripe_checker(pixel_r, pixel_g, pixel_b)
            
            #append to the correct list based on color
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

   #calculations to determine percentages of each color
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

    #append the results to the correct ripeness list as a perecent string and the filename
    veryunripe.append([("{:.3f}%".format(concentration_black * 100)), files [i].filename])
    unripe.append([("{:.3f}%".format(concentration_green * 100)), files [i].filename])
    ripe.append([("{:.3f}%".format(concentration_yellow * 100)), files [i].filename])
    overripe.append([("{:.3f}%".format(concentration_brown * 100)), files [i].filename])

ripeness = [veryunripe, unripe, ripe, overripe]
#sort my beauttiful list
for i in range(len(ripeness)):
    max_index = i
    for j in range(i + 1, len(ripeness)):
        if ripeness[j][0] > ripeness[max_index][0]:
            max_index = j
    ripeness[i], ripeness[max_index] = ripeness[max_index], ripeness[i]

#prints first five values of each ripeness list
print("for very unripe: " + str((ripeness[0])[:4]))
print("for unripe: " + str((ripeness[1])[:4]))
print("for ripe: " + str((ripeness[2])[:4]))
print("for overripe: " + str((ripeness[3])[:4]))

#binary search that seraches for a percent value and returns the image name
def find_image(list_name, percent):
    left = 0
    right = len(list_name) - 1
    while left <= right:
        mid = int((left + right) // 2)
        value = float(list_name[mid][0][:-1])

        if value == percent:
            return list_name[mid][1]
        elif value > percent: 
            right = mid - 1
        else:
            left = mid + 1
    return "none"

print(ripeness[0])
print(find_image(ripeness[0], 6.547))

end_time = time.time()
print("Program run time: {:.3f} seconds".format(end_time - start_time))


            

            

   
 

