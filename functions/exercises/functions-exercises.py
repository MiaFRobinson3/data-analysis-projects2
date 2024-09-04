# Part 1 A -- Make a Line
def make_line(size):
    line = ""
    for i in range(size):
        line += "#"
    return line
print(make_line(5))

# Part 1 B -- Make a Square
def make_square(size):
    square = ""
    for i in range(size):
        square += (make_line(size) + "\n")
    return square
print(make_square(5))

# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle += (make_line(width) + "\n")
    return rectangle
print(make_rectangle(5, 3))

# Rewrite make_square using make_rectangle 
def make_square(size):
    square = ""
    for i in range(size):
        square += (make_rectangle(size, size) + "\n")
    return square
print(make_square(5))  

# Part 2 A -- Make a Stairs
def make_downward_stairs(height): #define function
    stairs = ""                   # initialize empty string variable called stairs
    for i in range(height):       # for each iteration(I) of height within the range
        stairs += (make_line(i +1) + "\n")    #update the stairs variable with the value returned by calling the make_line function, adding 1 to it, and a line break
    return stairs                             # return the result
print(make_downward_stairs(5))                # call the function using 5 as the argument and print the result 

# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChars):
    spaces = " "
    chars = "#"
    return (spaces + chars)
print(make_space_line(3, 5))
    
# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line(height -i -1, 2 * i +1) + "\n")
    return triangle 
print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = ""
    triangle = make_isosceles_triangle(height)
    diamond += triangle[:-1]
    for i in range(len(triangle) -1, -1, -1):
        diamond += triangle[i]
    return diamond
print(make_diamond(5))


# Class Demo 9/3
def square_number(x):
    result = x * x 
    return result
result = square_number(4)
print(result)

def add_numbers_together(num):  #function body-function name and parameter
    total = 0                   #function body-initializes the variable called total and sets it to zero
    while num < 100:            #function body-begins a while loop that continues until the value of num is 100 or greater
        total += num            #function body-repeatedly adds the current value of num to the total
        num += 1                #function body-after each addition, value of num increases by 1
    return total                #the result that the funtionc returns
result = add_numbers_together(4)
print(result)
def add_numbers(x,y):
    result = x + y
    return result
result = add_numbers(4, 5)
print(result)