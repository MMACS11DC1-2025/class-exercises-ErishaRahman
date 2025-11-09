TURTLE RECURSIVE FLOWER PROJECT
⋆°❀⋆.ೃ࿔*:･⋆°❀⋆.ೃ࿔*:･⋆°❀⋆.ೃ࿔*:･⋆°❀⋆.ೃ࿔*:･

instructions!!!
    Once the code is inputed into trinket, enter a size under 150 thats prefferably over 20.
        numbers that are 0 or below will not work.
    Enter "fireboy" or Watergirl" (not case sensitive) for a color. the code will not work other other words
    Enter "lighter" or "darker" for a stem color. the code will not work with other words.
    Once the three inputs are properly added, a flower will be drawn with the specific colors and size chosen

Recursion and depth discussion
    The number of recurssions, [size], would be decreased with every loop, pushing it closer and closer to the base case, since i wanted a normal swirl without any weird patterns occuring. i did not set a definate limit because unless the program crashes, the sixe can work with most values. i wouldve added a maximum, but trinket has a weird feature of being able to increase/decrease the canvas in an odd way depending on device, so i left that up to preference, though i think 100-150 is large enough. i wrote the code to give the same proportions to every flower, not dependant on size aswell.

My test cases
![alt text](image-1.png)
![alt text](image2.png)
![alt text](image3.png)



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

Debugs/tests
    Most of my debugging and testing was for the colors and leaves, and less of the swirl.
    i wanted to add some leaves to enhance the drawing, but the left and right functions were unhelpful 
    due to them 