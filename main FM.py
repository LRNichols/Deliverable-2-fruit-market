print ("Welcome to the GC Fruit Market!")
name= input("What is your name?  ")

wares= [str("1. Apple  $2"),str("2. Grape  $1"),str("3. Orange  $3")]

total_cost=0
apples=0
oranges=0
grapes=0


print(f"Welcome, {name}, which fruit would you like to buy? (1, 2, or 3)")
print(wares[0])
print(wares[1])
print(wares[2])
fruit1 = input()

if fruit1 == 1:
    total_cost += 2
    apples += 1

elif fruit1 == 2:
    total_cost += 1
    grapes += 1

elif fruit1 == 3:
    total_cost += 3
    oranges +=3

fruitnex= input("Would you like to buy another piece of fruit? y/n")

while fruitnex=="y":
    print(f"Welcome, {name}, which fruit would you like to buy? (1, 2, or 3)")
    print(wares[0])
    print(wares[1])
    print(wares[2])
    fruit1 = input()

    if fruit1 == 1:
        total_cost += 2
        apples += 1
    elif fruit1 == 2:
        total_cost += 1
        grapes += 1
    elif fruit1 == 3:
        total_cost += 3
        oranges += 1

fruitnex= input("Would you like to buy another piece of fruit? y/n")