class Exhibition:
    """
    this class represents an exhibition within the museum. Exhibition are teporary events
    """
    #exhibition class that intiazlies start date, end date and loction
    def __init__ (self,startDate, endDate, location):
        #variable that stores the date when the exhibition is scheduled to start
        self.startDate = startDate
        #variable stores the date when the exhibition is scheduled to end
        self.endDate= endDate
        # variable stores the location within the museum where the exhibition is held
        self.location= location

    #method to handle logistic of scheduling an exhibition
    def scheduleExhibition(self):
        print(f"Exhibition scheduled from {self.startDate} to {self.endDate} at {self.location}.")

    #method to display information about the exhibition
    def displayExhibition(self):
        print(f"Exhibition Start Date: {self.startDate}") #printing start date
        print(f"Exhibition End Date: {self.endDate}") #printing end date
        print(f"Exhibition Location: {self.location}") #printing location


