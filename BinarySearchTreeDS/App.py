from BinarySearchTreeDS.BinarySearchTree import BST

bst = BST();

bst.insert(12)
bst.insert(10)
bst.insert(11)
bst.insert(13)
bst.insert(14)
bst.insert(16)
bst.insert(17)
bst.insert(19)

bst.traverseInOrder()

bst.remove(10)

bst.traverseInOrder()