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
fruit1 = int(input())

if fruit1 == 1:
    total_cost += 2
    apples += 1

elif fruit1 == 2:
    total_cost += 1
    grapes += 1

elif fruit1 == 3:
    total_cost += 3
    oranges +=1

fruitnex= input("Would you like to buy another piece of fruit? y/n ")

while fruitnex=="y":
    print(f"Welcome, {name}, which fruit would you like to buy? (1, 2, or 3)")
    print(wares[0])
    print(wares[1])
    print(wares[2])
    fruit1 = int(input())

    if fruit1 == 1:
        total_cost += 2
        apples += 1
    elif fruit1 == 2:
        total_cost += 1
        grapes += 1
    elif fruit1 == 3:
        total_cost += 3
        oranges += 1

    fruitnex= input("Would you like to buy another piece of fruit? y/n ")

print (f"Order for {name}")
print (f"{apples} apple(s) at $2 each")
print (f"{grapes} grape(s) at $1 each")
print (f"{oranges} orange(s) at $3 each")
print (f"subtotal: ${total_cost}")
tax= .05 * total_cost
final_cost= tax + total_cost
print( f"tax: ${tax}")
print (f"total: ${final_cost}")