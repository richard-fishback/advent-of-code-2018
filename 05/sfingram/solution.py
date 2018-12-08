def splode(c1: str, c2: str):
    return (c1.lower() == c2.lower()) and \
           ((c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper()))


def react(chain: str):
    polymer = list()
    for c in chain:
        if not polymer or not splode(polymer[-1], c):
            polymer.append(c)
        else:
            polymer.pop()
    return len(polymer)


with open('input.txt') as f:
    chain = next(iter(f)).strip()
print(f'''Part One: {react(chain)}''')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shortest_poly_len = sorted({letter: react(chain.replace(letter, '').replace(letter.upper(), ''))
                            for letter in alphabet}.items(),
                           key=lambda x: x[-1])[0][-1]
print(f'''Part Two: {shortest_poly_len}''')
