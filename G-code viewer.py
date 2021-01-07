# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import turtle
import numpy as np
import matplotlib
import matplotlib.pyplot as  plt
turtle.colormode(255)
t=turtle.Turtle()

    

file = open('sCube.gcode','r')
gcode = file.readlines()

def isFloat(string):   #This is a helper function to test if a string is indeed an integer
    try:
        float(string)
        return True
    except ValueError:
        return False
    
    
j = 0
i = 0
length=len(gcode)
y_array=np.array([0]*length)
x_array=np.array([0]*length)
n_layer=[0]*length
layer_count = 0

x_layers_list = []
y_layers_list = []
x_list = []
y_list = []


turtle.Screen().setworldcoordinates(0, 0, 270,290)
t.home()
t.pendown()
for line in gcode:   #Read the file line by line
    xstart = line.find('X')  #Search for 'x' in the line
    if (xstart >= 0):        #Bigger than -1 if the search found an 'X' character
        xend = line.find(' ',xstart)  #Find the space character after the 'X'
        x_text=line[xstart+1:xend] #copy the characters between xstart and xend. These characters are the text that makes out the first coordinate
        if (isFloat(x_text)):  #Test if indeed we have found a floating point number
            x_number=float(x_text)  #We did manage to identify a floating point number. Convert the x_text string to floating point.
        #    print('X is:', x_number)  #print to terminal
            x_list.append(x_number)
            

    ystart = line.find('Y')  #Do the entire thing again, but for the Y coordinate
    if (ystart >= 0):
        yend = line.find(' ',ystart)
        y_text=line[ystart+1:yend]
        if (isFloat(y_text)):
            y_number=float(y_text)
         #   print('Y is:', y_number)
            y_list.append(y_number)
            t.down()
            t.goto(x_list[i], y_list[i])
            i=i+1
            
    estart = line.find('E')  #Do the entire thing again, but for the E coordinate
    if (estart >= 0):
        eend = line.find(' ',estart)
        e_text=line[estart+1:eend]
        if (isFloat(e_text)):
            e_number=float(e_text)
          #  print('E is:', e_number)
           # print('\n') #A
            
    
    if line.startswith(';'):
        if 'LAYER:' in line:
            layer_up = line.find(':')
            if (layer_up >=0):
                elayer_up=line.find(' ',layer_up)
                n_lay=line[layer_up+1:elayer_up]
            #    print('\n')
             #   print('Layer up:',n_lay)
              #  print('\n')
                n_layer[i] = n_lay
            
            x_layers_list.append(x_list)
            y_layers_list.append(y_list)
            
            #plt.figure()
            plt.plot(x_list, y_list)
            plt.draw()
            plt.show(block = False)
            x_list = []
            y_list = []
            t.clear()
            t.pendown()
            print("Layer %i: %i points" % (layer_count, i))
          #  print('n. of point', i)
            i = 0
            layer_count += 1
            
    
    
  
   
    
#for lines in gcode:
 #   m =re.search(

        
      #  print('Layer is:', layer_number)
 #   t.up()
    
    # t.goto(x_array[j], y_array[j])
  

#fig, ax = plt.subplots()
#ax.plot([x_array[i]], [y_array[i]])
#ax.set(xlabel='x', ylabel='y')
#ax.grid()




    

    



