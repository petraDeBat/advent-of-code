test_input = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''

test_array = test_input.split()

import copy

# Start by looking for sets of three computers where 
# each computer in the set is connected to the other two computers.
def find_three_connected(data):
    computer_connections = {}
    for i in range(len(data)):
        comp1 , comp2 = data[i].split('-')[0], data[i].split('-')[1]

        if comp1 in computer_connections:
            # check if mapping already exists going the other way
            if comp2 not in computer_connections or comp1 not in computer_connections[comp2]:
                computer_connections[comp1].append(comp2) # don't love tis, will come back to it later
        else:
            computer_connections[comp1] = [comp2] # yeah def don't know about the list LOL

    # now to actually determine stuff (im ded)
    three_connected = []

    for key, values in computer_connections.items():
        print(key, values)

    for key, values in computer_connections.items():
        for computer in values:
            modded_values = copy.deepcopy(values)
            modded_values.remove(computer)
            for third_computer in modded_values:
                # wow...this is going get real ugly, real fast
                if third_computer in computer_connections and computer in computer_connections[third_computer]:
                    bah = [key, computer, third_computer]
                    bah.sort()
                    three_connected.append(bah)
    return three_connected
            



    return computer_connections
# test data should output 12 sets of three computers
# aq,cg,yn
# aq,vc,wq
# co,de,ka
# co,de,ta
# co,ka,ta
# de,ka,ta
# kh,qp,ub
# qp,td,wh
# tb,vc,wq
# tc,td,wh
# td,wh,yn
# ub,vc,wq


# narrow down the sets of three computers to only the ones that 
# have 't' as the start of a computer's name
# return number of sets found

connections = find_three_connected(test_array)

# sort based on first item
connections.sort(key=lambda x: x[0])

for i in range(len(connections)):
    print(f'{i+1}: {connections[i]}')


Missing set: {'de', 'ka', 'ta'}

kh ['tc', 'ub', 'ta']
qp ['kh', 'ub']

de ['cg', 'co', 'ta']

ka ['co', 'de']
yn ['aq', 'cg']
cg ['tb']
vc ['aq']
tb ['ka', 'wq', 'vc']
wh ['tc', 'td', 'yn', 'qp']

ta ['co', 'ka']

tc ['td']
td ['qp', 'yn']
aq ['cg']
wq ['ub', 'aq', 'vc']
ub ['vc']
co ['tc']