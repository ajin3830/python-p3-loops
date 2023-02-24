#!/usr/bin/env python3
import ipdb
def happy_new_year():
    # code goes here!
    # ipdb.set_trace()
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')
# happy_new_year()

# another way to do this:
# def happy_new_year():
#     for i in range(10, 0, -1):
#         print(i)

def square_integers(int_list):
    return [i ** 2 for i in int_list]

# to return squared ints for [1, 2, 3, etc] and [-1, -2, -3, etc]
# def square_integers(int_list):
#     for int in int_list:
#         if int > 0:
#             print(int ** 2)
#         elif int < 0:
#             print(-abs(int ** 2))

def fizzbuzz():
    # code goes here!
    # use modulo !!
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        # here we can't just omit else and print
        else:    
            print(i) 
        # make sure to increment outside else
        i += 1

# shorter version
# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 5 ==0:
#             print("Buzz")
#         elif i % 3 ==0:
#             print("Fizz")
#         else:
#             print(i)

# other ways to write this using 'not', but I don't get it
# def fizzbuzz():
#     # code goes here!
#     i = 1
#     while i <= 100:
#         if not i % 15:
#             print('FizzBuzz')
#         elif not i % 3:
#             print('Fizz')
#         elif not i % 5:
#             print('Buzz')
#         else:
#           print(i) 
#         i += 1


# def fizzbuzz():
#     for i in range(1, 101):
#         if not i % 15:
#             print("FizzBuzz")
#         elif not i % 5:
#             print("Buzz")
#         elif not i % 3:
#             print("Fizz")
#         else:
#             print(i) 