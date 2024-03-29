class Artwork:
    """
    this class represents the artwork in the museum collection
    """
    #constructor for the artwork class that intialized the artwork with its details
    def __init__ (self, title,artist,dateOfCreation, exhibitionLocation, historicalSignificance):
        #varaible stores the title of the artwork
        self.title = title
        #variable stores the name of the artist who created the artwork
        self.artist = artist
        #variable stores the data when the artwork was created
        self.dateOfCreation = dateOfCreation
        #variable stores the current location od the artwork within the museum
        self.exhibitionLocation = exhibitionLocation
        #varaible stores information about the artwork historical importance
        self.historicalSignificance = historicalSignificance

    #methods is intended updating the artwork information
    #placeholder does not contins any implementation
    def updateArtworkInfo(self, newLocation= None, newSignificance=None):
        #place holds future logic update artwork details
        #checks if the new location is providedm and update if so
        if newLocation:
            self.exhibitionLocation = newLocation
        #checks if the new historucal significance information is provided and update
        if newSignificance:
            self.historicalSignificance = newSignificance
        #print that it have been updated
        print(f"Artwork {self.title} updated")


    #methods is intended to display information about the artwork
    def displayArtwork (self):
        print(f"Title:{self.title}") #printing the title of the artwork
        print(f"Artist:{self.artist}") #prinitng the name of the artist
        print(f"Year:{self.dateOfCreation}") #printing the date of creation
        print(f"Location:{self.exhibitionLocation}") #printing the location
        print(f"Significance:{self.historicalSignificance}") #printing the historical significance of the artwork
