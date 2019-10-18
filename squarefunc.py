import turtle

# myturtle = turtle.Turtle()
# myturtle.speed(0)
#
# def square(direc,angle):
#     for j in range(4):
#         myturtle.forward(direc)
#         myturtle.right(angle)
#         # myturtle.forward(direc)
#         # myturtle.right(angle)
#         # myturtle.forward(direc)
#         # myturtle.right(angle)
#         # myturtle.forward(direc)
#
# for i in range(100):
#     square(200,90)
#     myturtle.right(11)
#
#
# Greeting = 'Hi how are you doing, it is very nice to meet you.'
# print(Greeting[0:-1:2])
# print(Greeting[::-1])
# print(Greeting.find('v'))
# print(Greeting[Greeting.find('i'):Greeting.find('i',10)])
# data = Greeting.split('i')
# data.append('Rajat & Family')
# data.append(6)
# print(data)

# phonebook = {'Rajat': 9713482642, 'Family': 7415812904}
# print (phonebook['Family'])

def sum_two(a,b):
    output = a+b
    return output

print (sum_two(10,15))

def square_number(a):
    return a**2

print (square_number(25))

def is_even(num):
    text = 'even'
    if num%2 == 0:
        return text
    else:
        text = 'odd'
        return text

print (is_even(12))

def strlen(st):
    return len(st)

print (strlen('Narayan Batham'))

def last_letter(name):
    return name[-1]

print (last_letter("Rajat Batham"))

def bigger_guy(a, b, c, d):
    return max(a, b, c, d)

print (bigger_guy(12, 11, 20, 21))

numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squaredList = []

for i in numberslist:
    squaredList.append(i**2)

print (squaredList)