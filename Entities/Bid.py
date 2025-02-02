class Bid:
    def __init__(self, bid_id, client, property_id, bid_amount):
        self.bid_id = bid_id
        self.client = client
        self.property_id = property_id
        self.bid_amount = bid_amount

    def __str__(self):
        return f"Bid ID: {self.bid_id}, Client: {self.client}, Property ID: {self.property_id}, Bid Amount: ${self.bid_amount}"

