# Interested in Java-like languages that specialize in visualization, and want to know where I got the class name from?
# Then take a look at the reference: https://processing.org/reference/PVector.html
class PVector:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
    
    def __str__(self):
        s = "[" + str(self.x) + "," + str(self.y) + "]:" + ("X" if self.data == 2 else "0")
        return s