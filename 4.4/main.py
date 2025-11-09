# ‧₊˚❀༉‧₊˚flower recursions˚₊‧༉❀˚₊‧

#overview: draws a flower as a recursive swirl with a stem, and leaves.
#recursion: the function "swirl(size)" takes one from size each call, forming a spiral until size is 0.
#run: enter size (min 20), FireBoy/WaterGirl, and lighter/darker stem.

#tests:
  # input test 1: enter 20, "FireBoy", enter "lighter" ==> 
    #smallest red flower, light brown stem, green leaves
    
  # input test 2: enter 70, "WaterGirl", enter "darker" ==> 
    #medium blue flower, black stem, green leaves
    
  # input test 3: enter 100, "FireBoy", enter "lighter" ==> 
    #very large red flower, light brown stem, green leaves
    
  # input test 4: enter 80, "watergirl", enter "darker" ==> 
    #large blue flower, black stem, green leaves 
    
  # input test 5: enter a number <=0
    #the program returns

#20 is the minimun since that number creates the smallest swirl possible
  #the true minimum is 1, since thats the lowest you can go before the
  #code doesnt run, though it will be difficult to view
  #there is no actual maximun, unless the program crashes, since you can
  #enlarge the screen to different sizes on different devices
  #(though i reccomend not going over 150)
#fixes: color key bug, angle tweaks, smoother swirl.

#imports/setting up
import turtle
tool = turtle.Turtle()

#user inputs for graphics
num = input("how big woud you like your flower? The minimun is 20.")


      
character = input("FireBoy or WaterGirl").lower().strip()
stemcolor = input("Would you like your stem lighter or darker?").lower().strip()

numb = int(num)

#color dictionary
colors = {"fireboy":"#FF0000", "watergirl":"#0000FF", "darker":"#000000",
          "lighter":"#967969", "leaves":"#008900"}
#stem code
def branch(size):
    if size <= 0: #base case
      return
    else:
      tool.color(colors[stemcolor])
      tool.pendown()  
      tool.setheading(270)  #fancy way of angles and degrees (i got this
      #from vic my friend thank you vic your method is great)
      tool.forward(numb*1.35) #go down
      
      #used (numb), not numbers, so the flower could look the same at
      #any size
      
      tool.color(colors["leaves"])
      tool.setheading(45)
      tool.forward(numb/2)  
      tool.setheading(15)  
      tool.forward(numb/2)  
      tool.setheading(250)  
      tool.forward(numb/2)  
      tool.setheading(180)  
      tool.forward(numb*1.35/2) #leaf 1 
      #rotating and turning to make a diamond shaped leaf
      
      #i was having difficulties with the turn left/right commands,
      #and numbers (setheading) help the code turn in a a specific direction
      
      tool.color(colors[stemcolor])
      tool.setheading(270)  # change the degress
      tool.forward(numb*0.25)  #go down
      
      tool.color(colors["leaves"])
      tool.setheading(180)
      tool.forward(numb/2) 
      tool.setheading(250)  
      tool.forward(numb/2) 
      tool.setheading(15)  
      tool.forward(numb/2)  
      tool.setheading(60)  
      tool.forward(numb*0.75/2)  #second leaf
      
      tool.color(colors[stemcolor])
      tool.setheading(270)  # change the degrees
      tool.forward(numb*1.2)  # move down and finish the stem
      tool.stamp()

def swirl(size):
    if size == 0: #base case
      return
    else:
      tool.color(colors[character]) # the swirl flower part
      tool.speed(90)
      tool.forward(2+size/4)
      tool.left(30-size/12)
      swirl(size - 1) #what leads to the base case
      #increases the distance and decreases the rotation 
      #to properly execute drawing the swirl
      #(i found this idea online)
      

#the actual execution of the code
tool.pendown()
swirl(numb)
branch(numb)
