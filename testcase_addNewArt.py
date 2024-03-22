from artwork import Artwork
from room import Room

def addNewArt():
    room = Room ("101",1)
    artwork = Artwork ("Mona Lisa", "Leonardo da Vinci","1503","Gallery","Mysterious woman with enigmatic smile")

    room.addArtwork(artwork)
    assert artwork in room.artworks, "Artwork should be added to the room's list of artworks"

if __name__== "__main__":
    addNewArt()
    print ("Adding new artwork pass ")