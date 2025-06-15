from bin import Bin
from bin import preOrder,preorder
from avl import AVLTree
from avl import greater_greater
from avl import lesser_greater
from avl import lesser_lesser
from avl import greater_lesser
from avl import bin_id_sort
from avl import object_id_sort
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.green_avl_tree = AVLTree(greater_greater)
        self.red_avl_tree = AVLTree(greater_lesser)
        self.yellow_avl_tree = AVLTree(lesser_greater)
        self.blue_avl_tree = AVLTree(lesser_lesser)
        self.bins_id_avl_tree = AVLTree(bin_id_sort)
        self.objects_id_avl_tree = AVLTree(object_id_sort)

    def add_bin(self, bin_id, capacity):
        old_bin = Bin(bin_id,capacity)
        self.green_avl_tree.insert_object_type(old_bin)
        self.red_avl_tree.insert_object_type(old_bin)
        self.yellow_avl_tree.insert_object_type(old_bin)
        self.blue_avl_tree.insert_object_type(old_bin)
        self.bins_id_avl_tree.insert_object_type(old_bin)

    def add_object(self, object_id, size, color):

        object = Object(object_id,size,color)
        if color == Color.BLUE:
            bin = self.blue_avl_tree.searchbin_blue(object)
            if bin is None:
                raise NoBinFoundException
            old_bin = bin.object_type
            bin_id = old_bin.bin_id
            new_object = Object(object_id,size,color,bin_id)
            self.yellow_avl_tree.delete_object_type(old_bin)
            self.blue_avl_tree.delete_object_type(old_bin)
            self.red_avl_tree.delete_object_type(old_bin)
            self.green_avl_tree.delete_object_type(old_bin)
            
            # old_bin.add_object(new_object)
            # old_bin = Bin(old_bin.bin_id,old_bin.capacity - size,old_bin.key)

            old_bin.add_object(new_object)
            
            self.yellow_avl_tree.insert_object_type(old_bin)
            self.red_avl_tree.insert_object_type(old_bin)
            self.green_avl_tree.insert_object_type(old_bin)
            self.blue_avl_tree.insert_object_type(old_bin)
            self.objects_id_avl_tree.insert_object_type(new_object)
            bin_id_avl_find = self.bins_id_avl_tree.search_binid(bin_id)
            # bin_id_avl_find.object_type.capacity = old_bin.capacity - size
            # bin_id_avl_find.object_type.add_object(new_object)
            
    
        if color == Color.YELLOW:
            bin = self.yellow_avl_tree.searchbin_yellow(object)
            
            if bin is None:
                raise NoBinFoundException
            old_bin = bin.object_type
            bin_id = old_bin.bin_id
            new_object = Object(object_id,size,color,bin_id)
            self.yellow_avl_tree.delete_object_type(old_bin)
            self.blue_avl_tree.delete_object_type(old_bin)
            self.red_avl_tree.delete_object_type(old_bin)
            self.green_avl_tree.delete_object_type(old_bin)
            #old_bin.add_object(new_object)
            # old_bin = Bin(old_bin.bin_id,old_bin.capacity - size,old_bin.key)
            old_bin.add_object(new_object)
            
            self.yellow_avl_tree.insert_object_type(old_bin)
            self.red_avl_tree.insert_object_type(old_bin)
            self.green_avl_tree.insert_object_type(old_bin)
            self.blue_avl_tree.insert_object_type(old_bin)
            self.objects_id_avl_tree.insert_object_type(new_object)
            # bin_id_avl_find = self.bins_id_avl_tree.search_binid(bin_id)
            # bin_id_avl_find.object_type.capacity = old_bin.capacity - size
            # bin_id_avl_find.object_type.add_object(new_object)

        if color == Color.RED:
            bin = self.red_avl_tree.searchbin_red(object)
            if bin is None:
                raise NoBinFoundException
            old_bin = bin.object_type
            bin_id = old_bin.bin_id
            new_object = Object(object_id,size,color,bin_id)
            self.yellow_avl_tree.delete_object_type(old_bin)
            self.blue_avl_tree.delete_object_type(old_bin)
            self.red_avl_tree.delete_object_type(old_bin)
            self.green_avl_tree.delete_object_type(old_bin)
            #old_bin.add_object(new_object)
            # old_bin = Bin(old_bin.bin_id,old_bin.capacity - size,old_bin.key)
            old_bin.add_object(new_object)
            
            self.yellow_avl_tree.insert_object_type(old_bin)
            self.red_avl_tree.insert_object_type(old_bin)
            self.green_avl_tree.insert_object_type(old_bin)
            self.blue_avl_tree.insert_object_type(old_bin)
            self.objects_id_avl_tree.insert_object_type(new_object)
            bin_id_avl_find = self.bins_id_avl_tree.search_binid(bin_id)
            # bin_id_avl_find.object_type.capacity = old_bin.capacity - size
            # bin_id_avl_find.object_type.add_object(new_object)

        if color == Color.GREEN:
            bin = self.green_avl_tree.searchbin_green(object)
            if bin is None:
                raise NoBinFoundException
            old_bin = bin.object_type
            bin_id = old_bin.bin_id
            new_object = Object(object_id,size,color,bin_id)
            self.yellow_avl_tree.delete_object_type(old_bin)
            self.blue_avl_tree.delete_object_type(old_bin)
            self.red_avl_tree.delete_object_type(old_bin)
            self.green_avl_tree.delete_object_type(old_bin)
            #old_bin.add_object(new_object)
            # old_bin = Bin(old_bin.bin_id,old_bin.capacity - size,old_bin.key)
            old_bin.add_object(new_object)
            
            self.yellow_avl_tree.insert_object_type(old_bin)
            self.red_avl_tree.insert_object_type(old_bin)
            self.green_avl_tree.insert_object_type(old_bin)
            self.blue_avl_tree.insert_object_type(old_bin)
            self.objects_id_avl_tree.insert_object_type(new_object)
            bin_id_avl_find = self.bins_id_avl_tree.search_binid(bin_id)
            # bin_id_avl_find.object_type.capacity = old_bin.capacity - size
            # bin_id_avl_find.object_type.add_object(new_object)

            
      

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        object_found = self.objects_id_avl_tree.search_objectid(object_id)
        
        color_found = object_found.object_type.color
        size_found = object_found.object_type.size
        bin_id_found = object_found.object_type.bin_id
        new_object = object_found.object_type
        self.objects_id_avl_tree.delete_object_type(object_found.object_type)
        bin_node_find = self.bins_id_avl_tree.search_binid(bin_id_found)
        
        old_bin = bin_node_find.object_type
       
        self.yellow_avl_tree.delete_object_type(old_bin)
        self.green_avl_tree.delete_object_type(old_bin)
        self.red_avl_tree.delete_object_type(old_bin)
        self.blue_avl_tree.delete_object_type(old_bin)
        old_bin.remove_object(new_object)
        self.yellow_avl_tree.insert_object_type(old_bin)
        self.green_avl_tree.insert_object_type(old_bin)
        self.red_avl_tree.insert_object_type(old_bin)
        self.blue_avl_tree.insert_object_type(old_bin)

       


    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin_node_find = self.bins_id_avl_tree.search_binid(bin_id)
        capacity=bin_node_find.object_type.capacity
        l = bin_node_find.object_type.traversal_key()
        return (capacity,l)


    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        object_node_find = self.objects_id_avl_tree.search_objectid(object_id)
        return object_node_find.object_type.bin_id
    
    