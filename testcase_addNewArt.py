#importing the artwoek and room classes adding new artwork to a room
from artwork import Artwork
from room import Room

def addNewArt():
    #instance room with the room number and first floor
    room = Room ("101",1)
    #artwork found in google
    artwork = Artwork ("Mona Lisa", "Leonardo da Vinci","1503","Gallery","Mysterious woman with enigmatic smile")

    #artwork to the previously defined room
    room.addArtwork(artwork)

    #check if the artwork is added
    if artwork in room.artworks:
        print("Artwork Added successfully")
    else:
        print("Failed to add artwork")

    #print a message indicating that the details of the added artwork woill be displayed nect
    print("Display added artwork details: ")
    #methods of the artwork to print its details
    artwork.displayArtwork()

#if statement to check if this script is being run as the main program and not being imported by another module
if __name__== "__main__":
    #if this is the main program it will execute the addnewart function
    addNewArt()
    print("")
    print ("Adding new artwork pass")