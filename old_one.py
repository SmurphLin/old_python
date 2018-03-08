l = [
     [True, True, False],
     [False, False, True],
     [True, False, False]
    ]

found = False

n = 10
n = str(n)
one = n[0]
one = int(one)
two = n[1]
two = int(two)


def largestNumber(n):
    value = 0
    while True:
        if n == 1:
            value = value + 9
            break
        else:
            while n > 1:
                value += 9*10**(n-1)
                n -= 1
    return value

print largestNumber(4)


# n children , m candy, maximize candy eaten but must be able to eat equal amounts

# i.e candies(n,m) = 9
def candies(n, m):
    leftover = m%n
    return m-leftover

print candies(6,10)
print 16*11

def seatsInTheater(nCols, nRows, col, row):
   the_col = nCols - (col -1)
   the_row = nRows - (row)
   return the_col*the_row

print seatsInTheater(16,11,5,3)

def maxMultiple(divisor, bound):
    N = bound
    if N%divisor == 0:
        return N
    else:
        return maxMultiple(divisor,(bound-1))

print maxMultiple(3,5)


def circleOfNumbers(n, firstNumber):
    number_circle = [i for i in range(n)]


points = [
            [1, 1], [3, 1], [3, 2], [3, 3],
            [1, 3], [2, 5], [1, 5], [-1, -1],
            [-1, -2], [-2, -3], [-4, -4]
         ]

"""this works for finding max y points"""
def point_sort(points):
    max_y = 0
    min_y = 0
    max_y_points = []
    min_y_points = []

    k = 1
    while True:
        for i in range(len(points)):
            if points[i][k] > max_y:
                max_y = points[i][k]
                max_point = points[i]
        max_y_points.append(max_point)
        for i in range(len(points)):
            if points[i][k] == max_y and points[i] != max_point:
                max_y_points.append(points[i])
        break


    return max_y_points


def min_points(points):
    min_y_points = []

    k = 1
    j= 0
    while True:
        hold = points[j][k]
        for i in range(len(points)):
            if points[i][k] < hold:
                hold = points[i][k]
                min_point = points[i]
        min_y_points.append(min_point)
        break
    return min_y_points



def circleOfNumbers(n, firstNumber):
    circle = [i for i in range(n)]

    stopping_point = int(n/2)
    if firstNumber + stopping_point < len(circle):
        return firstNumber + stopping_point
    elif firstNumber + stopping_point >= len(circle):
        i = 0
        while i < firstNumber + stopping_point - len(circle):
            i += 1
        return i

print "\n"
print circleOfNumbers(4,0)
l = [1,2,3]
print len(l)


