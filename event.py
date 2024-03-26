#importing the exhibition class from the exhibition module to extend it
from exhibition import Exhibition
import datetime
class Event(Exhibition):
    """
    this class is a subclass of exhibition and represents a special
    type of exhibition, such as concerts or fundraises
    """
    #constructor event that intialize for event-specific attributes along with inherited attributes
    def __init__(self, startDate, endDate, location, eventType, specialPrice):
        #attributes from the parent exhibition class by calling its constructor
        super().__init__(startDate, endDate, location)
        #variable stores the type of event (concert or fundraisers)
        self.eventType = eventType
        #variable stores the price of the event as a float
        #input is converted to float to ensure numerical operation can be prefformed
        self.specialPrice = float(specialPrice)

    #method is intended to handle the logistic of sceduling an event
    #place holds and does not contain any implementaitopn
    def scheduleEvent(self):
        #placeholder for futire event scheduiling logic
        today= datetime.date.today() #todays date
        startDate= datetime.datetime.strptime(self.startDate, "%Y - %m - %d").date() #converting start date string to date object
        if startDate < today:
            print("Error: event canoot be scheduled in the past") #error if the event start date is in the past
        else:
            print(f"Event '{self.eventType}' successfully scheduled from {self.startDate} to {self.endDate}")#confirming

    #method is intended to output the details of the event
    def displayEventDetails(self):
        super().displayExhibition() #display details inherited from the exhibition class
        print(f"Event Type: {self.eventType}") #printing type
        print(f"Special Price: {self.specialPrice}") #printing price