#!/usr/bin/env python3

#This is a single line comment
#Python program to illustrate lists
#Name:Faith wanakacha
#Email:faithkhayanga05@gmail.com
#Date:17th Feb 2023
#File:list.py
















names=["faith", "mary", "valentine", "happiness", "leshan",]
print(names)
print(names[0])
print(names[0:3])
fruits=["berries", "oranges", "bananas", "mangoes", "pineapples", "apple", "watermelon",]
print(fruits[0:-1])
print(fruits[0:3])
print([3])
print("my favourite fruit is",fruits[5] .upper())
#adding two lists
vegetables=["kales", "spinach", "cabbage", "managu","carrots", "broccoli",]
stationery=["pens", "ink", "paper", "glue", "ruler",]
shoppings=vegetables + stationery
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)    
print("my name is " + names[4]+ "and my favourite fruit is" + fruits[3] )