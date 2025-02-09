import unittest
from unittest.mock import patch
from io import StringIO
from typing import List
from faker import *
import time
from Entities.Property import Property
from Entities.Client import Client
from Entities.Agent import Agent
from Entities.Appointment import Appointment
from Entities.Bid import Bid
from DataStructures.BinaryTree import BinaryTree
from DataStructures.Queue import Queue
from DataStructures.graph import PropertyGraph
import sys
sys.setrecursionlimit(100001)

class RealEstateSystem:
    def __init__(self):
        self.properties: BinaryTree = BinaryTree('property_id')  # Binary tree of Property objects
        self.clients: BinaryTree = BinaryTree('client_id')        # Binary tree of Client objects
        self.agents: BinaryTree = BinaryTree('agent_id')          # List of Agent objects
        self.appointments: Queue = Queue()  # List of Appointment objects
        self.bids: List[Bid] = []    

    def addProperty(self, property):
        """Add property to the properties list."""
        self.properties.insert( property)

    def deleteProperty(self, property):
        """Remove property from the properties list"""
        self.properties.delete(property) 

    def getProperty(self, property) -> Property:
        return self.properties.find(property)

    def getAgent(self, agentID) -> Agent:
        return self.agents.find(agentID)  

    def getClient(self, clientId) -> Client:
        return self.clients.find(clientId) 

    def setProperty(self, properties: List[Property]) -> None:
        """set a list of properties as property"""   
        self.properties.append(properties) 

    def getNearestNProperties(self, property_id, number_n):
        graph = PropertyGraph()
        for eachitem in self.getAllProperties():
            graph.Add_Property( eachitem.property_id, eachitem.latitude, eachitem.longitude)
        nearestn: List[Property] = list()
        for property in graph.Get_Nearest_Properties(property_id, number_n):
            nearestn.append(self.getProperty(property[0]))
        return nearestn    


    def getAllProperties(self):
        return self.properties.get_all_objects()    

    def changePropertyStatus(self, updatedProperty):
        """Update a property’s status."""
        for idx, prop in enumerate(self.properties):
            if prop['id'] == updatedProperty['id']:
                self.properties[idx] = updatedProperty
                break

    def addClient(self, client):
        """Add client to the clients list."""
        self.clients.insert(client)

    def updateClientRequirement(self, client, updatedRequirements):
        """Allow clients to update requirements as they go."""
        for c in self.clients:
            if c['id'] == client['id']:
                c['requirements'] = updatedRequirements
                break

    def addAgent(self, agent):
        """Add agent to the agents list."""
        self.agents.insert(agent)

    def scheduleAppointment(self, appointment):
        """Add appointment to the appointments list."""
        self.appointments.enqueue(appointment)

    def getFirstAppointment(self) -> Appointment:
        """Return the first item in the queue"""   
        return self.appointments.dequeue()

    def placeBid(self, bid):
        """Add bid to the bids list."""
        self.bids.append(bid)

    def recommendProperties(self, client):
        """Return recommendations based on nearest neighborhood and changes in inventory."""
        filtered_properties = self.filterProperties(client)
        return self.nearestNeighborhood(client, filtered_properties)

    def filterProperties(self, client):
        """Filter the list of properties within a certain range based on price, amenities, preferred property type and other parameters."""
        valid_properties = []
        for prop in self.properties:
            if (prop['price'] <= client['budget'] and
                prop['amenities'].intersection(client['preferred_amenities']) and
                prop['property_type'] == client['preferred_property_type']):
                valid_properties.append(prop)
        return valid_properties

    def calculateDistance(self, client, property):
        """Calculate the distance between the client and the property."""
        # You would use a geolocation API or other method to calculate real distances
        # For simplicity, we can assume a mock function here
        return abs(client['location'][0] - property['location'][0]) + abs(client['location'][1] - property['location'][1])

    def startRealTimeBidding(self, property):
        """Allow clients to bid on real-time and send notifications."""
        print(f"Real-time bidding started for property {property['id']}")
        # In a real implementation, this would interface with a live system to accept bids and notify clients.


realEstateSystem = RealEstateSystem()

class TestRealEstateSystemPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the RealEstateSystem before performance tests."""
        cls.realEstateSystem = RealEstateSystem()

    def test_add_100000_clients(self):
        """Test performance of adding 1,00,000 clients within 10 seconds."""
        start_time = time.time()

        for client in Client.create_random_clients(100000):
            self.realEstateSystem.addClient(client)

        end_time = time.time()
        self.assertLess(end_time - start_time, 10, "Adding 10,000 clients took too long!")

    def test_get_100000_clients(self):
        """Test performance of adding 1,00,000 clients within 10 seconds."""
        start_time = time.time()

        for client in (1,100000):
            self.realEstateSystem.getClient(client)

        end_time = time.time()
        self.assertLess(end_time - start_time, 10, "Getting 1,00,000 clients took too long!")    



    def test_add_100000_properties(self):
        """Test performance of adding 1,00,000 properties within 15 seconds."""
        start_time = time.time()

        for property in Property.create_random_properties(100000):
            self.realEstateSystem.addProperty(property)

        end_time = time.time()
        self.assertLess(end_time - start_time, 15, "Adding 1,00,000 properties took too long!")

    def test_add_10000_agents(self):
        """Test performance of adding 1,00,000 agents within 10 seconds."""
        start_time = time.time()

        for i in range(10000):
            agent = Agent(i, f"Agent_{i}", [])
            self.realEstateSystem.addAgent(agent)

        end_time = time.time()
        self.assertLess(end_time - start_time, 10, "Adding 10,000 agents took too long!")

    def test_Nearest_10000_Properties(self):
        """Testing the retrieval of nearest 10000 properties""" 

        for property in Property.create_random_properties(20000):
            self.realEstateSystem.addProperty(property)
        start_time = time.time()

        self.realEstateSystem.getNearestNProperties(5, 10000)  
        end_time = time.time()
        self.assertLess(end_time - start_time, 10, "Fetching 10,000 nearest neighbors took too long!")

    def test_create_10000_appointments(self):
        """Testing the creation of 100000 appointments"""
        start_time = time.time()
        for i in range(1,100000):
            apptm: Appointment = Appointment(i,i,i,i, '2025-12-12')
            self.realEstateSystem.scheduleAppointment(apptm)
        end_time = time.time()    
        self.assertLess(end_time - start_time, 1, "Deleting 1,00,000 clients took too long!")      


    def test_delete_100000_clients(self):
        """Test performance of adding 1,00,000 clients within 10 seconds."""
        start_time = time.time()

        for i in range(1,100000):
            realEstateSystem.deleteProperty(i)
        end_time = time.time()

        self.assertLess(end_time - start_time, 10, "Deleting 1,00,000 clients took too long!")    
  
        

if __name__ == "__main__":
    unittest.main()










