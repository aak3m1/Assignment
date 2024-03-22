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
        self.visitorGroupSize = visitorGroupSize
        #variable that stores the name of the tour guide as string
        self.guideName = guideName

    #method is intended to handle the scheduling of a tour
    #A placeholder and does not contain any implementation
    def scheduleTour(self):
        #place holding for future tour scheduling logic
        pass


    #method is intendend to display the details of the tour
    #A placeholder and does not contain any implementation
    def displayTourDetails(self):
        #placeholder for a future code to display tour details
        pass
