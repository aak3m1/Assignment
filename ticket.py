class Ticket:
    def __init__ (self, ticketID, purchaseDate, eventDate, price, visitorCategory):
        self.ticketID = ticketID
        self.purchaseDate = purchaseDate
        self.eventDate = eventDate
        self.price = price
        self.visitorCategory= visitorCategory

    def calculatePrice(self):
        pass
    def printTicketDetails(self):
        pass

