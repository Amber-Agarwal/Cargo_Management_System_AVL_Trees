from avl import AVLTree
from avl import object_id_sort
def preorder(root, arr):

    if not root:
        return

    arr.append(root.object_type.object_id)

    preorder(root.left, arr)

    preorder(root.right, arr)

# Function to initiate preorder traversal
# and return the resulting list
def preOrder(root):
    arr = []
    preorder(root, arr)
    return arr

class Bin:
    def __init__(self, bin_id, capacity,key = None):
        self.bin_id = bin_id
        self.capacity = capacity
        self.key = AVLTree(object_id_sort)
       

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.key.insert_object_type(object)
        self.capacity -= object.size
    def remove_object(self, object):
        # Implement logic to remove an object by ID
        self.key.delete_object_type(object)
        self.capacity+=object.size
    def traversal_key(self):
        return preOrder(self.key.root)

