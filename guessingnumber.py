startUpMessage = "Your guessing game begins !!"
for char in startUpMessage:
        print(char, end=" ")

print("\n")
print("your guessing game begings")
user_input = int(input("enter the between 1-100 :"))
wining_number = 25
gameOver = False
numberOfGuesses = 1
while numberOfGuesses != 3:
    numberOfGuesses += 1
    if (user_input <= 25) and (user_input >= 20) :
        print(f"your guess is correct! {user_input}")
        break
    elif ((user_input >= 1) and (user_input <= 20)) or ((user_input >= 25) and (user_input <= 100)):
        print(f"your guess number {user_input} out of range")
        user_input = int(input("Guess the number again : "))
        continue
print("sorry your guessing limit is over ")
print(numberOfGuesses)