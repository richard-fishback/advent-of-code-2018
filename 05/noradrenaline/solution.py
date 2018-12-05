

def aspirational_collapse(v):
    # a single collapse operation
    m = '  '+v
    n = v+'  '
    v = ' '+v+' '
    return ''.join([c for i,c in enumerate(v) if not (m[i]!=v[i] and m[i].lower()==v[i].lower()) and not (n[i]!=v[i] and n[i].lower()==v[i].lower())]).strip()
    # shoot, this doesn't properly handle abBbA

def collapse(v):
    # fucking just iterate then.
    i = 0
    new_v = ''
    while i <= len(v)-1:
        if i==len(v)-1 or not (v[i]!=v[i+1] and v[i].lower()==v[i+1].lower()):
            # this letter should be included
            new_v = new_v+v[i]
            i+=1
        else:
            # this means that we have found a match, so skip adding this and the next letter
            i+=2
    return new_v

    


def recursive_collapse(v):
    c = collapse(v)
    if c == v:
        return v
    else:
        return recursive_collapse(c)

#print("part 1: "+str(len(recursive_collapse(open('input.txt').readline()))))
# stupid recursive collapse exceeds allowed recursion depth (it works for test cases now)

a = open('input.txt').readline().strip()
def while_collapse(a):
    b = collapse(a)
    while a != b:
        a = b
        b = collapse(b)
    return b

print("part 1: " + str(len(while_collapse(a))))

def remove(letter,a):
    letter = letter.lower()
    return ''.join([c for c in a if c.lower() != letter])

shortest = len(a)
for char in set(a.lower()):
    this_len = len(while_collapse(remove(char,a)))
    if this_len < shortest:
        shortest = this_len

print("part 2: " + str(shortest))

