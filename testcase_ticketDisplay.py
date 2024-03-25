#importing ticket class from the ticket module
from ticket import Ticket

def displayPayment():
    tickets = [
        Ticket ("AA104-1145-2", "2024-03-22", "2024-04-01", 63.0, "Adult"),
        Ticket("AB105-2231-4","2024-04-20", "2024-04-29",63.0,"Adult")
    ]
    totalPrice = 0
    for i, ticket in enumerate(tickets, start=1):
        print(f"Ticket {i}:")
        ticket.printTicketDetails()
        totalPrice += ticket.price
        print("")
    print("")
    print(f"Total Price for {len(tickets)} tickets: DHS {totalPrice:.2f}")



if __name__== "__main__":
    displayPayment()
    print("Passed displaying ticket details")