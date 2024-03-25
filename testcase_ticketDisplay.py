#importing ticket class from the ticket module
from ticket import Ticket
def printTicketDetails():
    #instance of the ticket
    ticket = Ticket("AA104-1145-2", "2024-03-22", "2024-04-01", 63.0, "Adult")

    try:
        print("Attempting to display th ticket details... ")
        ticket.printTicketDetails()
        print ("Ticket deails displayed successfully" )
    except Exception as e:
        print(f"An error occured: {e}")
        assert False, "Failed to display"

if __name__== "__main__":
    printTicketDetails()
    print("-----")
    print("Passed ticket details")