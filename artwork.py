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
    def updateArtworkInfo(self):
        #place holds future logic update artwork details
        pass

    def displayArtwork (self):
        pass
