from Kruskal.Vertex import Vertex
from Kruskal.Edge import Edge
from Kruskal.Algorithm import Algorithm

vertex1 = Vertex("A")
vertex2 = Vertex("B")
vertex3 = Vertex("C")
vertex4 = Vertex("D")
vertex5 = Vertex("E")
vertex6 = Vertex("F")

edge1 = Edge(2,vertex1, vertex2)
edge2 = Edge(4,vertex1, vertex4)
edge3 = Edge(4,vertex2, vertex3)
edge4 = Edge(4,vertex2, vertex4)
edge5 = Edge(3,vertex2, vertex5)
edge6 = Edge(1,vertex2, vertex6)
edge7 = Edge(5,vertex3, vertex6)
edge8 = Edge(2,vertex4, vertex5)
edge9 = Edge(5,vertex5, vertex6)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)

algorithm = Algorithm()
algorithm.constructSpanningTree(vertexList, edgeList)