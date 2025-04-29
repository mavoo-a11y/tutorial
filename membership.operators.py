# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"Good job! {letter} is in the word")
# else:
#     print(f"{letter} is not in the word")

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} is not in the word")
else:
    print(f"Good job! {letter} is in the word")