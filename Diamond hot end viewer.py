# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:45:25 2020

@author: rict
"""




from itertools import combinations_with_replacement
from itertools import permutations, repeat
import itertools
import sys
import re
import copy
import math
import turtle
import numpy as np
import matplotlib
import matplotlib.pyplot as  plt
import pickle
import matplotlib.image as mpimg
from pylab import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import random

turtle.colormode(255)
t=turtle.Turtle()

x_list = []
y_list = []
e_list = []

x0_list = []
y0_list = []
e0_list = []

last_X = 0
last_Y = 0
last_E = 0
X = 0
Y = 0
E = 0

ex_list2 = []

# gcode = [             #This is a sample G code
#     ';TYPE:SKIN',
#     'G1 F1200 X-9.914 Y-9.843 E0',
#     'G0 F9000 X-9.843 Y-9.914',
#     'G1 F1200 X9.914 Y9.843 E3.65844',
#     'G0 F9000 X9.914 Y9.702',
#     'G1 F1200 X-9.702 Y-9.914 E3.95254',
#     'G0 F9000 X-9.560 Y-9.914',
#     'G1 F1200 X9.914 Y9.560 E4.24451',
#     'G0 F9000 X9.914 Y9.419',
#     'G1 F1200 X-9.419 Y-9.914 E4.53437',
#     'G0 F9000 X-9.277 Y-9.914',
#     'G1 F1200 X9.914 Y9.277 E4.82211',
#     'G0 F9000 X9.914 Y9.136',
#     'G1 F1200 X-9.136 Y-9.914 E5.10772',
#     'G0 F9000 X-8.995 Y-9.914',
#     'G1 F1200 X9.914 Y8.995 E5.39123',
#     'G0 F9000 X9.914 Y8.853',
#     'G1 F1200 X-8.853 Y-9.914 E5.67260'
#     ]

#Opening file and reading lines
file = open('Cube.gcode','r', encoding="utf8")
gcode = file.readlines()

#definition of a function for reading each value in line from the mentioned one to the first space 
#when the value chosen does not have a space at the end but just passes to the next line (if end is < -1), it reads to end of the string
def extract_value_from_gcode(gcode_line, character):
    start = gcode_line.find(character)  #Read the chosen character
    if (start > -1):                    #if start is not the last value of the string
        end = gcode_line.find(' ',start) #Read the values from start to the first space
    if end > -1:
        value = float(float(gcode_line[start+1:end]))
    else:
        value = float(float(gcode_line[start+1:]))
    return value
    try:
        float(value)  #to handle errors with strings
        return True
    except ValueError:
        return False



def isFloat(string):   #This is a helper function to test if a string is indeed an integer same as before
    try:
        float(string)
        return True
    except ValueError:
        return False




def modifyList(lst):
    for ind, _ in enumerate(lst):
        lst[ind] -= 1/float(delta) # access list element by index and increment
    return lst





while True:
        numbe = str(input("How many extruders do you want to work with?" + '\n'))
        if numbe in ('1', '2', '3'):
            break
        print("Invalid input. You can work only up to 3 extruders!")

if int(numbe) == 1:
    print("You have only one extruder")
    ##insert the generation of a nwe file copy of the other one
    sys.exit("Use the file")
    

a = input("How much of each extruder do you want to use? Please insert up to 3 values with a space in between" + '\n')
b= list(float(s) for s in a.split())
while sum(b) != 100:
    print("It is no possible!")
    a = input("How much of each extruder do you want to use? Please insert up to 3 values with a space in between" + '\n')
    b= list(float(s) for s in a.split())
if a == '100':
    print("You have only one extruder")
    sys.exit("Use the file")    
    
delta = int(input("How many parts do you want to divide your segment into?" + '\n'))
deltac = delta

c = input("Do you want to have a net division between each extruder? (Y/N)" + '\n')
while c != 'Y' or c != 'N':
    if c == 'Y' or c == 'N':
        break
    c = input("Nope! Do you want to have a net division between each extruder? (Y/N)" + '\n')
    

if c == 'Y':
    ex_list2.extend(repeat(0, round((b[0]/100)*delta)))     
    ex_list2.extend(repeat(1, round((b[1]/100)*delta)))
    if len(b) > 2:
        ex_list2.extend(repeat(2, round((b[2]/100)*delta)))
                
 

    
    
k=0    
if c == 'N':
    
    d = input("Do you want to have the best precision for each extruder? (Y/N) If N it will be random" + '\n')
    while d != 'Y' or d != 'N':
        if d == 'Y' or d == 'N':
            break
        print('Error')
        d = input("Do you want to have the best precision for each extruder? (Y/N) If N it will be random" + '\n')
        
    if d == 'Y':
        
        # while int(b[0]) % int(delta) != 0:
        #     if int(b[0]) % int(delta) == 0 or k > 4:
        #         break
        #     result = int(b[0]) % int(delta)
        #    # print(result)
        #     if result >= int(delta)/2:
        #         deltax = delta + 1
        #     else:
        #         deltax = delta - 1
        #         k += 1    
        #     delta = deltax    
        # d0= delta
        # #print(d0)
        # delta = deltac   
        # while b[1] % int(delta) != 0:
        #     if b[1] % int(delta) == 0 or k > 4:
        #         break
        #     result = b[1] % int(delta)
        #     if result >= int(delta)/2:
        #         deltay = delta + 1
        #     else:
        #         deltay = delta - 1
        #         k += 1
        #     delta = deltay    
            
        # d1= delta
        # #print(d1)
         
        # if sum(b[0] + b[1] != 100):
        #     delta = deltac
        #     while b[2] % int(delta) != 0:
        #         if b[2] % int(delta) == 0 or k > 4:
        #             break
        #         result = b[2] % int(delta)
        #         if result >= int(delta)/2:
        #             deltaz = delta + 1
        #         else:
        #             deltaz = delta - 1
        #             k += 1
        #         delta = deltaz
        # else:
        #     pass
        #     # print(deltaz)
        # d2= delta
        # #print(d2)
        # delta = deltac
        # if d0 != d1 or d1 != d2 or d0 != d2:
        #     delta = 10
        # else:
        #     delta = deltac
        #print(delta)
        while True:
            norm_w1 = [float(f)/float(sum(b)) + float(1/delta) for f in b] 
            #print(norm_w1)
            while True:
                if all(np.less_equal(norm_w1, np.zeros(len(b))+1e-8)): 
                    #modifyList(norm_w1) <= [0.0,0.0,0.0]:
                    break
                round_mod1 = [round(i, 2) for  i in modifyList(norm_w1)] 
                r_modlst1= [0.0 if j <= 0.0 else j for j in round_mod1]
                print(r_modlst1)
          ##############################################################     # print(r_modlst)
                for i in range(len(r_modlst1)):
                    if r_modlst1[i] != 0.0:
                        ex_list2.append(i)  # append the value weighted according to a difference between the percentages and the increments chosen
            break
        print(ex_list2)
    elif d == 'N':
        for i in range(delta):
            if len(b) > 2:
                r = random.randint(0,2)
            else:
                r = random.randint(0,1)
            ex_list2.append(r)
print(ex_list2)
        
# elif c == 'Y':
#     ex_list2.extend(repeat(0, b[0]/10))
#     ex_list2.extend(repeat(1, b[1]/10))
#     if len(b) > 2:
#         ex_list2.extend(repeat(2, b[2]/10))
                
# print(ex_list2)
        
    

outfile = open("out.gcode","w+")

for line_idx, line in enumerate(gcode):
    if 'T0' in line:
            outfile.write(line.replace('T0', 'T1'))
            outfile.write(line.replace('T0', 'T2')) 
    if 'G1 ' in line:
        if 'X' in line:
            if 'E' in line:
                if 'X' in line:
                    X = float(extract_value_from_gcode(line, 'X'))      #read X, Y, E values
                if 'Y' in line:
                    Y = float(extract_value_from_gcode(line, 'Y'))
                if 'E' in line:
                    E = float(extract_value_from_gcode(line, 'E'))
                        
                X_steps = np.round(np.linspace(last_X, X, delta + 1), 3)
                Y_steps = np.round(np.linspace(last_Y, Y, delta + 1), 3)
                E_steps = np.round(np.linspace(last_E, E, delta + 1), 5)             
                
                
                for line_idx, i in enumerate(range(0, int(delta))):                 #write the extruder T0,T1,T2 and if it always the same it passes over 
                    if ex_list2[i-1] == 0:
                        if ex_list2[i-2] == 0 and i>0:
                            pass
                        else:
                            outfile.write('T0;' + '\n')
                                    
                    elif ex_list2[i-1] == 1:
                        if ex_list2[i-2] == 1 and i>0:
                            pass
                        else:
                            outfile.write('T1;' + '\n')
                                    
                    elif ex_list2[i-1] == 2:
                        if ex_list2[i-2] == 2 and i>0:
                            pass
                        else:
                            outfile.write('T2;' + '\n')
                    new_line = line.replace(str(X), str(X_steps[line_idx]))         #replace the value in line with the new value that is the value divided into delta steps with the proper index
                    new_line = new_line.replace(str(Y), str(Y_steps[line_idx]))
                    new_line = new_line.replace(str(E), str(E_steps[line_idx]))
                    outfile.write(new_line)
                    
                last_X = X
                last_Y = Y
                last_E = E
                
    elif 'G0' in line:      #if there is G0, write the same line as it is
        if 'X' in line:
            last_X = extract_value_from_gcode(line, 'X')
        if 'Y' in line:
            last_Y = extract_value_from_gcode(line, 'Y')
        outfile.write(line)
    else:
        outfile.write(line)                       
                            
outfile.close()
                        
file = open('out.gcode','r')
gcode = file.readlines()


    
    
j = 0
i = 0
length=len(gcode)
y_array=np.array([0]*length)
x_array=np.array([0]*length)
z_array=np.array([0]*length)
n_layer=[0]*length
layer_count = 0
colors = []
x_layers_list = []
y_layers_list = []
z_layers_list = []
x_list = []
y_list = []
z_list = []
b_list = []
layer_height = 0
fig0 = plt.figure()

ax0 = fig0.add_subplot(121)
ax1 = fig0.add_subplot(122, projection='3d')
#turtle.Screen().setworldcoordinates(0, 0, 270,290)
t.home()
t.pendown()
current_color = 'red'
for idx, line in enumerate(gcode):   #Read the file line by line
    fline = line.find('LAYER:0')
    if idx < fline:
        break
    
    if 'T0' in line:                #change the color with reading the new extruder
        current_color = 'red'
    elif 'T1' in line:
        current_color = 'blue'
    elif 'T2' in line:
        current_color = 'green'
    if 'G1 ' in line:
        xstart = line.find('X')  #Search for 'x' in the line
        if (xstart >= 0):        #Bigger than -1 if the search found an 'X' character
            xend = line.find(' ',xstart)  #Find the space character after the 'X'
            x_text=line[xstart+1:xend] #copy the characters between xstart and xend. These characters are the text that makes out the first coordinate
        if (isFloat(x_text)):  #Test if indeed we have found a floating point number
            x_number=float(x_text)  #We did manage to identify a floating point number. Convert the x_text string to floating point.
            #    print('X is:', x_number)  #print to terminal
            x_list.append(x_number)
            b_list.append(current_color)
                
        
    if 'G1 ' in line:
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
                
        
                
        
    if line.startswith(';'):
        if 'LAYER:' in line:
            layer_up = line.find(':')   #with the written LAYER it changes the layer unless it is 0 that just continues
            
                
            if (layer_up >=0):
                elayer_up=line.find(' ',layer_up)
                n_lay=line[layer_up+1:elayer_up]
                if n_lay == str(0):
                    continue
                if (isFloat(n_lay)):
                    layer_height=float(n_lay) * 0.1
                    z_list.append(layer_height)
                     #   z_list.append(z_number)
                #    print('\n')
                 #   print('Layer up:',n_lay)
                  #  print('\n')
                        
                   # n_layer[i] = n_lay
                    
                    
            x_layers_list.append(x_list)
            y_layers_list.append(y_list)
            z_layers_list.append(z_list)
                
                #plt.figure()
                
                # if 'T0' in line:
                #     colors = 'red'
                                       
                # elif 'T1' in line:
                #     colors = 'blue'
                    
                # elif 'T2' in line:
                #     colors = 'green'
                
            colors =  ['blue','red','green']
                
            for idx in range(1, len(x_list)):  #plot the lists with the color change
                    #print(idx)
                    #print(x_list[idx-1:idx+1], y_list[idx-1:idx+1], b_list[idx])
                ax0.plot(x_list[idx-1:idx+1], y_list[idx-1:idx+1], color=b_list[idx])
                ax0.set_xlim(min(x_list),max(x_list))
                ax0.set_ylim(min(y_list),max(y_list))
            ax1.plot(x_list, y_list, z_list)
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
                        
                        
                