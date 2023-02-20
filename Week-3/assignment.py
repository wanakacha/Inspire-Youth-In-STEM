#create an empty list of favourite musicians
#using for loop add five new musicians
#copy the list to a new list called celebs
#sort the list
#pop out two celebs from the list
#count the remaining celebrities in the list
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