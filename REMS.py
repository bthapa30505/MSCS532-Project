import unittest
from unittest.mock import patch
from io import StringIO
from typing import List
from faker import *
from Entities.Property import Property
from Entities.Client import Client
from Entities.Agent import Agent
from Entities.Appointment import Appointment
from Entities.Bid import Bid
from DataStructures.BinaryTree import BinaryTree
from DataStructures.Queue import Queue

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

    def getProperty(self, property) -> Property:
        return self.properties.find(property)

    def getAgent(self, agentID) -> Agent:
        return self.agents.find(agentID)  

    def getClient(self, clientId) -> Client:
        return self.clients.find(clientId) 

    def setProperty(self, properties: List[Property]) -> None:
        """set a list of properties as property"""   
        self.properties.append(properties) 

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

    def nearestNeighborhood(self, client, properties):
        """Sort properties based on distance and return the first 5."""
        properties_sorted = sorted(properties, key=lambda prop: self.calculateDistance(client, prop))
        return properties_sorted[:5]

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

# Creating and storing dummy data for propery, client and agents.
property_to_test = None
client_to_test = None
agent_to_test = None
for random_property in Property.create_random_properties(100):
    realEstateSystem.addProperty(random_property)
    if(random_property.property_id == 23):
        property_to_test = random_property
for random_client in Client.create_random_clients(100):
    realEstateSystem.addClient(random_client)
    if(random_client.client_id == 55):
        client_to_test = random_client
for random_agent in Agent.create_random_agents(10):
    realEstateSystem.addAgent(random_agent) 
    if(random_agent.agent_id == 5):
        agent_to_test = random_agent
   


class TestRealEstateSystem(unittest.TestCase):
    
    #APPOINTMENTS SHOULD BE PICKED IN CORRECT ORDER
    #ORDER GOES IN: 3, 2, 1, 4, 5
    #ORDER SHOULD COME OUT: 3, 2, 1, 4, 5
    @patch('sys.stdout', new_callable=StringIO)  
    def test_get_first_appointment_id(self, mock_stdout):

        appointments = Appointment.create_appointment_objects()
        for appointment in appointments:
            realEstateSystem.scheduleAppointment(appointment) 

        # Assuming `realEstateSystem.getFirstAppointment().getAppointmentID()` returns 101
        expected_output = "3\n2\n1\n4\n5\n"  # Expected print output
        
        for _ in range(5):
            print(realEstateSystem.getFirstAppointment().getAppointmentID())

        self.assertEqual(mock_stdout.getvalue(), expected_output)  # Compare output

    
    #OBJECT STORED IN BINARY TREE FOR REAL ESTATE PROPERTY SHOULD WORK
    #FETCHING FROM BINARY TREE SHOULD GIVE RIGHT RESULT
    #PROPERY 23 IS RANDOMLY CHOSEN PROPERTY TO TEST
    def test_get_property_23(self):
        property_23 = realEstateSystem.getProperty(23)
        
        # Expected attributes of the property
        expected_property = property_to_test

        # Check that the appointment properties match
        self.assertEqual(property_23.property_id, expected_property.property_id)
        self.assertEqual(property_23.price, expected_property.price)
        self.assertEqual(property_23.amenities, expected_property.amenities)
        self.assertEqual(property_23.property_type, expected_property.property_type)
        self.assertEqual(property_23.location, expected_property.location)
        self.assertEqual(property_23.latitude, expected_property.latitude)
        self.assertEqual(property_23.longitude, expected_property.longitude)

    # OBJECT STORED IN BINARY TREE FOR AGENT SHOULD WORK
    # AGENT 5 IS RANDOMLY CHOSEN AGENT TO TEST
    # FETCHING FROM BINARY TREE SHOULD GIVE RIGHT RESULT
    def test_get_agent_5(self):
        # Fetch agent 5 from the system
        agent_5 = realEstateSystem.getAgent(5)

        # Expected agent attributes (initialize this with the expected agent object)
        expected_agent = agent_to_test  # Replace with your actual expected agent object

        # Check that the agent properties match
        self.assertEqual(agent_5.agent_id, expected_agent.agent_id)
        self.assertEqual(agent_5.name, expected_agent.name)
        self.assertEqual(agent_5.assigned_properties, expected_agent.assigned_properties)
    

    # OBJECT STORED IN BINARY TREE FOR CLIENT SHOULD WORK
    # CLIENT 55 IS RANDOMLY CHOSEN TO TEST
    # FETCHING FROM BINARY TREE SHOULD GIVE RIGHT RESULT
    def test_get_client_55(self):
        # Fetch client 55 from the system
        client_55 = realEstateSystem.getClient(55)

        # Expected client attributes (initialize this with the expected client object)
        expected_client = client_to_test  # Replace with your actual expected client object

        # Check that the client properties match
        self.assertEqual(client_55.client_id, expected_client.client_id)
        self.assertEqual(client_55.name, expected_client.name)
        self.assertEqual(client_55.preferred_amenities, expected_client.preferred_amenities)
        self.assertEqual(client_55.preferred_price_min, expected_client.preferred_price_min)
        self.assertEqual(client_55.preferred_price_max, expected_client.preferred_price_max)
        self.assertEqual(client_55.preferred_property_type, expected_client.preferred_property_type)



if __name__ == "__main__":
    unittest.main()








