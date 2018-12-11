from string import ascii_lowercase

def react_polymer(polymer):
    reduced = []
    for unit in polymer:
        if not reduced:
            reduced.append(unit)
        else:
            tail = reduced.pop()
            if abs(ord(tail) - ord(unit)) != 32:
                reduced.append(tail)
                reduced.append(unit)
    return len(reduced)

if __name__ == '__main__':
    polymer = [line.strip() for line in open('input.txt')][0]
    print('solution 1:', react_polymer(polymer))
    print('solution 2:', min({letter:react_polymer(polymer.replace(letter,'').replace(letter.upper(),'')) for letter in list(ascii_lowercase)}.values()))
