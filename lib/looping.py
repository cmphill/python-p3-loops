#!/usr/bin/env python3

def happy_new_year():
   i = 10
   while i > 0:
       print(i)
       i -= 1
       if i == 0:
           print(f"Happy New Year!")
def square_integers(int_list):
    square_integers = list()
    for int in int_list:
        square_integer = int ** 2
        square_integers.append(square_integer)
    return square_integers
#    int_list = [int ** 2 for int in int_list]
#    return int_list

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")
        else:
            print (i)
