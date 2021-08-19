index = 4
while index > -1:
    letter = 'fruit'[index]
    print(letter)
    index = index - 1

#or

for letter in "fruit"[::-1]:
    print(letter)

print(len('fruit'))