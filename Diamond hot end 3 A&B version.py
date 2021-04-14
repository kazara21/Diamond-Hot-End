# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:42:42 2021

@author: rict
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:35:44 2021

@author: rict
"""
import turtle
import numpy as np
import matplotlib
import matplotlib.pyplot as  plt
import sys
turtle.colormode(255)
t=turtle.Turtle()


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


"Rules: How many extruders are the extruders we are using but it is acutally a useless question"
"       How much is to select the values A,B or C(optional) for the string"
"       Mixing values is to add the values just inserted to the game, otherwise it adds only one line with those coefficients"
"       Mxing in 3D is only for the 3D rapresentation. By saying yes we include the mixing colour to our model"
"       Tansiction phase is to add the part found on Internet (virtual tools T0-T18 and mix ratios)"


a = []
c = []
A_rem = ""
E_rem = ""
count = 1
add = 0
add1 = 0
n_T = 0
layer_count = 0
z = input('How many?')
n=0

i = input("How much of each extruder do you want to use? Please insert up to 3 values with a space in between" + '\n')
z1 = input('Do you want the mixing with these values? (Y/N)')
a= list(float(s) for s in i.split())
while sum(a) != 100:
    print("It is not possible! The sum needs to be 100!")
    i = input("How much of each extruder do you want to use? Please insert up to 3 values with a space in between" + '\n')
    a= list(float(s) for s in i.split())
print(a)
choice = input("Do you want the mixing colour in the 3D?(Y/N)")
exp = input("Do you want the transiction phase?(Y/N)")
if exp == 'Y':
    exp1 = input("How many effects do you want?")
    exp2 = float(exp1)
# for i in range(len(b)):

#     a.append((b[i]/10))
# print(a)
# for i in range(0, int(a[2])):
#     print(i)
n_file = 'vers2_xyzCalibration_cube'
file = open('vers3_xyzCalibration_cube.gcode','r', encoding="utf8")
gcode = file.readlines()
b = open("AB.gcode","w+")
if exp == 'Y':
    b.write('M163 S0 P1' + '\n' + 
    'M163 S1 P0' + '\n' + 
    'M163 S2 P0' + '\n' + 
    'M164 S0' + '\n' + 
    '\n' +
    'M163 S0 P0' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P0' + '\n' + 
    'M164 S1' + '\n' + 
    '\n' +
    'M163 S0 P0' + '\n' + 
    'M163 S1 P0' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S2' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P0' + '\n' + 
    'M164 S3' + '\n' + 
    '\n' +
    'M163 S0 P0' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S4' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P0' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S5' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S6' + '\n' + 
    '\n' +
    'M163 S0 P2' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P0' + '\n' + 
    'M164 S7' + '\n' + 
    '\n' +
    'M163 S0 P2' + '\n' + 
    'M163 S1 P0' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S8' + '\n' + 
    '\n' +
    'M163 S0 P2' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S9' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P2' + '\n' + 
    'M163 S2 P0' + '\n' + 
    'M164 S10' + '\n' + 
    '\n' +
    'M163 S0 P0' + '\n' + 
    'M163 S1 P2' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S11' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' +  
    'M163 S1 P2' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S12' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P0' + '\n' + 
    'M163 S2 P2' + '\n' + 
    'M164 S13' + '\n' + 
    '\n' +
    'M163 S0 P0' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P2' + '\n' + 
    'M164 S14' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P2' + '\n' + 
    'M164 S15' + '\n' + 
    '\n' +
    'M163 S0 P2' + '\n' + 
    'M163 S1 P2' + '\n' + 
    'M163 S2 P1' + '\n' + 
    'M164 S16' + '\n' + 
    '\n' +
    'M163 S0 P2' + '\n' + 
    'M163 S1 P1' + '\n' + 
    'M163 S2 P2' + '\n' + 
    'M164 S17' + '\n' + 
    '\n' +
    'M163 S0 P1' + '\n' + 
    'M163 S1 P2' + '\n' + 
    'M163 S2 P2' + '\n' + 
    'M164 S18' '\n' + '\n')
    
for line in gcode:
    if z1 == 'Y':        
        if 'G1 ' in line:
            if 'X' in line:
                if 'Y' in line:
                    if len(a) == 2:
                        yup = line.find('E')
                        if (yup >= 0):
                            # yupp = line.find(' ',yup)
                            E_rem=line[yup:]
                            A_rem=line[:yup]
                        new_line = b.write(A_rem + ' A' + str(a[0]/sum(a)) + ' B' + str(a[1]/sum(a)) + ' ' + E_rem)
                    elif len(a) == 3:
                        yup = line.find('E')
                        if (yup >= 0):
                            # yupp = line.find(' ',yup)
                            E_rem=line[yup:]
                            A_rem=line[:yup]
                        new_line = b.write(A_rem + ' A' + str(a[0]/sum(a)) + ' B' + str(a[1]/sum(a)) + ' C' + str(a[2]/sum(a)) + ' ' + E_rem)
                    else:
                        sys.exit("Error: Use the file or try again")
                else:
                    b.write(line)
            else:
                b.write(line)   
        else:
            if 'T1' not in line:
                b.write(line)
    else:
        b.write(line)
    if add == 0:
        if line.startswith('G92'):
            if len(a) > 2:
                b.write('M165 A' + str(a[0]/sum(a)) + ' B' + str(a[1]/sum(a)) + ' C' + str(a[2]/sum(a)) + '  ; a tot for each filament' + '\n' + 'G92 E0' + '\n' + 'G1 E30 F100     ; extrude 30mm' + '\n')
            else:
                 b.write('M165 A' + str(a[0]/sum(a)) + ' B' + str(a[1]/sum(a)) + '  ; a tot for each filament' + '\n' + 'G92 E0' + '\n' + 'G1 E30 F100     ; extrude 30mm' + '\n')
            
            add = 1
    if add1 == 0:
        if line.startswith(';LAYER_COUNT:'):
            b.write("M207 F3000 S4 Z0.3   ; set firmware retraction 50mm/s 4mm, 0.3mm zhop" + "\n" + "M209               ; use firmware retraction"  + "\n")
            add1 = 1
    
    if exp == 'Y':
        if 'LAYER_COUNT:' in line:
            n_layer = line.find(':')
            if n_layer >= 0:
                n_layere= line.find(' ',n_layer)
                n_layer_value=line[n_layer+1:n_layere]
                l_l = round(float(n_layer_value)/(exp2))
                print(l_l)
                layer_count = 0
        if  'Layer count' in line:
            n_layer = line.find(': ')
            if n_layer >= 0:
                n_layere= line.find(' ',n_layer)
                n_layer_value=line[n_layer+1:]
                l_l = round(float(n_layer_value)/(exp2))
                print(l_l)
                layer_count = 0
        if 'LAYER:0' in line:    #'MESH:' + n_file
            layer_count += 1
            if layer_count == l_l:
                b.write('T' + str(n_T) + ';' + '\n')
                n_T += 1
                if n_T == 19:
                    n_T = 0
                layer_count = 0
        # if 'LAYER:' in line:
        #     n_T = 0
                
        
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
###########################################################
###########################################################
# file = open('AB.gcode','r')
# gcode = file.readlines()

# def isFloat(string):   #This is a helper function to test if a string is indeed an integer
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False
    
    
# j = 0
# i = 0
# length=len(gcode)
# y_array=np.array([0]*length)
# x_array=np.array([0]*length)
# n_layer=[0]*length
# layer_count = 0

# x_layers_list = []
# y_layers_list = []
# z_layers_list = []
# x_list = []
# x_list1 = []
# x_list2 = []
# x_list3 = []
# y_list = []
# y_list1 = []
# y_list2 = []
# y_list3 = []
# z_list = []
# b_list = []
# b1_list = []
# b2_list = []
# fig0 = plt.figure()

# ax0 = fig0.add_subplot(121)
# ax1 = fig0.add_subplot(122, projection='3d')
# turtle.Screen().setworldcoordinates(0, 0, 270,290)
# t.home()
# t.pendown()
# b0 = float(a[0]/sum(a))
# b1 = float(a[1]/sum(a))
# b2 = 0
# if len(a) > 2:
#     b2 = float(a[2]/sum(a))
#     vec = [b0,b1,b2]
# else:
#     vec = [b0,b1]
   
# current_color = (b0,b1,b2)

# # The R,G,B values are divided by 255 to change the range from 0..255 to 0..1:
# # R' = R/255
# # G' = G/255
# # B' = B/255
# # The black key (K) color is calculated from the red (R'), green (G') and blue (B') colors:

# K = 1-max(b0, b1, b2)

# #The cyan color (C) is calculated from the red (R') and black (K) colors:

# C = (1-b0-K)/(1-K)

# #The magenta color (M) is calculated from the green (G') and black (K) colors:

# M = (1-b1-K)/(1-K)

# #The yellow color (Y) is calculated from the blue (B') and black (K) colors:

# Y = (1-b2-K)/(1-K)

# current_color1 = 'cyan'
# current_color2 = 'magenta'
# current_color3 = 'yellow'
# for line in gcode:   #Read the file line by line
#     if 'A' in line:                #change the color with reading the new extruder
#         if choice == 'Y':
#             current_color = (C,M,Y)
#     #         if b0 != 0.0:
#     #             current_color1 = 'cyan'
#     #     else:
#     #         if b0 != 0.0:
#     #             current_color = 'cyan'
#     # elif 'B' in line:
#     #     if choice == 'Y':
#     #         current_color = (C,M,Y)
#     #         if b1 != 0.0:
#     #             current_color2 = 'magenta'
#     #         if b0 == 0.0:
#     #             current_color1 = 'magenta'         
#     #     else:
#     #         current_color = 'magenta'
#     #         if b0 == 0.0 and b1 != 0.0:
#     #             current_color1 = 'magenta'
#     #             current_color2 = 'magenta'
            
            
                
#     # elif 'C' in line:
#     #     if b2 != 0.0:
#     #         current_color3 = 'yellow'
            
            
#     xstart = line.find('X')  #Search for 'x' in the line
#     if (xstart >= 0):        #Bigger than -1 if the search found an 'X' character
#         xend = line.find(' ',xstart)  #Find the space character after the 'X'
#         x_text=line[xstart+1:xend] #copy the characters between xstart and xend. These characters are the text that makes out the first coordinate
#         if (isFloat(x_text)):  #Test if indeed we have found a floating point number
#             x_number=float(x_text)  #We did manage to identify a floating point number. Convert the x_text string to floating point.
#         #    print('X is:', x_number)  #print to terminal
#             x_list.append(x_number)
#             x_list1.append(x_number + 0.1)
#             x_list2.append(x_number + 0.2)
#             x_list3.append(x_number + 0.3)
#             b_list.append(current_color)
#             b1_list.append(current_color1)
#             b2_list.append(current_color2)

#     ystart = line.find('Y')  #Do the entire thing again, but for the Y coordinate
#     if (ystart >= 0):
#         yend = line.find(' ',ystart)
#         y_text=line[ystart+1:yend]
#         if (isFloat(y_text)):
#             y_number=float(y_text)
#           #   print('Y is:', y_number)
#             y_list.append(y_number)
#             y_list1.append(y_number + 0.1)
#             y_list2.append(y_number + 0.2)
#             y_list3.append(y_number + 0.3)
#             t.down()
#             t.goto(x_list[i], y_list[i])
#             i=i+1
            
#     estart = line.find('E')  #Do the entire thing again, but for the E coordinate
#     if (estart >= 0):
#         eend = line.find(' ',estart)
#         e_text=line[estart+1:eend]
#         if (isFloat(e_text)):
#             e_number=float(e_text)
#           #  print('E is:', e_number)
#             # print('\n') #A
            
    
#     if line.startswith(';'):
#         if 'LAYER:' in line:
#             layer_up = line.find(':')
#             if (layer_up >=0):
#                 elayer_up=line.find(' ',layer_up)
#                 n_lay=line[layer_up+1:elayer_up]
#                 if n_lay == str(0):
#                     continue
#                 if (isFloat(n_lay)):
#                     layer_height=float(n_lay) * 0.1
#                     z_list.append(layer_height)
            
#             x_layers_list.append(x_list)
#             y_layers_list.append(y_list)
#             z_layers_list.append(z_list)
#             #plt.figure()
#             #colors =  ['cyan','magenta','yellow']
                
#             for idx in range(1, len(x_list)):  #plot the lists with the color change
#                     #print(idx)
#                     #print(x_list[idx-1:idx+1], y_list[idx-1:idx+1], b_list[idx])
#                 if choice == 'Y':
#                     ax0.plot(x_list[idx-1:idx+1], y_list[idx-1:idx+1], color=current_color)
#                     if b0 != 0.0:
#                         ax0.plot(x_list1[idx-1:idx+1], y_list1[idx-1:idx+1], color=current_color1)
#                     if b1 != 0.0: 
#                         ax0.plot(x_list2[idx-1:idx+1], y_list2[idx-1:idx+1], color=current_color2)
#                     if len(a) > 2:
#                         ax0.plot(x_list3[idx-1:idx+1], y_list3[idx-1:idx+1], color=current_color3)
#                 else:
#                     if b0 != 0.0:
#                         ax0.plot(x_list1[idx-1:idx+1], y_list1[idx-1:idx+1], color=current_color1)
#                     if b1 != 0.0: 
#                         ax0.plot(x_list2[idx-1:idx+1], y_list2[idx-1:idx+1], color=current_color2)
#                     if len(a) > 2:
#                         ax0.plot(x_list3[idx-1:idx+1], y_list3[idx-1:idx+1], color=current_color3)
                
#                 ax0.set_xlim(min(x_list),max(x_list))
#                 ax0.set_ylim(min(y_list),max(y_list))
                
#                 if choice == 'Y':
#                     ax1.plot(x_list[idx-1:idx+1], y_list[idx-1:idx+1], z_list, color=current_color)
#                     if b0 != 0.0:
#                         ax1.plot(x_list1[idx-1:idx+1], y_list1[idx-1:idx+1], z_list, color=current_color1)
#                     if b1 != 0.0:
#                         ax1.plot(x_list2[idx-1:idx+1], y_list2[idx-1:idx+1], z_list, color=current_color2)
#                     if len(a) > 2:
#                         ax1.plot(x_list3[idx-1:idx+1], y_list3[idx-1:idx+1], z_list, color=current_color3)
#                 else:
#                     if b0 != 0.0:
#                         ax1.plot(x_list1[idx-1:idx+1], y_list1[idx-1:idx+1], z_list, color=current_color1)
#                     if b1 != 0.0:
#                         ax1.plot(x_list2[idx-1:idx+1], y_list2[idx-1:idx+1], z_list, color=current_color2)
#                     if len(a) > 2:
#                         ax1.plot(x_list3[idx-1:idx+1], y_list3[idx-1:idx+1], z_list, color=current_color3)

#                 plt.xlim(min(x_list),max(x_list))
#                 plt.ylim(min(y_list),max(y_list))
#                 # else:
#                 #     colors[idx+1] = colors[idx]
#                 # if colors[idx] == 1 and len(colors) > 2:
#                 #     colors[idx] = colors[idx-1]
        
#                 #ax0.plot(x_list, y_list)
#                 #plt.draw()
                
                
#             plt.pause(0.1)
#             #plt.axis('tight')
#             plt.show(block = False)
                
                
#             x_list = []
#             x_list1 = []
#             x_list2 = []
#             x_list3 = []
#             y_list = []
#             y_list1 = []
#             y_list2 = []
#             y_list3 = []
#             z_list = []
#             t.clear()
#             t.pendown()
#             print("Layer %i: %i points" % (layer_count, i))   #it counts the number of points per layer
#               #  print('n. of point', i)
#             i = 0
#             layer_count += 1      