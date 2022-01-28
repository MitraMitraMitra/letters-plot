
import matplotlib
import matplotlib.pyplot as plt
import math
import csv
import re

def generate_letter_point(which_letter, height, current, points_distance = 2):

        if which_letter == 'A':
            points1 = []
            increment = points_distance * (height / 5) / math.sqrt(height ** 2 + (height / 5) ** 2)
            x_coordinate = 0
            while 5 * x_coordinate < height:
                points1.append((x_coordinate, 5 * x_coordinate))
                x_coordinate = x_coordinate + increment

            points2 = []
            while -5 * x_coordinate + 2 * height > 0:
                points2.append((x_coordinate, -5 * x_coordinate + 2 * height))
                x_coordinate = x_coordinate + increment

            start_of_line = min(points1, key = lambda x: abs(x[1] - 0.6 * height))
            end_of_line = min(points2, key = lambda x: abs(x[1] - 0.6 * height))

            points3 = []
            i = start_of_line[0]
            while i < end_of_line[0]:
                points3.append((i, 0.6 * height))
                i = i + points_distance

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'B':
            # WIDTH = (0.1 + 0.3 = 0.4) * HEIGHT
            points1 = []
            radius_1 = 0.2 * height
            radius_2 = 0.3 * height
            arc_length = points_distance
            theta_1 = arc_length * 360 / (2 * math.pi * radius_1)
            theta_2 = arc_length * 360 / (2 * math.pi * radius_2)
            i = -90
            while i < 90:
                points1.append((radius_1 * math.cos(i * math.pi / 180) + height/10, radius_1 * math.sin(i * math.pi / 180) +0.8*height))
                i = i + theta_1

            i = -90
            while i < 90:
                points1.append((radius_2 * math.cos(i * math.pi / 180) + height / 10, radius_2 * math.sin(i * math.pi / 180) + 0.3 * height))
                i = i + theta_2

            points2 = []
            i = 0
            while i < height:
                points2.append((0, i))
                i = i + points_distance

            points3 = []
            i = 0
            while i < height / 10:
                points3.append((i, 0))
                points3.append((i, 0.6 * height))
                points3.append((i, height))
                i = i + points_distance

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'C':
            # WIDTH = (2 * 0.2 = 0.4) * HEIGHT
            points1 = []
            radius = height / 5
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            i = 0
            while i < 180:
                points1.append((radius + radius * math.cos(i * math.pi / 180),radius * math.sin(i * math.pi / 180) + height - radius))
                points1.append((radius + radius * math.cos((i + 180)  * math.pi / 180), radius * math.sin((i + 180) * math.pi / 180) + radius))
                i = i + theta

            points2 = []
            i = radius
            while i < height - radius:
                points2.append((0, i))
                i = i + points_distance

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'D':
            # WIDTH = (2 * 0.2 = 0.4) * HEIGHT
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            points2 = []
            radius = 0.3 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            i = -90
            while i < 90:
                points2.append((height / 10 + radius * math.cos(i * math.pi / 180), height / 2 + radius * math.sin(i * math.pi / 180) * 1.667))
                i = i + theta

            points3 = []
            i = 0
            while i < height / 10:
                points3.append((i, height))
                points3.append((i, 0))
                i = i + points_distance

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'E':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, 0))
                points2.append((i, height / 2))
                points2.append((i, height))
                i = i + points_distance


            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current

        elif which_letter == 'F':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, height))
                i = i + points_distance

            points3 = []
            i = 0
            while i < 0.33 * height:
                points3.append((i, 0.68 * height))
                i = i + points_distance

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'G':
            points1 = []
            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            i = 0
            while i < 180:
                points1.append((radius + radius * math.cos(i * math.pi / 180), 0.8 * height + radius * math.sin(i * math.pi / 180)))
                points1.append((radius + radius * math.cos((i + 180) * math.pi / 180), radius + radius * math.sin((i + 180) * math.pi / 180)))
                i = i + theta

            points2 = []
            i = 0.2 * height
            while i < 0.8 * height:
                points2.append((0, i))
                i = i + points_distance

            points3 = []
            i = 0.2 * height
            while i < 0.4 * height:
                points3.append((0.4 * height, i))
                i = i + points_distance

            points4 = []
            i = 0.25 * height
            while i < 0.4 * height:
                points4.append((i, 0.4 * height))
                i = i + points_distance

            points5 = points1 + points2 + points3 + points4
            points = []
            for i in points5:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'H':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                points1.append((0.4 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, height / 2))
                i = i + points_distance

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'I':
            points1 = []
            i = 0
            while i < height:
                points1.append((0.2 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, 0))
                points2.append((i, height))
                i = i + points_distance

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'J':
            points1 = []
            i = height / 6
            while i < height:
                points1.append((0.4 * height, i))
                i = i + points_distance


            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, height))
                i = i + points_distance

            points3 = []
            radius = height / 6
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            i = 180
            while i < 360:
                points3.append((0.4 * height - radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'K':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance


            points2 = []
            i = 0
            while i < height / 20:
                points1.append((i, height / 2))
                i = i + points_distance

            points3 = []
            i = 0

            # WHILE NOT OUT OF BORDERS (0.4 * HEIGHT x HEIGHT)
            while i < 0.35 * height and height / 2 + (0.5 / 0.35) * i < height:
                points3.append((i + height / 20, height / 2 + (0.5 / 0.35) * i))
                points3.append((i + height / 20, height / 2 - (0.5 / 0.35) * i))
                i = i + 0.35 * points_distance / 0.610328


            points5 = points1 + points2 + points3

            points = []
            for i in points5:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'L':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            i = 0
            while i < 0.4 * height:
                i = i + points_distance
                points1.append((i, 0))

            points = []
            for i in points1:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'M':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                points1.append((0.4 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.2 * height:
                points2.append((0.2 * height + i, 0.7 * height + i * 0.3 / 0.2))
                points2.append((0.2 * height - i, 0.7 * height + i * 0.3 / 0.2))
                i = i + points_distance * 0.2 / 0.360555

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'N':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                points1.append((0.4 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, height - 2.5 * i))
                i = i + points_distance / math.sqrt(5)

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0]+current,i[1]))

            current = current + 0.4*height + height / 10
            return points, current


        elif which_letter == 'O':
            points1 = []
            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            i = 0
            while i < 180:
                points1.append((radius + radius * math.cos(i * math.pi / 180), 0.8 * height + radius * math.sin(i * math.pi / 180)))
                points1.append((radius + radius * math.cos((i + 180) * math.pi / 180), radius + radius * math.sin((i + 180) * math.pi / 180)))
                i = i + theta

            points2 = []
            i = 0.2 * height
            while i < 0.8 * height:
                points2.append((0, i))
                points2.append((0.4 * height, i))
                i = i + points_distance

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'P':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.15 * height:
                points2.append((i, height))
                points2.append((i, 0.5 * height))
                i = i + points_distance

            points3 = []
            radius = 0.25 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            i = - 90
            while i < 90:
                points3.append((0.15 * height + radius * math.cos(i * math.pi / 180), 0.5 * height + radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'Q':
            points1 = []
            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            i = 0
            while i < 180:
                points1.append((radius + radius * math.cos(i * math.pi / 180),
                                0.8 * height + radius * math.sin(i * math.pi / 180)))
                points1.append((radius + radius * math.cos((i + 180) * math.pi / 180),
                                radius + radius * math.sin((i + 180) * math.pi / 180)))
                i = i + theta

            points2 = []
            i = 0.2 * height
            while i < 0.8 * height:
                points2.append((0, i))
                points2.append((0.4 * height, i))
                i = i + points_distance

            points3 = []
            i = radius / 2
            while i < radius:
                points3.append((i + radius, - i + radius))
                i = i + points_distance / math.sqrt(2)

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current

        elif which_letter == 'R':
            points1 = []
            i = 0
            while i < height:
                points1.append((0, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.15 * height:
                points2.append((i, height))
                points2.append((i, 0.7 * height))
                i = i + points_distance

            points3 = []
            radius = 0.15 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            i = - 90
            while i < 90:
                points3.append((0.15 * height + radius * math.cos(i * math.pi / 180), 0.7 * height + radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points4 = []
            i = 0
            while i < 0.25 * height:
                points4.append((i + 0.15 * height, 0.7 * height -i * 0.7 / 0.25))
                i = i + 0.25 * points_distance / 0.743303

            points5 = points1 + points2 + points3 + points4
            points = []
            for i in points5:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'S':

            radius = height / 5
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            points1 = []
            i = 0
            while i < 220:
                points1.append((radius + radius * math.cos(i * math.pi / 180), 0.2 * height + 3 * radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points2 = []
            i = -180
            while i < 40:
                points2.append((radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points3 = []
            mini = min(points1, key = lambda item: item[1])
            maxi = max(points2, key = lambda item: item[1])

            d_x = mini[0] - maxi[0]
            d_y = maxi[1] - mini[1]
            ratio = d_y / d_x
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i < maxi[0] - mini[0]:
                points3.append((mini[0] + i, mini[1] - i * ratio))
                i = i + calculated_x_step

            points = []
            points4 = points1 + points2 + points3
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'T':
            points1 = []
            i = 0
            while i < height:
                points1.append((0.2 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, height))
                i = i + points_distance

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'U':
            points1 = []
            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            points2 = []
            i = 180
            while i < 360:
                points2.append((radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points3 = []
            i = 0.2 * height
            while i < height:
                points3.append((0, i))
                points3.append((0.4 * height, i))
                i = i + points_distance

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'V':
            points1 = []
            i = 0
            while i < 0.2 * height and i * math.sqrt(26) < height:
                points1.append((0.2 * height - i, i * math.sqrt(26)))
                points1.append((i + 0.2 * height, i * math.sqrt(26)))
                i = i + points_distance / math.sqrt(26)

            points = []
            for i in points1:
                points.append((i[0] + current, i[1]))

            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'W':
            points1 = []
            calculated_x_step = points_distance / math.sqrt(65)
            i = 0
            while i < 0.125 * height:
                points1.append((0.125 * height + i, 8 * i))
                points1.append((0.125 * height - i, 8 * i))
                points1.append((0.275 * height + i, 8 * i))
                points1.append((0.275 * height - i, 8 * i))
                i = i + calculated_x_step

            points = []
            for i in points1:
                points.append((current + i[0], i[1]))
            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'X':
            center_y = height / 2
            center_x = 0.2 * height
            calculated_x_step = points_distance / 2.69258
            points1 = []
            i = 0
            while i < 0.2 * height:
                points1.append((center_x - i, center_y + i * 2.5))
                points1.append((center_x + i, center_y + i * 2.5))
                points1.append((center_x - i, center_y - i * 2.5))
                points1.append((center_x + i, center_y - i * 2.5))
                i = i + calculated_x_step

            points = []
            for i in points1:
                points.append((current + i[0], i[1]))
            current = current + 0.4 * height + height / 10
            return points, current


        elif which_letter == 'Y':
            points1 = []
            i = 0
            calculated_x_step = points_distance / 1.80278
            while i < 0.2 * height:
                points1.append((0.2 * height + i, 0.65 * height + math.sqrt(3) * i))
                points1.append((0.2 * height - i, 0.65 * height + math.sqrt(3) * i))
                i = i + calculated_x_step

            points2 = []
            i = 0
            while i < 0.65 * height:
                points2.append((0.2 * height, i))
                i = i + points_distance

            points3 = points1 + points2
            points = []
            for i in points3:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current

        elif which_letter == 'Z':
            points1 = []
            calculated_x_step = points_distance / 2.69258
            i = 0
            while i < 0.4 * height:
                points1.append((i, 2.5 * i))
                i = i + calculated_x_step

            i = 0
            while i < 0.4 * height:
                points1.append((i, height))
                points1.append((i, 0))
                i = i + points_distance

            points = []
            for i in points1:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current

        elif which_letter == '-':
            points1 = []
            i = 0
            while i < 0.4 * height:
                points1.append((i, height / 2))
                i = i + points_distance

            points = [(current + i[0], i[1]) for i in points1]

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '1':
            points1 = []
            i = 0
            while i < 0.4 * height:
                points1.append((i, 0))
                i = i + points_distance

            points2 = []
            ratio = 3 / 2
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i < 0.2 * height:
                points2.append((i, 0.7 * height + i * 3/2))
                i = i + calculated_x_step

            points3 = []
            i = 0
            while i < height:
                points3.append((0.2 * height, i))
                i = i + points_distance

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '2':
            radius = height / 5
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)

            points1 = []
            i = -20
            while i < 180:
                points1.append((radius + radius * math.cos(i * math.pi / 180), 0.2 * height + 3 * radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            i = 0
            points2 = []
            ratio = 1.88586
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            #while i < height - 0.2 * height - math.cos(70 * math.pi / 180) * 0.2 * height:
            while ratio * i < height - 0.2 * height - math.cos(70 * math.pi / 180) * 0.2 * height:
                points2.append((i, ratio * i))
                i = i + calculated_x_step

            points3 = []
            i = 0
            while i < 0.4 * height:
                points3.append((i, 0))
                i = i + points_distance

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10
            return points, current

        elif which_letter == '3':
            points1 = []
            i = 0
            while i < 0.4 * height:
                points1.append((i, height))
                i = i + points_distance

            points2 = []
            ratio = 4/3
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i * ratio < 0.4 * height:
                points2.append((0.1 * height + i, 0.6 * height + i * ratio))
                i = i + calculated_x_step

            radius = 0.3 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            points3 = []
            i = -90
            while i < 90:
                points3.append((0.1 * height + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points4 = points1 + points2 + points3
            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '4':
            points1 = []
            i = 0
            while i < 0.8 * height:
                points1.append((0.23 * height, i))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points2.append((i, 0.6 * height))
                i = i + points_distance

            points3 = []
            ratio = 4 / 2.4
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i * ratio < 0.4 * height:
                points2.append((i, 0.6 * height + i * ratio))
                i = i + calculated_x_step

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '5':
            points1 = []
            i = 0
            while i < 0.4 * height:
                points1.append((i, height))
                i = i + points_distance

            points2 = []
            i = 0
            while i < 0.4 * height:
                points1.append((0, 0.6 * height + i))
                i = i + points_distance

            points3 = []
            i = 0
            while i < 0.1 * height:
                points1.append((i, 0.6 * height))
                i = i + points_distance

            radius = 0.3 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            points4 = []
            i = 90
            while 0.1 * height + radius * math.cos((i - theta) * math.pi / 180) > 0:
                points4.append((0.1 * height + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                i = i - theta

            points4 = points1 + points2 + points3 + points4

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '6':
            points1 = []
            i = 0
            while i < 0.6 * height:
                points1.append((0, 0.2 * height + i))
                i = i + points_distance

            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            points2 = []
            i = 0
            while i < 180:
                points2.append((radius + radius * math.cos(i * math.pi / 180), radius - radius * math.sin(i * math.pi / 180)))
                points2.append((radius + radius * math.cos(i * math.pi / 180), radius + 0.1 * height + radius * math.sin(i * math.pi / 180)))
                points2.append((radius + radius * math.cos(i * math.pi / 180), 0.8 * height + radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points3 = []
            i = 0
            while i < 0.1 * height:
                points3.append((0.4 * height, 0.2 * height + i))
                i = i + points_distance

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '7':
            points1 = []
            i = 0.03 * height
            while i < 0.4 * height:
                points1.append((i, height))
                i = i + points_distance

            points2 = []
            ratio = 5
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i * ratio < height:
                points2.append((0.2 * height + i, i * ratio))
                i = i + calculated_x_step

            points3 = []
            i = 0
            while 0.9 * height + i * ratio < height:
                points3.append((i, 0.9 * height + i * ratio))
                i = i + calculated_x_step

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '8':
            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            points1 = []
            i = -225
            while i < 45:
                points1.append((radius + radius * math.cos(i * math.pi / 180), radius + radius * math.sin(i * math.pi / 180)))
                points1.append((radius + radius * math.cos(i * math.pi / 180), height - radius - radius * math.sin(i * math.pi / 180)))
                i = i + theta

            points2 = []
            ratio = 1.12132
            calculated_x_step = points_distance / math.sqrt(1 + ratio ** 2)
            i = 0
            while i * ratio < 0.6 * height - 0.2 * math.sqrt(2) * height:
                points2.append((((0.4 - 0.2 * math.sqrt(2)) / 2) * height + i, (0.2 + 0.2 * math.sqrt(2) / 2) * height + i * ratio))
                points2.append((((0.4 - 0.2 * math.sqrt(2)) / 2 + 0.2 * math.sqrt(2)) * height - i, (0.2 + 0.2 * math.sqrt(2) / 2) * height + i * ratio))
                i = i + calculated_x_step

            points3 = points1 + points2

            points = []
            for i in points3:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

        elif which_letter == '9':
            points1 = []
            i = 0
            while i < 0.6 * height:
                points1.append((0.4 * height, 0.2 * height + i))
                i = i + points_distance

            radius = 0.2 * height
            arc_length = points_distance
            theta = arc_length * 360 / (2 * math.pi * radius)
            points2 = []
            i = 0
            while i < 180:
                points2.append((radius + radius * math.cos(i * math.pi / 180), 0.8 * height + radius * math.sin(i * math.pi / 180)))
                points2.append((radius + radius * math.cos(i * math.pi / 180), 0.7 * height - radius * math.sin(i * math.pi / 180)))
                points2.append((radius + radius * math.cos(i * math.pi / 180), radius - radius * math.sin(i * math.pi / 180)))

                i = i + theta

            points3 = []
            i = 0
            while i < 0.1 * height:
                points3.append((0, 0.7 * height + i))
                i = i + points_distance

            points4 = points1 + points2 + points3

            points = []
            for i in points4:
                points.append((current + i[0], i[1]))

            current = current + 0.4 * height + height / 10

            return points, current

def write_letter(string, height, distance_between_points, current, filename = None):
    points = []
    for i in s:
        if re.match('[0-9A-Za-z-]', i) != None:
            if i.islower():
                i = i.upper()
            if i == '0':
                i = 'o'
            letter = generate_letter_point(i, height, current, distance_between_points)
            points = points + letter[0]
            current = letter[1]
        elif i == '\n':
            new_points = []
            for j in points:
                new_points.append((j[0], j[1] + height + height / 10))
            current = 0
            points = new_points
        else:
            current = current + 0.4 * height
    return points

    if filename != None:
        with open(filename + '.csv', 'w', newline = '') as csvfile:
            text = csv.writer(csvfile)
            for i in points:
                text.writerow(i)

s = 'aid?!F'
height = 25
distance_between_points = 0.2
current = 0

p = write_letter(s, height, distance_between_points, current, filename = None)

x = []
y = []
for i in p:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x, y, 5)
plt.axis('equal')
plt.show()