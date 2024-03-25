#importing the visitor class from the visitor model and so on for the ticket
from visitor import Visitors
from ticket import Ticket


def ticketPurchase():
    # instance of the vistitor with attributes
    visitor = Visitors("Afra Abduljalil",20,"Adult")
    #instance of the ticket with the attributes
    ticket = Ticket ("A11311", "2024-03-22","2024-04-01",63.0,"Adult")

    #calling the methods to simulate the visitor
    visitor.purchaseTicket(ticket)
    #asserting the ticket object
    assert ticket in visitor.tickets, "Tickets should be added to visitors list of tickets"

    #printing
    print("")
    print("Dispaying purchased ticket details: ")
    ticket.printTicketDetails()

#ticket purcahse is withing the main
if __name__ == "__main__":
    print("")
    ticketPurchase()
    print("Passed the ticket Purchase")