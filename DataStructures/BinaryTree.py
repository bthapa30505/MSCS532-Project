class TreeNode:
    def __init__(self, value):
        self.value = value  # The object stored in the node
        self.left = None  # Left child
        self.right = None  # Right child

class BinaryTree:
    def __init__(self, sortable_property):
        self.root = None  # Root node of the tree
        self.sortable_property = sortable_property  # The key used for sorting the objects
    
    def _get_key(self, obj):
        return getattr(obj, self.sortable_property)  # Retrieve the sorting key from the object
    
    def insert(self, obj):
        if not hasattr(obj, self.sortable_property):
            raise ValueError(f"Object must have a '{self.sortable_property}' attribute")  # Ensure object has the sortable property
        
        if self.root is None:
            self.root = TreeNode(obj)  # Set root if tree is empty
        else:
            self._insert_recursive(self.root, obj)  # Recursively insert into the tree
    
    def _insert_recursive(self, node, obj):
        if self._get_key(obj) < self._get_key(node.value):  # Insert into left subtree if key is smaller
            if node.left is None:
                node.left = TreeNode(obj)  # Create new node if left is empty
            else:
                self._insert_recursive(node.left, obj)  # Recursively insert into left subtree
        else:
            if node.right is None:
                node.right = TreeNode(obj)  # Create new node if right is empty
            else:
                self._insert_recursive(node.right, obj)  # Recursively insert into right subtree
    
    def find(self, key):
        return self._find_recursive(self.root, key)  # Start recursive search from root
    
    def _find_recursive(self, node, key):
        if node is None:
            return None  # Return None if key is not found
        if key == self._get_key(node.value):
            return node.value  # Return value if key matches
        elif key < self._get_key(node.value):
            return self._find_recursive(node.left, key)  # Search in left subtree
        else:
            return self._find_recursive(node.right, key)  # Search in right subtree
    
    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)  # Start recursive removal from root
    
    def _remove_recursive(self, node, key):
        if node is None:
            return None  # Return None if node is not found
        
        if key < self._get_key(node.value):
            node.left = self._remove_recursive(node.left, key)  # Search in left subtree
        elif key > self._get_key(node.value):
            node.right = self._remove_recursive(node.right, key)  # Search in right subtree
        else:
            if node.left is None:
                return node.right  # Replace node with right child if left is empty
            elif node.right is None:
                return node.left  # Replace node with left child if right is empty
            min_larger_node = self._find_min(node.right)  # Find the smallest value in the right subtree
            node.value = min_larger_node.value  # Replace current node with that smallest value
            node.right = self._remove_recursive(node.right, self._get_key(min_larger_node.value))  # Remove the duplicate node
        return node  # Return the updated node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left  # Traverse to the leftmost node
        return node  # Return the node with the smallest value
    
    def get_all_objects(self):
        objects = []
        self._inorder_collect_objects(self.root, objects)
        return objects  # Return all objects in sorted order based on traversal

    # Helper function for in-order traversal
    def _inorder_collect_objects(self, node, objects):
        if node is not None:
            self._inorder_collect_objects(node.left, objects)  # Left subtree
            objects.append(node.value)  # Store the entire object
            self._inorder_collect_objects(node.right, objects)  # Right subtree



