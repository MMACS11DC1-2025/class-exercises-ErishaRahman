#imports/setting up
import turtle
tool = turtle.Turtle()

#user inputs for graphics
num = input("how big woud you like your flower? The minimun is 20.")
character = input("FireBoy or WaterGirl").lower().strip()
stemcolor = input("Would you like your stem lighter or darker?").lower().strip()

numb = int(num)

colors = {"fireboy":"#FF0000", "watergirl":"#0000FF", "darker":"#000000",
          "lighter":"#967969", "green":"#008900"}

def branch(size):
    if size == 0:
      return
    else:
      tool.color(colors[stemcolor])
      tool.pendown()  
      tool.setheading(270)  #fancy way of angles and degrees (i got this
      #from vic my friend thank you vic your method is great)
      tool.forward(numb*1.35) #go down
      
      tool.color(colors['green'])
      tool.setheading(45)
      tool.forward(numb/2)  
      tool.setheading(15)  
      tool.forward(numb/2)  
      tool.setheading(250)  
      tool.forward(numb/2)  
      tool.setheading(180)  
      tool.forward(numb*1.35/2) #leaf 1 
      
      tool.color(colors[stemcolor])
      tool.setheading(270)  # change the degress
      tool.forward(numb*0.25)  #go down
      
      tool.color(colors['green'])
      tool.setheading(180)
      tool.forward(numb/2) 
      tool.setheading(250)  
      tool.forward(numb/2) 
      tool.setheading(15)  
      tool.forward(numb/2)  
      tool.setheading(60)  
      tool.forward(numb*0.75/2)  #second leaf
      
      tool.color(colors[stemcolor])
      tool.setheading(270)  # change the direct via degress
      tool.forward(numb*1.2)  # Moves the turtle down by 100 units
      tool.stamp()

def swirl(size):
    if size == 0:
      return
    else:
      tool.color(colors[character])
      tool.speed(90)
      tool.forward(2+size/4)
      tool.left(30-size/12)
      swirl(size - 1)


tool.pendown()
swirl(numb)
branch(numb)

#test case 1 (: 