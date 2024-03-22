from exhibition import Exhibition
from event import Event

def openNewExhibition():
    exhibition = Exhibition ("2024-03-11", "2024-05-21","Hall A")
    assert exhibition.startDate == "2024-03-11", "exhibition start date should be set"
    assert exhibition.endDate == "2024-05-21", "exhibition end date should be set"
    assert exhibition.location == "Hall A", "exhibition location should be set"

def openNewEvent():
    event = Event ("2024-06-11", "2024-07-20","Outdoor","Concert",355.0)
    assert event.eventType == "Concert", "event type should be set to Concert"
    assert event.specialPrice == 355.0, "special price event price should be set"

if __name__=="__main__":
    openNewExhibition()
    print("Passs Testing Opening New Exhibition")
    openNewEvent()
    print("Pass Testing Opening New Event")



