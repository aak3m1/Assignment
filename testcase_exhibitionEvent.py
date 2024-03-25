#importing the necessary classes from
from exhibition import Exhibition
from event import Event

def openNewExhibition():
    #creating a new instance of the exhibition class
    exhibition = Exhibition ("2024-03-11", "2024-05-21","Hall A")
    #assert satement to ensure the exhibition details are corecctly srt
    assert exhibition.startDate == "2024-03-11", "exhibition start date should be set"
    assert exhibition.endDate == "2024-05-21", "exhibition end date should be set"
    assert exhibition.location == "Hall A", "exhibition location should be set"
    #displaying the details of the created exhibiton
    exhibition.displayExhibition()

def openNewEvent():
    #create a new instance of the event class
    print("")
    event = Event ("2024-06-11", "2024-07-20","Outdoor","Concert",355.0)
    #assert statement to ensure the details are correctly set
    assert event.eventType == "Concert", "event type should be set to Concert"
    assert event.specialPrice == 355.0, "special price event price should be set"
    #displaying the details of the event
    event.displayEventDetails()

#ensuring it will run only when it is the main program
if __name__=="__main__":
    #testing new exhibiton
    openNewExhibition()
    print("Pass Testing Opening New Exhibition")
    #testing new event
    openNewEvent()
    print("Pass Testing Opening New Event")



