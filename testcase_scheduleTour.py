#Importing the tour and the visitor classes
from tour import Tour
from visitor import Visitors


#define a function to test adding visitors to a tour and displaying
def scheduleTourAddvisitor():
    #create a tour instance with specific details
    tour = Tour ("T031", "2024-03-27","30","Ahmed Alhosani")

    #create two visitor instances with their details
    visitor1 = Visitors("Alia",30,"Adult")
    visitor2 = Visitors("Sarah",7,"Child")

    #add two visitors to the tour
    tour.addVisitor(visitor1)
    tour.addVisitor(visitor2)

    #displaying details
    tour.displayTourDetails()

    #asserting checks to ensure both visitors were added
    assert visitor1 in tour.visitors, "Visitor 1 should be added to the tour"
    assert visitor2 in tour.visitors, "Visitor 2 should be added to the tour"

    print("")
    #print success message
    print("The tour Scheduling and adding visition is successful ")

if __name__=="__main__":
    #execute the test function
    scheduleTourAddvisitor()