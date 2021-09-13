import math

sect = 12
angle = 360 / sect
r1 = 10
r2 = 20
xc1= 40
yc1 = 40
ang = 0
angles = []
circle = []
rate = 0
height = 0.3
rates = []
b = open("Radial.gcode","w+")
b.write('M109 T0 S220.000000' + '\n' +
        'T0' + '\n' +
        '; -- START GCODE --' + '\n' +
        'G21        ;metric values' + '\n' +
        'G90        ;absolute positioning' + '\n' +
        'M107       ;start with the fan off' + '\n' +
        'G28 X0 Y0  ;move X/Y to min endstops' + '\n' +
        'G28 Z0     ;move Z to min endstops' + '\n' +
        'G1 Z15.0 F1200 ;move the platform down 15mm' + '\n' +
        'G92 E0                  ;zero the extruded length' + '\n' +
        'M165 A0.33 B0.33 C0.34  ; a tot for each filament' + '\n' +
        'G92 E0' + '\n' +
        'G1 E30 F100     ; extrude 30mm' + '\n' +
        'G1 F200 E5              ;extrude 5mm of feed stock' + '\n' +
        'G92 E0                  ;zero the extruded length again' + '\n' +
        'G1 F3000' + '\n' +
        '; -- end of START GCODE --' + '\n' +
        'G0 F3000 X0 Y0' + '\n' +
        ';LAYER:0' + '\n')

layer = 0
b.write('M107' + '\n' +
'G0 F2000 X40 Y30 Z0.30' + '\n' +
'G0 X40 Y40' + '\n' )

for j in range (0,70):
    for idx,i in enumerate(range(0,12)):
        #points in the circumference
        tx = (math.cos((math.pi / 180) * ang) * r1)
        ty = (math.sin((math.pi / 180) * ang) * r1)
        tx1 = (math.cos((math.pi / 180) * ang) * r2)
        ty1 = (math.sin((math.pi / 180) * ang) * r2)
        if -1e-8< tx < 1e-8:
            tx = 0.0
        if -1e-8< ty < 1e-8:
            ty = 0.0
        if -1e-8< tx1 < 1e-8:
            tx1 = 0.0
        if -1e-8< ty1 < 1e-8:
            ty1 = 0.0
        rate += 0.5

        tx = round(tx, 4)
        ty = round(ty, 4)
        tx1 = round(tx1, 4)
        ty1 = round(ty1, 4)
        xc1 = round(xc1, 4)
        yc1 = round(yc1, 4)
        #go to the
        b.write('G0' + ' X' + str(xc1) + ' Y' + str(yc1) + ' E' + str(round(rate, 4)) + '\n')

        b.write('G1' + ' X'+ str(round(tx + xc1,4)) + ' Y' + str(round(ty + yc1,4)) + ' E' + str(round(rate,4)) + '\n')
        angles.append([tx,ty])
        rate += 0.5
        b.write('G1' + ' X' + str(round(tx1 + xc1,4)) + ' Y' + str(round(ty1 + yc1,4)) + ' E' + str(round(rate,4)) + '\n')
        angles.append([tx1,ty1])
        #rate = rate - 0.01
        #b.write('G1' + ' Z' + str(round(height +0.1,2)) + ' E' + str(round(rate,4)) + '\n' )
        b.write('G0' + ' X' + str(round(tx1 + xc1 + tx1,4)) + ' Y' + str(round(ty1 + yc1 + ty1,4)) + '\n')
        b.write('G0' + ' X' + str(xc1) + ' Y' + str(yc1) + '\n') #+
                #'G0' + ' Z' + str(round(height,2)) + '\n')
        angles.append([0,0])
        rate = rate + 0.5
        circle.append([tx1, ty1])
         #    if (ang >= 0) :
    #         angles.append([tx, ty]);

        ang += angle
    n = j

    height += 0.3
    b.write(';LAYER:' + str(j+1) + '\n' +
            'G0' + ' Z' + str(round(height,2)) + '\n')
    a = print(rate)
    layer += 1
    for i in range(0, 13):

        ax = (math.cos((math.pi / 180) * ang) * r2)
        ay = (math.sin((math.pi / 180) * ang) * r2)
        if -1e-8 < ay < 1e-8:
            ay = 0.0
        if -1e-8 < ax < 1e-8:
            ax = 0.0
        ax = round(ax, 4)
        ay = round(ay, 4)
        xc1 = round(xc1, 4)
        yc1 = round(yc1, 4)
        rate = rate + 0.5

        b.write('G1' + ' X' + str(round(ax + xc1,4)) + ' Y' + str(round(ay + yc1,4)) + ' E' + str(round(rate,4)) + '\n')


        ang += angle
    ang = 0

    print(angles)
    print(circle)
    angles = []
b.write('M107' + '\n' +
        'G1 F2400 E2487.91257' + '\n' +
        'G0 F3000 X43.70 Y41.91 Z105.00' + '\n' +
        '; -- END GCODE --' + '\n' +
        'M104 S0                     ;extruder heater off' + '\n' +
        'M140 S0                     ;heated bed heater off (if you have it)' + '\n' +
        ';G90' + '\n' +
        'G91                                    ;relative positioning' + '\n' +
        'G1 E-5 F300                            ;retract the filament a bit before lifting the nozzle, to release some of the pressure' + '\n' +
        'G1 Z200 F3000 ;move Z up a bit and retract filament even more' + '\n' +
        'G28 X0 Y0                              ;move X/Y to min endstops, so the head is out of the way' + '\n' +
        'M84                         ;steppers off' + '\n' +
        'G90                         ;absolute positioning' + '\n' +
        '; -- end of END GCODE --' + '\n' +
        'G1 X45 F2000      ;Move X axis to part ejection position' + '\n' +
        'G1 Y120           ;Move Y axis to part ejection position' + '\n' +
        'G4 P1             ;Sleep for 1 millisecond. Seems stupid but forces the printer to empty the motion buffer before continuing to next code line.' + '\n' +
        'M42 P57 S255      ;Start conveyor belt' + '\n' +
        'G4 S8             ;Wait 8 seconds' + '\n' +
        'M42 P57 S0        ;Stop conveyor belt' + '\n' +
        'G1 Y0             ;Move to home' + '\n' +
        'G1 X120           ;Move to home' + '\n')
b.close()