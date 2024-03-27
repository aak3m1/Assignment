class Tour:
    """
    This class represents the details of a museum tour
    """
    #Constructor for the tour class with intializiation for tour attributes
    def __init__ (self, tourID, date, visitorGroupSize, guideName):
        #variable that stres the unique identifiers for the tour
        self.tourID = tourID
        #variable that stores the data of the tour string
        self.date= date
        #variable the visitor group size to store the number or visitor
        #in the tour group as an integer
        self.visitorGroupSize = int(visitorGroupSize) #convert to int
        #variable that stores the name of the tour guide as string
        self.guideName = guideName
        #list to store visitors
        self.visitors = []

    #method is intended to handle the scheduling of a tour
    #A placeholder and does not contain any implementation
    def addVisitor(self,visitor):
        #place holding for future tour scheduling logic
        if len(self.visitors) < self.visitorGroupSize:
            self.visitors.append(visitor)
            print(f"{visitor.name} has been added to the tour {self.tourID}")
        else:
            print("Tour is full capacity")


    #method is independent to display the details of the tour
    #A placeholder and does not contain any implementation
    def displayTourDetails(self):
        #placeholder for a future code to display tour details
        print(f"Tour ID: {self.tourID}")
        print(f"Date: {self.date}")
        print(f"Group Size: {self.visitorGroupSize}")
        print(f"Guide Name: {self.guideName}")
        print("Visitors: ")
        for visitor in self.visitors:
            print(f"- {visitor.name}")



