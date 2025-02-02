import math

class Property:
    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    # Calculate distance between two properties using Haversine formula
    def distance_to(self, other_property):
        # Radius of the Earth in kilometers
        R = 6371.0
        
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(other_property.latitude)
        lon2 = math.radians(other_property.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Distance in kilometers
        distance = R * c
        return distance

class PropertyGraph:
    def __init__(self):
        # This will store the properties as vertices in a graph
        self.properties = {}

    def Add_Property(self, id, latitude, longitude):
        # Create a Property object and add it to the graph
        if id not in self.properties:
            self.properties[id] = Property(id, latitude, longitude)
        else:
            print(f"Property with id {id} already exists.")

    def Get_Nearest_Properties(self, property_id, n=10):
        # Get the property object based on id
        if property_id not in self.properties:
            print(f"Property with id {property_id} does not exist.")
            return []

        target_property = self.properties[property_id]
        
        # Create a list of tuples (property_id, distance)
        distances = []
        for prop_id, prop in self.properties.items():
            if prop_id != property_id:  # Don't compare the property with itself
                dist = target_property.distance_to(prop)
                distances.append((prop_id, dist))

        # Sort the properties by distance (ascending)
        distances.sort(key=lambda x: x[1])

        # Return the nearest `n` properties
        nearest_properties = distances[:n]
        
        return nearest_properties

    def print_properties(self):
        # Print all properties in the graph
        for prop in self.properties.values():
            print(f"Property {prop.id}: Latitude {prop.latitude}, Longitude {prop.longitude}")

# Example usage:

# Create a PropertyGraph object
graph = PropertyGraph()

# Add properties (id, latitude, longitude)
graph.Add_Property(1, 40.7128, -74.0060)  # New York
graph.Add_Property(2, 34.0522, -118.2437) # Los Angeles
graph.Add_Property(3, 41.8781, -87.6298)  # Chicago
graph.Add_Property(4, 29.7604, -95.3698)  # Houston
graph.Add_Property(5, 37.7749, -122.4194) # San Francisco

# Print all properties
graph.print_properties()

# Find the 3 nearest properties to property with id 1 (New York)
nearest = graph.Get_Nearest_Properties(1, n=3)
