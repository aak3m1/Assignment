from exhibition import Exhibition

class Event(Exhibition):
    def __init__(self, startDate, endDate, location, eventType, specialPrice):
        super().__init__(startDate, endDate, location)
        self.eventType = eventType
        self.specialPrice = float(specialPrice)
    def scheduleEvent(self):
        pass
    def displayEventDetails(self):
        pass
