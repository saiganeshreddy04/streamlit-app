vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
n = input("Enter a word: ")
count = 0
for i in n:
    if i in vowels:
        count += 1
print("Number of vowels in the word:", count)
