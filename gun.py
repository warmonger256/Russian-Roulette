# Gun.py

# This function contains everything there is to know in order to use and control
# the gun that is supposed to be used in the game.

import random

class Gun():
    """ The gun is actually a list with a size of 6, and within its index are
        randomly placed 1's, a 1 connotates a filled chamber while a 0 is
        otherwise.

    """
    def __init__():
        self.cylinder = [] # Initialize the empty cylinder
        
        while len(self.cylinder) < 6: # While we don't have 6 empty chambers yet
            self.cylinder.append(0)

        # Debugging message to check if we have the correct number of empty
        # cylinders
        print 'We have ' + len(self.cylinder) + ' empty cylinders in the gun'

        # Now we will get a random number, and use that as the index number where
        # we will put the 1 value (loaded bullet).

        random.seed()
        self.bulletIndex = random.randint(1,6)
        
        # Now let's put that bullet in the selected index.
        self.cylinder.insert(self.bulletIndex, 1)

        # Now let's put the cylinder location into the first cylinder.
        self.currentCylinder = 1

    def shoot():
        """ 'Shoots' the gun. While this is in effect, the gun just puts the
            value of the current cylinder into a buffer, moves the location
            of the current cylinder (rotating the cylinder), the returns
            the buffered value.

        """
        cylinderValue = self.cylinder[self.currentCylinder] # Put it in the buffer
        self.CurrentCylinder += 1 # Rotate the cylinder

        return cylinderValue
