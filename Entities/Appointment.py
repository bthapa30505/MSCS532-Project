from datetime import datetime

# Appointment Class
class Appointment:
    def __init__(self, appointment_id: int, client: str, agent: str, property_id: int, date_time: datetime):
        self.appointment_id = appointment_id
        self.client = client
        self.agent = agent
        self.property_id = property_id
        self.date_time = date_time  # Store as datetime object

    def getAppointmentID(self):
        return self.appointment_id 

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}\n" \
               f"Client: {self.client}\n" \
               f"Agent: {self.agent}\n" \
               f"Property ID: {self.property_id}\n" \
               f"Date and Time: {self.date_time.strftime('%Y-%m-%d %H:%M:%S')}"  # Corrected strftime

    @staticmethod
    def create_appointment_objects():
        """Creates and returns a list of Appointment objects."""
        client_agent_property_list = [
            (3, 11, 1, 10),
            (2, 12, 2, 20),
            (1, 13, 3, 30),
            (4, 14, 4, 40),
            (5, 15, 5, 50)
        ]
        appointments = []
        for appointmentId, client_id, agent_id, property_id in client_agent_property_list:
            current_time = datetime.now()  # Keep as datetime object
            appointment = Appointment(appointmentId, client_id, agent_id, property_id, current_time)
            appointments.append(appointment)
        return appointments
