#importing ticket class from the ticket module
from ticket import Ticket
def displayPayment():
    #list of ticket objects each represents a ticket purchase by a vistor
    tickets = [
        Ticket ("AA104-1145-2", "2024-03-22", "2024-04-01", 63.0, "Adult"),
        Ticket("AB105-2231-4","2024-04-20", "2024-04-29",63.0,"Adult")
    ]
    #variable to hold the total price of all tickets
    totalPrice = 0

    #for loop for each ticket in the list, enumerating to get both the index (i) and the ticket object
    for i, ticket in enumerate(tickets, start=1):
        #printing index i to number each ticket
        print(f"Ticket {i}:")
        #calling the printing ticket details method of the ticket object to display its details
        ticket.printTicketDetails()
        #adding the price of the current ticket to the total price
        totalPrice += ticket.price
        #empty line to space betwewen the ticket details
        print("")
    print("")
    #printing the total prive foe all tickets
    print(f"Total Price for {len(tickets)} tickets: DHS {totalPrice:.2f}")


#checking if it is running
if __name__== "__main__":
    displayPayment()
    #printing a message indecating that the script has sucssesfully completed
    print("Passed displaying ticket details")