class TreeNode:
    def __init__(self, value):
        self.value = value  # The object stored in the node
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of node (for balancing)

class BinaryTree:
    def __init__(self, sortable_property):
        self.root = None  # Root node of the tree
        self.sortable_property = sortable_property  # The key used for sorting the objects
    
    def _get_key(self, obj):
        return getattr(obj, self.sortable_property)  # Retrieve the sorting key from the object
    
    def insert(self, obj):
        if not hasattr(obj, self.sortable_property):
            raise ValueError(f"Object must have a '{self.sortable_property}' attribute")
        self.root = self._insert_recursive(self.root, obj)
    
    def _insert_recursive(self, node, obj):
        if node is None:
            return TreeNode(obj)
        
        key = self._get_key(obj)
        if key < self._get_key(node.value):
            node.left = self._insert_recursive(node.left, obj)
        else:
            node.right = self._insert_recursive(node.right, obj)
        
        # Update height and balance the node
        return self._balance(node)
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return None
        
        if key < self._get_key(node.value):
            node.left = self._delete_recursive(node.left, key)
        elif key > self._get_key(node.value):
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children, find the inorder successor
                successor = self._find_min_node(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, self._get_key(successor.value))
        
        # Update height and balance the node
        return self._balance(node)


    def _get_height(self, node):
        return node.height if node else 0
    
    def _get_balance_factor(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0
    
    def _balance(self, node):
        # Update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Get balance factor
        balance = self._get_balance_factor(node)
        
        # Perform rotations if unbalanced
        if balance > 1:  # Left heavy
            if self._get_balance_factor(node.left) < 0:  # Left-Right case
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        if balance < -1:  # Right heavy
            if self._get_balance_factor(node.right) > 0:  # Right-Left case
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def find(self, key):
        return self._find_recursive(self.root, key)
    
    def _find_recursive(self, node, key):
        if node is None:
            return None
        if key == self._get_key(node.value):
            return node.value
        elif key < self._get_key(node.value):
            return self._find_recursive(node.left, key)
        else:
            return self._find_recursive(node.right, key)
    
    def get_all_objects(self):
        objects = []
        self._inorder_collect_objects(self.root, objects)
        return objects
    
    def _inorder_collect_objects(self, node, objects):
        if node is not None:
            self._inorder_collect_objects(node.left, objects)
            objects.append(node.value)
            self._inorder_collect_objects(node.right, objects)




