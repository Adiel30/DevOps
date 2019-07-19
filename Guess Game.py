import random
num = random.randint(1,100)
print(num)
print(" This is a gusses game: ")
print("Now Gusse Number ")

guesses = [0]

while True:
    guess = int (input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    break

