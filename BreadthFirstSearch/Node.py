

class Vertex(object):
    # integer data -- private
    # boolean visited -- private
    # list[vertex] neighborList -- private
    visited = None
    
    def __init__(self, data):
        self.data = data
        self.nieghborList = []
        
    
    def addNeighbor(self, vertex):
        self.neighborList.append(vertex)
        
        
    def isVisited(self):
        pass