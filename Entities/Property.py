from typing import List
from .Amenity import Amenity
from faker import Faker
import random
from .PropertyType import PropertyType

# Property Class
class Property:
    def __init__(self, property_id: int, price: float, amenities: List[Amenity], 
                 property_type: str, location: str, latitude: float, longitude: float):
        self.property_id = property_id
        self.price = price
        self.amenities = amenities
        self.property_type = property_type
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        amenities_list = ', '.join([amenity.value for amenity in self.amenities])
        return f"Property ID: {self.property_id}\n" \
               f"Price: ${self.price}\n" \
               f"Amenities: {amenities_list}\n" \
               f"Property Type: {self.property_type}\n" \
               f"Location: {self.location}\n" \
               f"Latitude: {self.latitude}\n" \
               f"Longitude: {self.longitude}"
    
    def create_random_properties(num_properties: int = 100) -> list['Property']:
        fake = Faker()  # Create a Faker instance
    
        properties: list['Property'] = [] 
        for i in range(1, num_properties + 1):
            # Generate random data for each property
            price = round(random.uniform(100000, 1000000), 2)
            amenities = random.sample(list(Amenity), random.randint(1, 5))  # Randomly select 1 to 5 amenities
            property_type = random.choice(list(PropertyType))  # Randomly select property type
            
            # Generate a random street address and then force NJ as the state
            street_address = fake.street_address()
            city = fake.city()
            state = "New Jersey"  # Force NJ as the state
            zip_code = fake.zipcode_in_state("NJ")
            location = f"{street_address}, {city}, {state} {zip_code}"
            
            latitude = round(random.uniform(39.8, 41.4), 6)  # New Jersey latitude range
            longitude = round(random.uniform(-75.5, -73.5), 6)  # New Jersey longitude range

            # Create a Property instance
            property_instance = Property(
                property_id=i,
                price=price,
                amenities=amenities,
                property_type=property_type,
                location=location,
                latitude=latitude,
                longitude=longitude
            )
            
            properties.append(property_instance)
        
        return properties   


    def retPropName(self):
        return self.property_id 


