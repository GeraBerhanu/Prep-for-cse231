def print_lyrics():
    print('Im a lumberjack, and Im okay.')
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

print(" poggers" * 4 + '.')

print_lyrics()


def print_twice(x):
    print(x)
    print(x)


print_twice('pop')

def bean_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


bean_twice('poggers ', 'poggies')

print("             " + "poggers")

def right_justify(pog):
    x = 70 - len(pog)
    y = " " * x
    print(y + pog)
