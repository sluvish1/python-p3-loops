#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter-=1
    print("Happy New Year!")   
        

def square_integers(int_list):
    int_list_squared = [number**2 for number in int_list]
    return int_list_squared
 
    
def fizzbuzz():
    i=1
    for i <= 100: