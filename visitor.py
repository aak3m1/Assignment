class Visitors:
    """
    this class is a visitor constructor
    where it initializes a new instance of the class.
    """
    def __init__(self,name,age, category):
        #instance variable to store the name of the visitor
        self.name = name #as a string
        #instance variable to store the age of the vistor
        self.age = age #as a integer
        #instance variable to store category of the visitor
        self.category = category #(Adult, Child, Senior)
        #instance variable list that will store the tickets purchase
        self.tickets = []

    #method to placehold for registring visitors
    def registerVisitors (self):
        #there is no implementation so pass
        pass

    #method allows a visitor to purhcase a ticket
    #then it will be added to the visitors list
    def purchaseTicket(self, ticket):
        #the ticket passed as a parameter is appened to the tickets list
        self.tickets.append(ticket)


