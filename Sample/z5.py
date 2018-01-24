def area_triangle(x1, y1, x2, y2, x3, y3):
    a= (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
    return abs(a)

def  foundInBermudatriangle(x1, y1, x2, y2, x3, y3, px, py, bx, by):
    plane, boat = 0,0
    a = area_triangle(x1, y1, x2, y2, x3, y3)

    a1 = area_triangle(px, py, x2, y2, x3, y3)

    a2 = area_triangle(x1, y1, px, py, x3, y3)

    a3 = area_triangle(x1, y1, x2, y2, px, py)

    b1 = area_triangle(bx, by, x2, y2, x3, y3)

    b2 = area_triangle(x1, y1, bx, by, x3, y3)

    b3 = area_triangle(x1, y1, x2, y2, bx, by)

    if (a == 0):
        return 0

    if (a == (a1 + a2 + a3)):
        plane=1
    else:
        plane = 0

    if (a == (b1 + b2 + b3)):
        boat=1
    else:
        boat = 0

    if (plane == 1 and boat == 0):
        return 1

    elif (plane == 0 and boat == 1):
        return 2

    elif (plane == 1 and boat == 1):
        return 3

    elif (plane == 0 and boat == 0):
        return 4
    else:
        return 0