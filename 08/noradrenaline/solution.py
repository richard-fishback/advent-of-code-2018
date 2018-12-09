# oh jeez, this one is trickier.

inp = [int(x) for x in open('input.txt').readline().split()]
test_inp = [int(x) for x in open('sample_input.txt').readline().split()]

def build_nodes(inputlist,start,node_id,parent):
    this_node = {}
    this_node['id'] = node_id
    this_node['parent'] = parent
    this_node['start'] = start
    this_node['meta_num'] = inputlist[start+1]
    this_node['child_num'] = inputlist[start]
    if inputlist[start]==0:
        this_node['children'] = []
        this_node['end'] = start+2+inputlist[start+1] # this is actually the start of the next one 
        this_node['metadata'] = inputlist[this_node['end']-this_node['meta_num']:this_node['end']]
        return [this_node]
    else:
        family = [this_node]
        next_start = start+2
        for child in range(inputlist[start]):
            next_node_id = family[-1]['id'] + 1
            descendents = build_nodes(inputlist,next_start,next_node_id,node_id)
            next_start = descendents[0]['end']
            family.extend(descendents)
        # so now we have the list of this node and all descendents, but we need
        # to fill in the end of this node
        family[0]['end'] = next_start+family[0]['meta_num']
        family[0]['metadata'] = inputlist[family[0]['end']-family[0]['meta_num']:family[0]['end']]
        return family

#breakdown = build_nodes(test_inp,0,0,-1)
breakdown = build_nodes(inp,0,0,-1)
# we actually want the sum of the metadata
s = sum([sum(n['metadata']) for n in breakdown])
print("part 1: " + str(s))

# I feel like I'm being shitty here, but let's just get the child arrays by parsing parenthood
# there must be a better way but jeez, today is already kicking my ass pretty bad.

for i in range(len(breakdown)):
    breakdown[i]['children'] = [n['id'] for n in breakdown if n['parent'] == breakdown[i]['id']]

# o jeez, here we go again
def eat_children(node_array,i):
    # return the "value" of the ith entry in the node-array
    if node_array[i]['child_num'] == 0:
        return sum(node_array[i]['metadata'])
    else:
        val = 0
        for idx in node_array[i]['metadata']:
            # translate the relative counter (counts from 1) to absolute node_id
            # only count if idx-1 is in range
            if idx > 0 and idx <= node_array[i]['child_num']:
                child_id = node_array[i]['children'][idx-1]
                val += eat_children(node_array,child_id)
        return val

tval = eat_children(breakdown,0)
print("part 2: " + str(tval))
