from visitor import Visitors
from ticket import Ticket

def ticketPurchase():
    visitor = Visitors("Afra Abduljalil",20,"Adult")
    ticket = Ticket ("A11311", "2024-03-22","2024-04-01",63.0,"Adult")

    visitor.purchaseTicket(ticket)
    assert ticket in visitor.tickets, "Tickets should be added to visitors list of tickets"

if __name__ == "__main__":
    ticketPurchase()
    print("passed the ticket Purchase")