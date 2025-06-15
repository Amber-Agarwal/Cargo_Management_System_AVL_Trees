from node import Node




def lesser_lesser(object_type_1, object_type_2):
    if object_type_1.capacity>object_type_2.capacity:
        return 1
    elif object_type_1.capacity<object_type_2.capacity:
        return 0
    elif object_type_2.capacity == object_type_1.capacity:
        if object_type_1.bin_id>object_type_2.bin_id:
            return 1
        elif object_type_1.bin_id<object_type_2.bin_id:
            return 0
        
def lesser_greater(object_type_1, object_type_2):
    if object_type_1.capacity>object_type_2.capacity:
        return 1
    elif object_type_1.capacity<object_type_2.capacity:
        return 0
    elif object_type_2.capacity == object_type_1.capacity:
        if object_type_1.bin_id<object_type_2.bin_id:
            return 1
        elif object_type_1.bin_id>object_type_2.bin_id:
            return 0
        
def greater_lesser(object_type_1, object_type_2):
    if object_type_1.capacity<object_type_2.capacity:
        return 1
    elif object_type_1.capacity>object_type_2.capacity:
        return 0
    elif object_type_2.capacity == object_type_1.capacity:
        if object_type_1.bin_id>object_type_2.bin_id:
            return 1
        elif object_type_1.bin_id<object_type_2.bin_id:
            return 0
        
def greater_greater(object_type_1, object_type_2):
    if object_type_1.capacity<object_type_2.capacity:
        return 1
    elif object_type_1.capacity>object_type_2.capacity:
        return 0
    elif object_type_2.capacity == object_type_1.capacity:
        if object_type_1.bin_id<object_type_2.bin_id:
            return 1
        elif object_type_1.bin_id>object_type_2.bin_id:
            return 0

def bin_id_sort(object_type_1,object_type_2):
    if object_type_1.bin_id<object_type_2.bin_id:
        return 1
    else:
        return 0
    
def object_id_sort(object_type_1,object_type_2):
    if object_type_1.object_id<object_type_2.object_id:
        return 1
    else:
        return 0





