from ticket import Ticket
def printTicketDetails():
    ticket = Ticket ("AA104-1145-2", "2024-03-22","2024-04-01",63.0,"Adult")

    try:
        ticket.printTicketDetails()
        passed = True
    except Exception as e:
        passed = False

    assert passed, "print Ticket details wwithout errors"

if __name__ == "__main__":
    printTicketDetails
    print("passed ticket details")