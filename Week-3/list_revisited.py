#!/usr/bin/env python3

#This is a single line comment
#Python program to illustrate lists
#Name:Faith wanakacha
#Email:faithkhayanga05@gmail.com
#Date:20th Feb 2023
#File:list_revisited.py


myFavouriteFruits=["apple","mangoes","pineapple","guavas","bananas","watermelon"]
my_favourite_fruits=["apple,mango","pineapple","guavas","bananas","watermelon"]
for fruit in my_favourite_fruits:
    print(fruit)
print(len(my_favourite_fruits)) 
friends=["leshan","lynne","edel","staicy","aguko","regina"]
print(friends)
friends[4]="blue"   
print(friends)


new_friends = friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)
