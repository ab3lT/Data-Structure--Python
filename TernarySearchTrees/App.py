from TernarySearchTrees.TST import TST


tree = TST()

tree.put("apple", 100)
tree.put("orange", 200)
tree.put("banana", 300)

print(tree.get("apple"))
print(tree.get("orange"))
print(tree.get("banana"))