from tour import Tour
from visitor import Visitors

def scheduleTourAddvisitor():
    tour = Tour ("T001", "2024-03-27","30","Ahmed Alhosani")

    visitor1 = Visitors("Alia",30,"Adult")
    visitor2 = Visitors("Sarah",7,"Child")

    tour.addVisitor(visitor1)
    tour.addVisitor(visitor2)

    tour.displayTourDetails()

    assert visitor1 in tour.visitors, "Visitor 1 should be added to the tour"
    assert visitor2 in tour.visitors, "Visitor 2 should be added to the tour"

    print("The tour Scheduling and adding visitior is passed ")

if __name__=="__main__":
    scheduleTourAddvisitor()