class HashTable:
    def __init__(self, key_property, initial_size=100):
        self.key_property = key_property  # Property of the object to be used as key
        self.size = initial_size  # Initial size of the hash table
        self.count = 0  # Number of stored elements
        self.load_factor = 0.7  # Threshold for resizing
        self.table = [[] for _ in range(self.size)]  # Initialize the table with empty lists
    
    def _get_key(self, obj):
        return getattr(obj, self.key_property)  # Retrieve key property from object
    
    def _hash(self, key):
        return hash(key) % self.size  # Compute the hash index
    
    def _resize(self):
        new_size = self.size * 2  # Double the table size
        new_table = [[] for _ in range(new_size)]  # Create a new table
        
        # Rehash all existing elements into the new table
        for bucket in self.table:
            for obj in bucket:
                key = self._get_key(obj)
                index = hash(key) % new_size
                new_table[index].append(obj)
        
        # Update the table and size
        self.size = new_size
        self.table = new_table
    
    def insert(self, obj):
        # Resize if the load factor is exceeded
        if self.count / self.size > self.load_factor:
            self._resize()
        
        key = self._get_key(obj)  # Extract key from object
        index = self._hash(key)  # Get index for the key
        
        # Check if the key already exists in the bucket
        for i, existing_obj in enumerate(self.table[index]):
            if self._get_key(existing_obj) == key:
                self.table[index][i] = obj  # Update existing key with new object
                return
        
        # Add new object to the bucket
        self.table[index].append(obj)
        self.count += 1  # Increase element count
    
    def find(self, key):
        index = self._hash(key)  # Get index for the key
        for obj in self.table[index]:
            if self._get_key(obj) == key:
                return obj  # Return object if key is found
        return None  # Return None if key is not found
    
    def remove(self, key):
        index = self._hash(key)  # Get index for the key
        for i, obj in enumerate(self.table[index]):
            if self._get_key(obj) == key:
                del self.table[index][i]  # Remove the object
                self.count -= 1  # Decrease element count
                return
        raise KeyError(f"Key '{key}' not found")  # Raise error if key does not exist