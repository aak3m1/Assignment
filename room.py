class Room:
    def __init__(self,roomNumber,floor):
        self.roomNumber = roomNumber
        self.floor= floor
        self.artworks=[]

    def addArtwork(self,artwork):
        self.artworks.append(artwork)

    def removeArtwork(self,artwork):
        self.artworks.remove(artwork)