
class Room:
    """
    this class represents a room within the musueum
    """
    #intializes the room with a number and floor assignment
    def __init__(self,roomNumber,floor):
        #variable stores identifiers for the room
        self.roomNumber = roomNumber
        #variable indicate which floor roo, is located within the museum
        self.floor= floor
        #variable list to store instances of Artwork that are located in this room
        self.artworks=[]

    #method adds an artwork to the room list artworks
    def addArtwork(self,artwork):
        #artwork object passed as an argument is appened to the list of artwork in the room
        self.artworks.append(artwork)
        print(f"Artwork titled '{artwork.title}' added to Room {self.roomNumber} ")

    #methods removes an artwork from the rooms list of artwork
    def removeArtwork(self,artwork):
        try:
            self.artworks.remove(artwork)
            print(f"Artwork titled '{artwork.title}' removed from Room {self.roomNumber}")
        except ValueError:
            print(f"Artwork titled '{artwork.title}' nt found in Room {self.roomNumber}")

    def displayArtworkInRoom(self):
        print(f"Artworks in room {self.roomNumber} on Floor {self.floor}: ")
        for artwork in self.artworks:
            print(f"-{artwork.title} by {artwork.artist}")