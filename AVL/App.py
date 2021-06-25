from AVL.BalancedTree import BalancedTree

tree1 = BalancedTree()
tree2 = BalancedTree()
tree3 = BalancedTree()


tree1.insert(4)
tree1.insert(6)
tree1.insert(5)
tree1.traverseInOrder()

print('')

tree2.insert(7)
tree2.insert(8)
tree2.insert(9)
tree2.traverseInOrder()

print('')

tree3.insert(12)
tree3.insert(11)
tree3.insert(10)
tree3.traverseInOrder()
