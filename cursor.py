#-*- encoding: utf-8
"""
Cursor object for storing cursor data.
"""
    
class Cursor:
    def __init__(self, x=0, y=0):
        # Handle coords as a tuple
        if type(x) == type((0,)):
            x,y = x
            self.x = x
            self.y = y
        # Handle coords from existing Cursor
        elif isinstance(x, Cursor):  # Handle arguments as a cursor
            self.x = x.x
            self.y = x.y
        # Handle coords as plain ints
        else:
            self.x = x
            self.y = y

    def get_x(self):
        return x
        
    def get_y(self):
        return y
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def __getitem__(self, i):
        # TODO: Deprecate in favor of proper access methods.
        """Get coordinates with list indices."""
        if i == 0:
            return self.x
        elif i == 1:
            return self.y

    # Deprecated
    #def __setitem__(self, i, v):
    #    # TODO: Deprecate in favor of proper access methods.
    #    """Set coordinates with list indices."""
    #    if i == 0:
    #        self.x = v
    #    elif i == 1:
    #        self.y = v

    def __eq__(self, item):
        """Check for equality."""
        if isinstance(item, Cursor):
            if item.x == self.x and item.y == self.y:
                return True
        return False

    def __ne__(self, item):
        """Check for unequality."""
        if isinstance(item, Cursor):
            if item.x != self.x or item.y != self.x:
                return False

    def tuple(self):
        """Return cursor as a tuple."""
        return (self.x, self.y)
