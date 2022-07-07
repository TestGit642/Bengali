def ছাপা(data):
    print(data)


def যোগ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
def সংযোজন(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def বিয়োগ(x, y):
    result =x - y
    return result
    # print(বিয়োগ(1, 2))



def অক্ষম(x, y):
    result = x - y
    return result
# print(অক্ষম(126624654.2,2444646))

def গুণ(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul

def বিভক্তকরা(x, y):
    result = x / y
    return result

def বিভাগ(x, y):
    result = x / y
    return result
#string module

def বিপরীতসত্যা(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


def প্রথমবড়অক্ষর(str):
    for i in range(0, len(str)):

        if (str[i].istitle()):
            return str[i]

    return 0
def বিপরীতঅক্ষর(a):
    return a[::-1]
# function which return reverse of a string
def  অনেকশব্দ(a):
    max_frequency = {}
    for i in a:
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1
    my_result = max(max_frequency, key=max_frequency.get)
    return my_result

# Input Function

def নিবেস(data):  # input
    a = input(data)
    return a

#SORTING
#bubble sort
# Swap the elements to arrange in order
def সাজান(list):
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp
    return list
#bubble sort


#merege sort
def মার্জসাজান(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = মার্জসাজান(left_list)
    right_list =মার্জসাজান(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res
#merge sort


#insertion sort
def সন্নিবেশবাছাই(list1):
    # Outer loop to traverse through 1 to len(list1)
    for i in range(1, len(list1)):

        value = list1[i]

        # Move elements of list1[0..i-1], that are
        # greater than value, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1


#selection sort
def নির্বাচনবাছাই(array):
    n = len(array)
    for i in range(n):
        # Initially, assume the first element of the unsorted part as the minimum.
        minimum = i

        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                # Update position of minimum element if a smaller element is found.
                minimum = j

        # Swap the minimum element with the first element of the unsorted part.
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array
   #selection sort


#linear search
def খুঁজেপাবে(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1

#binary search
def দ্রুতঅনুসন্ধান(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


#jump search
import math
def মাধ্যমেঅনুসন্ধানকরুন(lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1


#fibonacci search
def ফিবোনাচিঅনুসন্ধান(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        return index + 1;
    return -1

#interpolation search
def সম্প্রসারণ(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1
#platform and os start
from os import *
from platform import *
def ওজন(a):
    return path.getsize(a)  # file size in byte

def কিখবর(a):
    return listdir(a)

def আমিজানিনা(a):
    return help(a)


কোনস্থানে= getcwd()  # current directory o
অপারেটর=processor()  # computer processor name p
অপারেটরআপগ্রেড=architecture()  # computer bit 32/64 p
কম্পিউটারনাম =machine()  # amd64 p
কম্পিউটারনাম =node()  # computer name p
অ্যাডমিননামপরিবর্তন=platform()  # osname p

#platform and os complete




#other start
def মিথ্যা():
    return False
def সত্য():
    return True

#date and time function
from datetime import datetime
now=datetime.now()
def সম্পূর্ণতারিখ():
    return datetime.isoformat(now)
তারিখ=datetime.today()
পুরোবছর=now.strftime("%A %m %Y")
বারোবছর=now.strftime("%a %m %y")
সময১২=now.strftime("%I %p %S")
সময২৪=now.strftime("%H:%M:%S")
#date and time functions complete




#lcm
def লাসাগনা(a, b):
    i = 1
    if a > b:
        c = a
        d = b
    else:
        c = b
        d = a
    while True:
        if ((c * i) / d).is_integer():
            return c * i
        i += 1;

#HCF
def গসাগু(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

#other math module
import math
পাই=math.pi
বর্গমূল=math.sqrt
গসাগু =math.gcd
লাসাগনা=math.lcm
ফ্যাক্টরিয়াল=math.factorial
রাউন্ডআপ=math.ceil
রাউন্ডকম=math.floor
দশমিকবিন্দু=math.modf
দশমিক=math.trunc

####################turtle module start########################
#ghanta function
import turtle
import datetime
def ঘড়ি():
    currentDT = datetime.datetime.now()
    screen=turtle.Screen()
    trtl=turtle.Turtle()
    screen.setup(620,620)
    screen.bgcolor('black')
    clr=['red','green','blue','yellow','purple']
    trtl.pensize(4)
    trtl.shape('turtle')
    trtl.penup()
    trtl.pencolor('red')
    m=0
    for i in range(12):
          m=m+1
          trtl.penup()
          trtl.setheading(-30*i+60)
          trtl.forward(150)
          trtl.pendown()
          trtl.forward(25)
          trtl.penup()
          trtl.forward(20)
          trtl.write(str(m),align="center",font=("Arial", 12, "normal"))
          if m==12:
            m=0
          trtl.home()
    trtl.home()
    trtl.setpos(0,-250)
    trtl.pendown()
    trtl.pensize(10)
    trtl.pencolor('blue')
    trtl.circle(250)
    trtl.penup()
    trtl.setpos(150,-270)
    trtl.pendown()
    trtl.pencolor('olive')
    trtl.write((str(currentDT)),font=("Arial", 22, "normal"))
    trtl.ht()
    turtle.done()
#ঘড়ি()

#animal function
import turtle as t
def কুকুর():
    t.screensize(500, 500)
    # 【 head outline 】
    t.pensize(5)
    t.home()
    t.seth(0)
    t.pd()  # pendown
    t.color('black')
    t.circle(20, 80)  # 0
    t.circle(200, 30)  # 1
    t.circle(30, 60)  # 2
    t.circle(200, 29.5)  # 3
    t.color('black')
    t.circle(20, 60)  # 4
    t.circle(-150, 22)  # 5
    t.circle(-50, 10)  # 6
    t.circle(50, 70)  # 7
    #  determine the approximate position of the nose t.xcor and t. ycor the position of the tortoise at the beginning
    x_nose = t.xcor()
    y_nose = t.ycor()
    t.circle(30, 62)  # 8
    t.circle(200, 15)  # 9
    # 【 nose 】
    t.pu()  # penup
    t.goto(x_nose, y_nose + 25)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 eye 】
    t.pu()
    t.goto(x_nose + 48, y_nose + 55)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 ear 】
    t.pu()
    t.color('#444444')
    t.goto(x_nose + 100, y_nose + 110)
    t.seth(182)
    t.pd()
    t.circle(15, 45)
    t.color('black')
    t.circle(10, 15)
    t.circle(90, 70)
    t.circle(25, 110)
    t.rt(4)
    t.circle(90, 70)
    t.circle(10, 15)
    t.color('#444444')
    t.circle(15, 45)
    # 【 body 】
    t.pu()
    t.color('black')
    t.goto(x_nose + 90, y_nose - 30)
    t.seth(-130)
    t.pd()
    t.circle(250, 28)
    t.circle(10, 140)
    t.circle(-250, 25)
    t.circle(-200, 25)
    t.circle(-50, 85)
    t.circle(8, 145)
    t.circle(90, 45)
    t.circle(550, 5)
    # 【 tail 】
    t.seth(0)
    t.circle(60, 85)
    t.circle(40, 65)
    t.circle(40, 60)
    t.lt(150)  # left
    t.circle(-40, 90)
    t.circle(-25, 100)
    t.lt(5)
    t.fd(20)
    t.circle(10, 60)
    # 【 back 】
    t.rt(80)  # right
    t.circle(200, 35)
    # 【 collar 】
    t.pensize(20)
    t.color('#F03C3F')
    t.lt(10)
    t.circle(-200, 25)
    # 【 love bell 】
    t.pu()
    t.fd(18)
    t.lt(90)
    t.fd(18)
    t.pensize(6)
    t.seth(35)  # setheading
    t.color('#FDAF17')
    t.begin_fill()
    t.lt(135)
    t.fd(6)
    t.right(180)  # brush turn around
    t.circle(6, -180)
    t.backward(8)
    t.right(90)
    t.forward(6)
    t.circle(-6, 180)
    t.fd(15)
    t.end_fill()
    # 【 front calf 】
    t.pensize(5)
    t.pu()
    t.color('black')
    t.goto(x_nose + 100, y_nose - 125)
    t.pd()
    t.seth(-50)
    t.fd(25)
    t.circle(10, 150)
    t.fd(25)
    # 【 posterior calf 】
    t.pensize(4)
    t.pu()
    t.goto(x_nose + 314, y_nose - 125)
    t.pd()
    t.seth(-95)
    t.fd(25)
    t.circle(-5, 150)
    t.fd(2)
    t.hideturtle()
    t.done()
#কুকুর()

def পান্ডা():
    pen = turtle.Turtle()

    # Defining method to draw a colored circle
    # with a dynamic radius
    def ring(col, rad):
        # Set the fill
        pen.fillcolor(col)

        # Start filling the color
        pen.begin_fill()

        # Draw a circle
        pen.circle(rad)

        # Ending the filling of the color
        pen.end_fill()

    ##########################Main Section#############################

    # pen.up			 --> move turtle to air
    # pen.down		 --> move turtle to ground
    # pen.setpos		 --> move turtle to given position
    # ring(color, radius) --> draw a ring of specified color and radius
    ###################################################################

    ##### Draw ears #####
    # Draw first ear
    pen.up()
    pen.setpos(-35, 95)
    pen.down
    ring('black', 15)

    # Draw second ear
    pen.up()
    pen.setpos(35, 95)
    pen.down()
    ring('black', 15)

    ##### Draw face #####
    pen.up()
    pen.setpos(0, 35)
    pen.down()
    ring('white', 40)

    ##### Draw eyes black #####

    # Draw first eye
    pen.up()
    pen.setpos(-18, 75)
    pen.down
    ring('black', 8)

    # Draw second eye
    pen.up()
    pen.setpos(18, 75)
    pen.down()
    ring('black', 8)

    ##### Draw eyes white #####

    # Draw first eye
    pen.up()
    pen.setpos(-18, 77)
    pen.down()
    ring('white', 4)

    # Draw second eye
    pen.up()
    pen.setpos(18, 77)
    pen.down()
    ring('white', 4)

    ##### Draw nose #####
    pen.up()
    pen.setpos(0, 55)
    pen.down
    ring('black', 5)

    ##### Draw mouth #####
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.right(90)
    pen.circle(5, 180)
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.left(360)
    pen.circle(5, -180)
    pen.hideturtle()
    turtle.done()
#পান্ডা()


#rainbow
def রংধনু():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)
    turtle.done()

# Python program to draw square
# using Turtle Programming
def আয়তক্ষেত্র():
    skk = turtle.Turtle()

    for i in range(4):
        skk.forward(50)
        skk.right(90)

    turtle.done()

# Python program to draw star
# using Turtle Programming
def তারা():
    star = turtle.Turtle()

    star.right(75)
    star.forward(100)

    for i in range(4):
        star.right(144)
        star.forward(100)

    turtle.done()


# Python program to draw hexagon
# using Turtle Programming
def ষড়ভুজ():
    polygon = turtle.Turtle()

    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

    turtle.done()

#
# import for turtle module
def অষ্টভুজ():
    # making a workScreen
    ws = turtle.Screen()

    # defining a turtle instance
    geekyTurtle = turtle.Turtle()

    # iterating the loop 8 times
    for i in range(8):
        # moving turtle 100 units forward
        geekyTurtle.forward(100)

        # turning turtle 45 degrees so
        # as to make perfect angle for an octagon
        geekyTurtle.left(45)
    turtle.done()


# draw any polygon in turtle
def বহুভুজ():
# creating turtle pen
  t = turtle.Turtle()

# taking input for the no of the sides of the polygon
  n = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
  l = int(input("Enter the length of the sides of the polygon : "))


  for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
    turtle.done()

# turtle library
#This to make turtle object
#tess=turtle.Turtle()

# self defined function to print coordinate
def সংযোগ():
    def buttonclick(x,y):
        print("ଆପଣ ଏହି ସ୍ଥାନରେ କ୍ଲିକ୍ କରିଛନ୍ତି ({0},{1})".format(x,y))

    #onscreen function to send coordinate
    turtle.onscreenclick(buttonclick,1)
    turtle.listen() # listen to incoming connections
    turtle.speed(10) # set the speed
    turtle.done() # hold the screen
#turtle complete

#help module
def সাহায্য(a):
    return help(a)


বড়হাতেরঅক্ষর=str.capitalize






































