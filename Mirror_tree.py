# Python3 program to find the mirror node in
# Binary tree

class Node:
	'''A binary tree node has data, reference to left child
		and a reference to right child '''

	def __init__(self, key, lchild=None, rchild=None):
		self.key = key
		self.lchild = None
		self.rchild = None


# recursive function to find mirror
def findMirrorRec(target, left, right):

	# If any of the node is none then node itself
	# and decendent have no mirror, so return
	# none, no need to further explore!
	if left == None or right == None:
		return None

	# if left node is target node, then return
	# right's key (that is mirror) and vice versa
	if left.key == target:
		return right.key
	if right.key == target:
		return left.key

	# first recur external nodes
	mirror_val = findMirrorRec(target, left.lchild, right.rchild)
	if mirror_val != None:
		return mirror_val

	# if no mirror found, recur internal nodes
	findMirrorRec(target, left.rchild, right.lchild)

# interface for mirror search
def findMirror(root, target):
	if root == None:
		return None

	if root.key == target:
		return target

	return findMirrorRec(target, root.lchild, root.rchild)

# Driver
def main():
	root = Node(1)
	n1 = Node(2)
	n2 = Node(3)
	root.lchild = n1
	root.rchild = n2
	n3 = Node(4)
	n4 = Node(5)
	n5 = Node(6)
	n1.lchild = n3
	n2.lchild = n4
	n2.rchild = n5
	n6 = Node(7)
	n7 = Node(8)
	n8 = Node(9)
	n3.rchild = n6
	n4.lchild = n7
	n4.rchild = n8

	# target node whose mirror have to be searched
	target = n3.key

	mirror = findMirror(root, target)
	print("Mirror of node {} is node {}".format(target, mirror))

if __name__ == '__main__':
	main()
