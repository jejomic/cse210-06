from game.casting.actor import Actor

"""A visible, moveable thing that participates in the game. 
    
    The responsibility of Asteroid is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        Actor class attributes
    """
class Asteroid(Actor):
    
    def __init__(self):
        super().__init__()
        self._message = ""
        
