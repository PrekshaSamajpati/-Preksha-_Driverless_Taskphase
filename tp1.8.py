import csv
import math
# Creating cones.csv
p = open("cones.csv", "w", newline="")
writer=csv.writer(p)
writer.writerow((["id", "x", "y", "colour"]))
n=int(input("Enter number of elements: "))
for i in range(n):
    print("Cone Number ",i+1)
    cone_id=input("enter id")
    colour=input("Enter blue or yellow: ")
    x=int(input("Enter x-coordinate: "))
    y=int(input("Enter y-coordinate: "))
    srecord=[cone_id,x,y,colour]
    writer.writerow(srecord)
    p.flush()
# Reading cones.csv
p = open("cones.csv", "r", newline="")
reader=csv.reader(p)
next(reader)
cones=[]
for row in reader:
    colour=row[3]
    x=int(row[1])
    y=int(row[2])
    cone_id=row[0]
    # Distance from origin
    distance=math.sqrt(x*x+y*y)
    cones.append([cone_id,x,y,colour,distance])
# Sort according to distance
for i in range(len(cones)):
    for j in range(i+1,len(cones)):
        if cones[i][4] > cones[j][4]:
            temp=cones[i]
            cones[i]=cones[j]
            cones[j]=temp
# Create blue.csv and yellow.csv
blue=open("blue.csv","w",newline="")
yellow=open("yellow.csv","w",newline="")
bluewriter=csv.writer(blue)
yellowwriter=csv.writer(yellow)
bluewriter.writerow(["id", "x", "y", "colour"])
yellowwriter.writerow(["id", "x", "y", "colour"])
for cone in cones:
    if cone[3]=="blue":
        bluewriter.writerow([cone[0],cone[1],cone[2],cone[3]])
    else:
        yellowwriter.writerow([cone[0],cone[1],cone[2],cone[3]])
blue.close()
yellow.close()
# Find nearest yellow cone for every blue cone
centre=open("centreline.csv","w",newline="")
centrewriter=csv.writer(centre)
centrewriter.writerow(['Blue_x','Blue_y','Yellow_x','Yellow_y',
                       'Midpoint_x','Midpoint_y'])
for bluecone in cones:

    if bluecone[3]=="blue":

        bx=bluecone[1]
        by=bluecone[2]

        mindistance=999999
        nearestx=0
        nearesty=0

        for yellowcone in cones:

            if yellowcone[3]=="yellow":

                yx=yellowcone[1]
                yy=yellowcone[2]

                distance=math.sqrt((bx-yx)*(bx-yx)
                                   +(by-yy)*(by-yy))

                if distance<mindistance:
                    mindistance=distance
                    nearestx=yx
                    nearesty=yy

        # Calculate midpoint
        midx=(bx+nearestx)/2
        midy=(by+nearesty)/2

        centrewriter.writerow([bx,by,nearestx,nearesty,midx,midy])
centre.close()
print("All files created successfully!")
