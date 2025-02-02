from enum import Enum
from typing import List
from .Amenity import Amenity
import random
from faker import Faker
from .PropertyType import PropertyType

# Client Class
class Client:
    def __init__(self, client_id: int, name: str, preferred_price_min: float, 
                 preferred_price_max: float, preferred_amenities: List[Amenity], 
                 preferred_property_type: PropertyType):
        self.client_id = client_id
        self.name = name
        self.preferred_price_min = preferred_price_min
        self.preferred_price_max = preferred_price_max
        self.preferred_amenities = preferred_amenities
        self.preferred_property_type = preferred_property_type

    def __str__(self):
        amenities_list = ', '.join([amenity.value for amenity in self.preferred_amenities])
        return f"Client ID: {self.client_id}\n" \
               f"Name: {self.name}\n" \
               f"Preferred Price Range: ${self.preferred_price_min} - ${self.preferred_price_max}\n" \
               f"Preferred Amenities: {amenities_list}\n" \
               f"Preferred Property Type: {self.preferred_property_type.value}"

    def create_random_clients(clients_number: int) :
        fake = Faker()
        clients = []
        for client_id in range(1, clients_number + 1):
        # Randomly generate client name
            name = fake.name()

            # Randomly generate price range (with min < max)
            preferred_price_min = round(random.uniform(200000, 1000000), 2)  # Min price between 200,000 and 1,000,000
            preferred_price_max = round(random.uniform(preferred_price_min + 500, 1000000), 2)  # Max price must be higher than min

            # Randomly select amenities (choosing 1-3 random amenities from the list)
            preferred_amenities = random.sample(list(Amenity), random.randint(1, 3))  # Randomly pick 1-3 amenities

            # Randomly select a property type
            preferred_property_type = random.choice(list(PropertyType))

            # Create and append the Client object
            client = Client(client_id, name, preferred_price_min, preferred_price_max, preferred_amenities, preferred_property_type)
            clients.append(client)
    
        return clients

