import random
lower = int(input("Enter starting range:- "))
upper = int(input("Enter ending range:- "))
user=int(input("how many chances u need ? -> "))

x = random.randint(lower, upper)
print(f"\n\tYou've only {user} chances to guess the integer!\n")

count = 0
while count <user:
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print(f"Congratulations you did it in {count} try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if count >=user:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
