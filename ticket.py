class Ticket:
    """
    this class represents the details about tge ticjer museum ticket
    """
    #constructor intitalizes new ticket instance with impportant ticket information
    def __init__ (self, ticketID, purchaseDate, eventDate, price, visitorCategory):
        #identifier for the ticket
        self.ticketID = ticketID
        #date the ticket was purchased
        self.purchaseDate = purchaseDate
        #date of the ticket valid for the event or exhibition
        self.eventDate = eventDate
        #price of the ticker in Dirhams (DHS)
        self.price = price
        #catecory of the visitor (Adult, Child, Senior or a student)
        self.visitorCategory= visitorCategory

    #place holder for calculating the price of the ticket
    def calculatePrice(self):
        if self.visitorCategory in ['Child','Teacher','Senior']:
            return 0 #free tickets for specific categories
        elif self.visitorCategory == 'Group':
            return self.price * 0.5 #50% discount for groups
        else:
            return self.price * 1.05 #applying 5% VAT

    #print the details of the ticket
    def printTicketDetails(self):
        #printing ticket details
        print("Ticket Details:")
        print(f"Ticket ID:{self.ticketID}") #printing the ID
        print(f"Purchase Date:{self.purchaseDate}") #printing the purchase date
        print(f"Event Date:{self.eventDate}") #prining the event datw
        print(f"Price: DHS {self.price:.2f}") # floating point number with two decimal places.
        print(f"Visitor Category: {self.visitorCategory}") #prinitng the visitor cateogry






