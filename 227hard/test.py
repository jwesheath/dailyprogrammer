from AdjMatrix import AdjMatrix

adj = AdjMatrix('example1.txt')
print(adj)
print(adj.grid)
print(adj.nodes)
print(adj.edges)
print(dir(adj))

adj = AdjMatrix('example2.txt')
print(adj)
adj = AdjMatrix('example3.txt')
print(adj)
adj = AdjMatrix('example4.txt')
print(adj)
adj = AdjMatrix('example5.txt')
print(adj)