class AVLTree:
    def __init__(self, compare_function):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def height(self,node):
        if node is None:
            return 0
        return node.height
    
    def Balanced(self,node):
        if node is None:
            return 0
        else:
            return self.height(node.left)-self.height(node.right)
        
    def left_rotate(self,node_to_be_rotated):
        a = node_to_be_rotated.right
        b = a.left
        a.left = node_to_be_rotated
        node_to_be_rotated.right = b
        node_to_be_rotated.height = 1 + max(self.height(node_to_be_rotated.left),self.height(node_to_be_rotated.right))
        a.height = 1+ max(self.height(a.right),self.height(a.left))
        return a
    
    def right_rotate(self,node_to_be_rotated):
        a = node_to_be_rotated.left
        b = a.right

        a.right = node_to_be_rotated
        node_to_be_rotated.left = b

        node_to_be_rotated.height = 1 + max(self.height(node_to_be_rotated.left),self.height(node_to_be_rotated.right))
        a.height = 1+ max(self.height(a.right),self.height(a.left))
        return a
    
    def left_most_node(self,root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    
    def right_most_node(self,root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr

    
    def search_bin_id(self,root,id_to_be_searched):
        if root is None or root.object_type.bin_id == id_to_be_searched:
            return root
        if root.object_type.bin_id<id_to_be_searched:
            return self.search_bin_id(root.right,id_to_be_searched)
        return self.search_bin_id(root.left,id_to_be_searched)
    
    def search_object_id(self,root,id_to_be_searched):

        if root is None or root.object_type.object_id == id_to_be_searched:
            return root
        if root.object_type.object_id<id_to_be_searched:
            return self.search_object_id(root.right,id_to_be_searched)
        return self.search_object_id(root.left,id_to_be_searched)
       
    


    def search_capacity(self,root,capacity_to_be_searched): # make a new function named searchcapacity
        
        if root is None or (root.object_type.capacity == capacity_to_be_searched.capacity and root.object_type.bin_id == capacity_to_be_searched.bin_id):
            return root
        if self.comparator(root.object_type,capacity_to_be_searched):
            return self.search_capacity(root.right,capacity_to_be_searched)
        return self.search_capacity(root.left,capacity_to_be_searched)
    
    def search_bin_green(self,root,object):
        if root is None:
            return root
        
        curr = root
        while curr.right is not None:
            curr = curr.right
        if curr.object_type.capacity < object.size:
            return None
        return curr
    
    def search_bin_red(self,root,object):
        if root is None:
            return root
        curr = root
        while curr.right is not None:
            curr = curr.right
        if curr.object_type.capacity< object.size:
            return None
        return curr
    
    def search_bin_yellow(self,root,object):
        # if root is None:
        #     return root
        # while root.left or root.right:
        #     if root.object_type.capacity>= object.size:
        #         if root.right is not None and root.right.object_type.capacity >= object.size:
        #             root=root.right
        #         else:
        #             # print(root.left.object_type.bin_id,root.right.object_type.bin_id)
        #             break
        #     elif root.object_type.capacity<object.size:
        #         if root.left is not None:
        #             root = root.left
        #         else:
        #             return None



        pass
                
    def search_bin_blue(self,root,object):
        # if root is None:
        #     return root
        # while root.left or root.right:
        #     if root.object_type.capacity>= object.size:
        #         if root.right is not None and root.right.object_type.capacity >= object.size:
        #             root=root.right
        #         else:
        #             break
        #     elif root.object_type.capacity<object.size:
        #         if root.left is not None:
        #             root = root.left
        #         else:
        #             return None
        # return root
        pass
    
    def insert(self,root,node_to_be_inserted):
        if root is None:
            return Node(node_to_be_inserted)
        elif self.comparator(node_to_be_inserted,root.object_type): # required comparision achieved
            root.left = self.insert(root.left,node_to_be_inserted)
        else:
            root.right = self.insert(root.right,node_to_be_inserted)
    
        root.height = 1+ max(self.height(root.left),self.height(root.right))
        if self.Balanced(root)>1 and self.comparator(node_to_be_inserted,root.left.object_type):
            return self.right_rotate(root)
        if self.Balanced(root)<-1 and self.comparator(root.right.object_type,node_to_be_inserted):
            return self.left_rotate(root)
        if self.Balanced(root)>1 and self.comparator(root.left.object_type,node_to_be_inserted):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if self.Balanced(root)<-1 and self.comparator(node_to_be_inserted,root.right.object_type):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
        
    def delete(self,root,node_to_be_deleted):
        if root is None:
            return root
        if self.comparator(node_to_be_deleted,root.object_type):
            root.left = self.delete(root.left,node_to_be_deleted)
        elif self.comparator(root.object_type,node_to_be_deleted):
            root.right = self.delete(root.right,node_to_be_deleted)
        else:
            if root.left is None:
                a = root.right
                root = None
                return a
            elif root.right is None:
                a = root.left
                root = None
                return a
            a = self.left_most_node(root.right)
            root.object_type = a.object_type
            root.right = self.delete(root.right,a.object_type)
        if root is None:
            return root
        root.height = 1+max(self.height(root.left),self.height(root.right))
        if self.Balanced(root)>1 and self.Balanced(root.left)>=0:
            return self.right_rotate(root)
        if self.Balanced(root)<-1 and self.Balanced(root.right)<=0:
            return self.left_rotate(root)
        if self.Balanced(root)>1 and self.Balanced(root.left)<0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if self.Balanced(root)<-1 and self.Balanced(root.right)>0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    
    def insert_object_type(self,object):
        self.root = self.insert(self.root,object)
    
    def delete_object_type(self,object):
        self.root = self.delete(self.root,object)
    
    def search_object_type(self,object):
        return self.search(self.root,object)
    
    def search_bin_use(self,object):
        return self.search_bin(self.root,object)
    
    def search_objectid(self,id_to_be_searched):
        return self.search_object_id(self.root,id_to_be_searched)
    
    def search_binid(self,id_to_be_searched):
        return self.search_bin_id(self.root,id_to_be_searched)
    
    def searchbin_blue(self,object):
        nd=self.root
        ans=None
        while nd:
            if nd.object_type.capacity>=object.size:
                ans=nd
                nd=nd.right
            else:nd=nd.left
        if ans: return ans
        return None
    
    def searchbin_yellow(self,object):
        # return self.search_bin_yellow(self.root,object)
        newnode=self.root
        final=None
        while newnode:
            if newnode.object_type.capacity>=object.size:
                final=newnode
                newnode=newnode.right
            else:newnode=newnode.left
        if final:
            return final
        return None
    
    def searchbin_green(self,object):
        return self.search_bin_green(self.root,object)
    
    def searchbin_red(self,object):
        return self.search_bin_red(self.root,object)
    
    def searchcapacity(self,object):
        return self.search_capacity(self.root,object)
    



    


