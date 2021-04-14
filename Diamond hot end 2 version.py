# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:35:44 2021

@author: rict
"""
import turtle
import numpy as np
import matplotlib
import matplotlib.pyplot as  plt
turtle.colormode(255)
t=turtle.Turtle()


a = []
c = []

count = 1
z = input('How many?')
n=0
b = input("How much of each extruder do you want to use? Please insert up to 3 values with a space in between" + '\n')
a= list(int(s) for s in b.split())
print(a)
# for i in range(len(b)):

#     a.append((b[i]/10))
# print(a)
# for i in range(0, int(a[2])):
#     print(i)
    
file = open('LOOPcube.gcode','r', encoding="utf8")
gcode = file.readlines()
b = open("b.gcode","w+")

for line in gcode:
    if 'G1 ' in line:
        if n == 0:
            if count == a[0]:
                b.write(line + 'T1' + '\n')
            else:
                b.write(line)
            count += 1
            if count == a[0]+1:
                count = 1
                n=1
        if n == 1:
            if count == a[1]:
                if z == str(3):
                    b.write(line + 'T2' + '\n')
                else:
                    b.write(line + 'T0' + '\n')
            else:
                b.write(line)
            count += 1
            if count == a[1]+1:
                count = 1
                if z == str(3):
                    n = 2
                else: 
                    n = 0
        if n == 2:
            if count == a[2]:
                b.write(line + 'T0' + '\n')
            else:
                b.write(line)
            count += 1
            if count == a[2]+1:
                count = 1
                n = 0
    else:
        b.write(line)
            
b.close()
    # if 'G0' in line:
    #     pass
    # else:
    #     print(line)
    #     c.append(line)
    #     # do stuff
        
# for i in range(len(c)):
#     next(c)
# for

file = open('b.gcode','r')
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
z_layers_list = []
x_list = []
y_list = []
z_list = []
b_list = []
fig0 = plt.figure()

ax0 = fig0.add_subplot(121)
ax1 = fig0.add_subplot(122, projection='3d')
turtle.Screen().setworldcoordinates(0, 0, 270,290)
t.home()
t.pendown()
current_color = 'red'
for line in gcode:   #Read the file line by line
    if 'T0' in line:                #change the color with reading the new extruder
        current_color = 'red'
    elif 'T1' in line:
        current_color = 'blue'
    elif 'T2' in line:
        current_color = 'green'
    xstart = line.find('X')  #Search for 'x' in the line
    if (xstart >= 0):        #Bigger than -1 if the search found an 'X' character
        xend = line.find(' ',xstart)  #Find the space character after the 'X'
        x_text=line[xstart+1:xend] #copy the characters between xstart and xend. These characters are the text that makes out the first coordinate
        if (isFloat(x_text)):  #Test if indeed we have found a floating point number
            x_number=float(x_text)  #We did manage to identify a floating point number. Convert the x_text string to floating point.
        #    print('X is:', x_number)  #print to terminal
            x_list.append(x_number)
            b_list.append(current_color)

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
                if n_lay == str(0):
                    continue
                if (isFloat(n_lay)):
                    layer_height=float(n_lay) * 0.1
                    z_list.append(layer_height)
            
            x_layers_list.append(x_list)
            y_layers_list.append(y_list)
            z_layers_list.append(z_list)
            #plt.figure()
            colors =  ['blue','red','green']
                
            for idx in range(1, len(x_list)):  #plot the lists with the color change
                    #print(idx)
                    #print(x_list[idx-1:idx+1], y_list[idx-1:idx+1], b_list[idx])
                ax0.plot(x_list[idx-1:idx+1], y_list[idx-1:idx+1], color=b_list[idx])
                ax0.set_xlim(min(x_list),max(x_list))
                ax0.set_ylim(min(y_list),max(y_list))
                ax1.plot(x_list[idx-1:idx+1], y_list[idx-1:idx+1], z_list, color=b_list[idx])
                plt.xlim(min(x_list),max(x_list))
                plt.ylim(min(y_list),max(y_list))
                # else:
                #     colors[idx+1] = colors[idx]
                # if colors[idx] == 1 and len(colors) > 2:
                #     colors[idx] = colors[idx-1]
        
                #ax0.plot(x_list, y_list)
                #plt.draw()
                
                
            plt.pause(0.1)
            #plt.axis('tight')
            plt.show(block = False)
                
                
            x_list = []
            y_list = []
            z_list = []
            t.clear()
            t.pendown()
            print("Layer %i: %i points" % (layer_count, i))   #it counts the number of points per layer
              #  print('n. of point', i)
            i = 0
            layer_count += 1      