import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def point_position(circle_x, circle_y, radius, point_x, point_y):
    dist = distance(circle_x, circle_y, point_x, point_y)
    if dist == radius:
        return 0
    elif dist < radius:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Usage: task2.py circle_file points_file")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]


    with open(circle_file, 'r') as f:
        circle_x, circle_y = map(int, f.readline().split())
        radius = int(f.readline())


    with open(points_file, 'r') as f:
        for line in f:
            point_x, point_y = map(int, line.split())
            pos = point_position(circle_x, circle_y, radius, point_x, point_y)
            print(pos)

if __name__ == "__main__":
    main()