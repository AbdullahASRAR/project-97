import random

number= random.randint(1,9) 
print(number)
chances=0
print("Enter a number from (1 to 9) to guess it:")
while chances < 5:
 guess = int(input("Enter your guess:- "))
 if guess == number:
    print("Congratulation YOU WON!!!")
    break
 elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

 else:
        print("Your guess was too high: Guess a number lower than", guess)

 chances += 1

if not chances < 5:
     print("YOU LOSE!!! The number is", number)
      