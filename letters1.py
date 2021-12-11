
import matplotlib
import matplotlib.pyplot as plt
import math
import csv

def generate_letter_point(which_letter,height,current,points_distance=2):

        if which_letter == 'A':
            # WIDTH = ?
            points1 = []
            increment = points_distance * (height/3.8) / math.sqrt(height ** 2 + (height / 3.8) ** 2)
            x_coordinate = 0
            while 3.8*x_coordinate<height:
                points1.append((x_coordinate,3.8*x_coordinate))
                x_coordinate = x_coordinate + increment

            points2 = []
            while -3.8*x_coordinate+2*height>0:
                points2.append((x_coordinate, -3.8*x_coordinate+2*height))
                x_coordinate = x_coordinate + increment
            start_of_line = min(points1, key=lambda x: abs(x[1] - 0.6 * height))
            end_of_line = min(points2, key=lambda x: abs(x[1] - 0.6 * height))

            points3 = []
            for i in range(int(start_of_line[0]),int(end_of_line[0]),points_distance):
                points3.append((i,0.6*height))

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0] + current, i[1]))

            current = current + int(0.526*height) + int(height/10)
            return points,current


        elif which_letter == 'B':
            # WIDTH = (0.1 + 0.3 = 0.4) * HEIGHT
            points1 = []
            radius_1 = 0.2 * height
            radius_2 = 0.3 * height
            arc_length = distance_between_points
            theta_1 = arc_length * 360 / (2 * math.pi * radius_1)
            theta_2 = arc_length * 360 / (2 * math.pi * radius_2)
            i = -90
            while i < 90:
            #for i in range(-90, 90, theta_1):
                points1.append((radius_1 * math.cos(i * math.pi / 180) + height/10, radius_1 * math.sin(i * math.pi / 180) +0.8*height))
                i = i + theta_1

            i = -90
            while i < 90:
            #for i in range(-90, 90, int(theta_2)):
                points1.append((radius_2 * math.cos(i * math.pi / 180) + height / 10,
                                radius_2 * math.sin(i * math.pi / 180) + 0.3 * height))
                i = i + theta_2

            points2 = []
            for i in range(0,height,points_distance):
                points2.append((0,i))

            points3 = []
            for i in range(0,int(height/10),points_distance):
                points3.append((i,0))
                points3.append((i,0.6*height))
                points3.append((i,height))

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0]+current,i[1]))

            current = current + int(0.4*height) + int(height / 10)
            return points,current


        elif which_letter == 'C':
            # WIDTH = (2 * 0.2 = 0.4) * HEIGHT
            points1 = []
            radius = height / 5
            arc_length = distance_between_points
            theta = arc_length * 360 / (2 * math.pi * radius)
            i = 0
            while i < 180:
            #for i in range(0, 180, int(theta)):
                points1.append((radius+radius * math.cos(i * math.pi / 180),radius * math.sin(i * math.pi / 180) + height-radius))
                points1.append((radius+radius * math.cos((i+180)  * math.pi / 180),radius * math.sin((i+180)  * math.pi / 180) + radius))
                i = i + theta

            points2 = []
            for i in range(int(radius),int(height-radius),points_distance):
                points2.append((0,i))

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(2*radius) + int(height/10)
            return points,current


        elif which_letter == 'D':
            # WIDTH = (2 * 0.2 = 0.4) * HEIGHT
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((0,i))

            points2 = []
            radius = 0.3 * height
            arc_length = distance_between_points
            theta = arc_length * 360 / (2 * math.pi * radius)
            #for i in range(-90, 90, 5):
            #    points2.append((height/10+radius * math.cos(i * math.pi / 180),radius+radius * math.sin(i  * math.pi / 180)))
            i = -90
            while i < 90:
                points2.append((height / 10 + radius * math.cos(i * math.pi / 180), height/2 + radius * math.sin(i * math.pi / 180)*1.65))
                i = i + theta

            points3 = []
            for i in range(0,int(height/10),points_distance):
                points3.append((i,height))
                points3.append((i, 0))

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0]+current,i[1]))

            current = current + int(radius) + int(height/10)
            return points,current


        elif which_letter == 'E':
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((0,i))
            points2 = []
            for i in range(0,int(height/3),points_distance):
                points2.append((i,0))
                points2.append((i,int(height/2)))
                points2.append((i,height))

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(height/3) + int(height/10)
            return points,current

        elif which_letter == 'F':
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((current,i))

            points2 = []
            for i in range(current, current+int(0.4*height), points_distance):
                points2.append((i, height))

            points3 = []
            for i in range(current, current + int(0.33 * height), points_distance):
                points3.append((i, 0.68*height))

            points = points1 + points2 + points3
            current = current + int(0.4 * height) + int(height/10)
            return points,current


        elif which_letter == 'G':
            points1 = []
            radius = height/2
            #arc_length = 2*math.pi*radius*(theta/360)
            arc_length = distance_between_points
            theta = arc_length*360/(2*math.pi*radius)
            #print(theta)
            #arc_length = 2*math.pi*radius*(theta/360)
            #print(arc_length)
            #for i in range(60,360,int((2*math.pi*height/2)/360)):
            for i in range(60, 360, int(theta)):
                points1.append((radius*math.cos(i*math.pi/180),radius*math.sin(i*math.pi/180)))

            points2 = []
            for i in range(int(height/2),int(0.2*height), -points_distance):
                points2.append((i,0))

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((i[0] + current + height/2,i[1]+height/2))

            current = current + height + int(height/10)
            return points,current


        elif which_letter == 'H':
            points1 = []
            for i in range(0, height, points_distance):
                points1.append((0, i))
                points1.append((height/3,i))

            points2 = []
            for i in range(0, int(height/3), points_distance):
                points2.append((i, height/2))

            points3 = points1+points2

            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(height/3) + int(height/10)
            return points,current


        elif which_letter == 'I':
            points1 = []
            initial = current
            for i in range(0,int(0.9*height),points_distance):
                for j in range(current,current+int(height/25),points_distance):
                    points1.append((j,i))
            points2 = []
            for i in range(0, 360, points_distance):
                points2.append(((height / 50) * math.cos(i * math.pi / 180), (height / 50) * math.sin(i * math.pi / 180)))
            points3 = []
            for i in points2:
                points3.append((i[0]+height/50+current,i[1]+0.98*height))
            points = points1 + points3

            current = current + int(2*height/10)
            return points,current


        elif which_letter == 'J':
            points1 = []
            for i in range(int(height/6), height, points_distance):
                points1.append((height/6, i))

            points2 = []
            for i in range(-int(height/6), int(height/6), points_distance):
                points2.append((i, height))

            points3 = []
            radius = height / 6
            for i in range(180, 360, int((2 * math.pi * height / 2) / 360)):
                points3.append((radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current+i[0]+height/6,i[1]))

            current = current + int(height/3) + int(height/10)
            return points,current


        elif which_letter == 'K':
            points1 = []
            for i in range(0, height, points_distance):
                points1.append((0, i))

            points2 = []
            for i in range(0, int(height/20), points_distance):
                points1.append((i, height/2))

            points3 = []
            for i in range(0,int(height/3-height/20),int(points_distance/1.764)):
                points3.append((i,height/2+1.764*i))
                points3.append((i,height/2 -1.764 * i))

            points4 = []
            for i in points3:
                points4.append((i[0]+height/20,i[1]))

            points5 = points1 + points2 + points4

            points = []
            for i in points5:
                points.append((i[0]+current,i[1]))

            current = current + int(height/3) + int(height/10)
            return points,current


        elif which_letter == 'L':
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((0,i))

            for i in range(0,int(height/3),points_distance):
                points1.append((i,0))

            points = []
            for i in points1:
                points.append((i[0]+current,i[1]))

            current = current + int(height/3) + int(height/10)
            return points,current


        elif which_letter == 'M':
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((0,i))
                points1.append((0.8*height, i))

            points2 = []
            for i in range(0, int(0.4*height),int(points_distance/math.sqrt(5))):
                points2.append((i,height-i))
                points2.append((i+0.4*height, i+0.6*height))

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(0.8*height) + int(height/10)
            return points,current


        elif which_letter == 'N':
            points1 = []
            for i in range(0,height,points_distance):
                points1.append((0,i))
                points1.append((0.4*height, i))

            points2 = []
            for i in range(0, int(0.4*height),int(points_distance/math.sqrt(5))):
                points2.append((i,height-2.5*i))

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(0.4*height) + int(height/10)
            return points,current


        elif which_letter == 'O':
            points1 = []
            radius = height / 2
            arc_length = distance_between_points
            theta = arc_length * 360 / (2 * math.pi * radius)
            for i in range(0, 360, int(theta)):
                points1.append((radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))

            points = []
            for i in points1:
                points.append((i[0]+current,i[1]))

            current = current + int(height) + int(height/10)
            return points,current


        elif which_letter == 'P':
            points1 = []
            for i in range(0, height,points_distance):
                points1.append((0,i))

            points2 = []
            for i in range(0, int(height/20),points_distance):
                points2.append((i, height))
                points2.append((i,0.7*height))

            points3 = []
            radius = 0.15*height
            for i in range(-90, 90, int((2 * math.pi * height / 2) / 360)):
                points3.append((height/20 + radius * math.cos(i * math.pi / 180), 0.7*height + radius + radius * math.sin(i * math.pi / 180)))

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0]+current,i[1]))

            current = current + int(0.15*height) + int(height/20) + int(height/10)
            return points,current


        elif which_letter == 'Q':
            points1 = []
            radius = height / 2
            for i in range(0, 360, int((2 * math.pi * height / 2) / 360)):
                points1.append((radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))

            points2 = []
            for i in range(int(radius/2),int(radius),int(points_distance/math.sqrt(2))):
                points2.append((i+radius,-i+radius))

            points3 = points1+points2

            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + height + int(height / 10)
            return points, current


        elif which_letter == 'R':
            points1 = []
            for i in range(0, height,points_distance):
                points1.append((0,i))

            points2 = []
            for i in range(0, int(height / 20), points_distance):
                points2.append((i, height))
                points2.append((i, 0.7 * height))

            points3 = []
            radius = 0.15 * height
            for i in range(-90, 90, int((2 * math.pi * height / 2) / 360)):
                points3.append((height / 20 + radius * math.cos(i * math.pi / 180),
                                0.7 * height + radius + radius * math.sin(i * math.pi / 180)))

            points4 = []
            for i in range(0, int(0.15*height),int(points_distance/4)):
                points4.append((i+height/20,0.7*height-4.7*i))

            points5 = points1 + points2 + points3 + points4
            points = []
            for i in points5:
                points.append((i[0] + current, i[1]))

            current = current + int(0.2 * height) + int(height/10)
            return points, current


        elif which_letter == 'S':
            points1 = []
            for i in range(-30, 90, points_distance):
                points1.append((height*0.075 * math.cos(i * math.pi / 180),0.15*height+height*0.075 * math.sin(i * math.pi / 180)))

            points2 = []
            for i in range(90, 270, points_distance):
                points2.append((height*0.075 * math.cos(i * math.pi / 180), (abs(math.sin(i * math.pi / 180))+2)*height*0.075 * math.sin(i * math.pi / 180)))

            points3 = []
            for i in points2:
                points3.append((-i[0],i[1]-0.45*height))

            points4 = []
            for i in range(150, 270, points_distance):
                points4.append((height * 0.075 * math.cos(i * math.pi / 180),height * 0.075 * math.sin(i * math.pi / 180)-0.6*height))

            points = []
            points5 = points1 + points2 + points3 + points4
            for i in points5:
                points.append((current+0.075*height+i[0],0.675*height+i[1]))

            current = current + int(0.15*height) + int(height/10)
            return points,current


        elif which_letter == 'T':
            points1 = []
            width = 0.33*height
            for i in range(0, height,points_distance):
                points1.append((width/2,i))

            points2 = []
            for i in range(0, int(width), points_distance):
                points2.append((i, height))

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + int(width) + int(height / 10)
            return points, current


        elif which_letter == 'U':
            points1 = []
            width = 0.33*height

            points2 = []
            full_radius = width / 2
            for i in range(0,int(width / 2),int(points_distance/2)):
                #points2.append((-i,-(2/7)*math.sqrt(width**2-4*i**2)+width/4))
                #points2.append((i, -(2 / 7) * math.sqrt(width ** 2 - 4 * i ** 2)+width/4))
                points2.append((-i + width/2,-(1/3)*math.sqrt(width**2-4*i**2)+width/3))
                points2.append((i + width/2, -(1 / 3) * math.sqrt(width ** 2 - 4 * i ** 2)+width/3))

            maxi = 0
            for i in points2:
                if i[1] > maxi:
                    maxi = i[1]

            points3 = []
            for i in range(int(maxi),height):
                points3.append((0,i))
                points3.append((width, i))



            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((i[0]+current,i[1]))

            current = current + int(width) + int(height / 10)
            return points, current


        elif which_letter == 'V':
            width = 0.33*height

            points1 = []
            for i in range(0,int(width/2),int(points_distance/3.2)):
                points1.append((i,height-i*6.06))
                points1.append((i+width/2,i*6.06))

            points = []
            for i in points1:
                points.append((i[0] + current, i[1]))
            current = current + int(width) + int(height / 10)
            return points, current


        elif which_letter == 'W':
            width = 0.33*height

            points1 = []
            for i in range(0,int(width/4),int(points_distance/6.4)):
                points1.append((i,height-i*12.12))
                points1.append((i+width/4,i*12.12))
                points1.append((i+width/2, height - i * 12.12))
                points1.append((i + 3*width / 4, i * 12.12))

            points = []
            for i in points1:
                points.append((i[0] + current, i[1]))
            current = current + int(width) + int(height / 10)
            return points, current


        elif which_letter == 'X':
            width = 0.33*height

            points1 = []
            for i in range(0,int(width),int(points_distance/6.06)):
                points1.append((i,height-i*3.03))
                points1.append((i,i*3.03))

            points = []
            for i in points1:
                points.append((i[0] + current, i[1]))
            current = current + int(width) + int(height / 10)
            return points, current


        elif which_letter == 'Y':
            points1 = []
            for i in range(-int(0.5*0.3*height),int(0.5*0.3*height),int(points_distance/math.sqrt(5))):
                points1.append((i,2*abs(i)))
            points2 = []
            for i in range(0,int(0.7*height),points_distance):
                points2.append((0,-i))
            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((current+int(0.5*0.3*height)+i[0],i[1]+int(0.7*height)))

            current = current + int(0.3*height) +int(height/10)
            return points,current

        elif which_letter == 'Z':
            width = 0.33 * height

            points1 = []
            for i in range(0,int(width),points_distance):
                points1.append((i,height))
                points1.append((i,0))

            points2 = []
            for i in range(0, int(width), int(points_distance / 6.06)):
                points2.append((i, i * 3.03))

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + int(width) + int(height / 10)
            return points, current


#s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#s = 'ABCD'
s = 'HAPPY BIRTHDAY FILIP'
height = 1000
distance_between_points = 20
points = []
current = 0
for i in s:
    print("now writing letter",i)
    if i != ' ':
        letter = generate_letter_point(i, height, current,distance_between_points)
        points = points + letter[0]
        current = int(letter[1])
    else:
        current = current + int(height/5)
x = []
y = []
for i in points:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x,y,5)
plt.axis('equal')
plt.show()

with open('cool.csv', 'w', newline='') as csvfile:
    text = csv.writer(csvfile)
    for i in points:
        text.writerow(i)