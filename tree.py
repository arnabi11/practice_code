class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:

    def __init__(self):
        self.inorderList = []
        self.revOrderList = []

    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node == None:
            node = self.createNode(data)
            return node
        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)
        return  node

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            self.inorderList.append(root.data)
            print root.data
            self.inorder(root.right)


    def preorder(self,root):
        if root is not None:
            print root.data
            self.preorder(root.left)
            self.preorder(root.right)
    def deleteNode(self,root,data):
        pass

    def height(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printLevelOrder(self,root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

    # Print nodes at a given level
    def printGivenLevel(self,root, level):
        if root is None:
            return
        if level == 1:
            print "%d" % (root.data),
        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)

    def mirror(self,node):
        if node==None:
            return
        else:
            self.mirror(node.left)
            self.mirror(node.right)
            self.temp = node.left
            node.left = node.right
            node.right = self.temp


def main():
    root = None
    tree = Tree()

    root = tree.insert(root, 6)
    root = tree.insert(root, 2)
    root = tree.insert(root, 3)
    root = tree.insert(root, 7)
    root = tree.insert(root, 4)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.insert(root, 8)
    root = tree.insert(root, 9)


    # print root.data
    tree.inorder(root)
    # tree.preorder(root)
    # print "\n Reverse: "
    # tree.revOrder(root)
    tree.mirror(root)
    print "\nInorder Mirror:"
    tree.inorder(root)
    print "\n Preorder Mirror:"
    tree.preorder(root)
    print "Level order traversal of mirror binary tree is -"
    tree.printLevelOrder(root)
    # searchNode = int(raw_input("Enter the node whose mirror is needed: "))
    # for indx,elem in enumerate(tree.inorderList):
    #     if elem == searchNode:
    #         print "Mirror of  %d is %d"%(searchNode,tree.revOrderList[indx])
    #         return

    # tree2 = Tree()
    # root2 = None
    # # print tree.inorderList
    # for i in tree.inorderList:
    #     # print i
    #     root2 = tree2.revInsert(root2,i)
    # tree2.inorder(root2)

if __name__ == "__main__":
    main()
