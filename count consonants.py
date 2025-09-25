vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
n = input("Enter a word: ")
count = 0
for i in n:
    if i not in vowels:
        count += 1
print("Number of conconants in the word:", count)
    
