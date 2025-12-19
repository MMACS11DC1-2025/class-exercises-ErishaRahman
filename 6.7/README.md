# Banana Ripeness Checker (summary)
# This program analyzes images of bananas to determine their ripeness based on color
#This will be donw by analyzing the pixel colors in the images
# Blind bakers can use this to sort and find bananas of certain ripeness
#Ripeness can be represented in various concentrations with four main colors
# Green - unripe
# Yellow - ripe
# Brown - overripe
# Black - very unripe


#testings + challenges
Most of my testing was needed for the looping parts involving variables, as well as the RGB color values. for colours, there was no technique to it, just tweaks here and there to make sure that the colors could actually be applicible to the images i was using. For the loops (haha get it pls dont dox my mark), i would try to print any values that seemed like they werent doing their job, and this was quite helpful for the binary search, as i had originally written it for a sorted list that increased.

#profilling
the pixel analysis had taken the longest (~2min), as that was the code scaning all the pixels and apprending them. i had noticed that extra code did not extend the length of time to execute, ot if it did, by a small amount. the rest of the code is either setting up or completing calculations, so the uneven timing is normal.

#extra credits
vic had helped explain large parts of this code to me which it why i was able to comment an explanation. i had also used demo code data to feed to chatgpt to quickly make tables and averages, so chatgpt was a helper in efficiencey.