n = list(map(int, input("Enter the numbers: ").split(' ')))
even_position = []
odd_position = []
for i in range(len(n)):
    if i % 2 == 0:
        even_position.append(n[i])
    else:
        odd_position.append(n[i])
print("Even position elements:", even_position)
print("Odd position elements:", odd_position)
