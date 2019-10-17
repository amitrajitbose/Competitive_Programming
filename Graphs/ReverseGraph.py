"""
Reverse a directed graph

Input:
A -> B, B -> C, A ->C

Output:
B->A, C -> B, C -> A


"""
from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value
    
    def __repr__(self):
        return self.value

def reverse_graph(graph):
    # Fill this in.
    # create new graph to hold the transposed graph
    transpose = {i:Node(i) for i in graph} # set up nodes in new graph
    for src in transpose:
        for dest in graph[src].adjacent:
            transpose[dest.value].adjacent.append(transpose[src])
    return transpose

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

print("Print Original Graph")
for _, val in graph.items():
    print(_, "-->", val.adjacent)
print("Print Reversed Graph")
for _, val in reverse_graph(graph).items():
    print(_, "-->", val.adjacent)

# []
# ['a', 'b']
# ['a']
