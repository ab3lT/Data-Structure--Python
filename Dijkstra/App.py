from Dijkstra.Vertex import Vertex
from Dijkstra.Edge import Edge
from Dijkstra.Algorithm import Algorithm


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")
node4 = Vertex("D")
node5 = Vertex("E")
node6 = Vertex("F")
node7 = Vertex("G")
node8 = Vertex("H")

edge12 = Edge(5, node1, node2)
edge15 = Edge(9, node1, node5)
edge18 = Edge(8, node1, node8)
edge23 = Edge(12, node2, node3)
edge24 = Edge(15, node2, node4)
edge28 = Edge(4, node2, node8)
edge34 = Edge(3, node3, node4)
edge37 = Edge(11, node3, node7)
edge47 = Edge(9, node4, node7)
edge56 = Edge(4, node5, node6)
edge57 = Edge(20, node5, node7)
edge58 = Edge(5, node5, node8)
edge63 = Edge(1, node6, node3)
edge67 = Edge(13, node6, node7)
edge83 = Edge(7, node8, node3)
edge86 = Edge(6, node8, node6)


node1.adjacenciesList.append(edge12)
node1.adjacenciesList.append(edge15)
node1.adjacenciesList.append(edge18)
node2.adjacenciesList.append(edge23)
node2.adjacenciesList.append(edge24)
node2.adjacenciesList.append(edge28)
node3.adjacenciesList.append(edge34)
node3.adjacenciesList.append(edge37)
node4.adjacenciesList.append(edge47)
node5.adjacenciesList.append(edge56)
node5.adjacenciesList.append(edge57)
node5.adjacenciesList.append(edge58)
node6.adjacenciesList.append(edge63)
node6.adjacenciesList.append(edge67)
node8.adjacenciesList.append(edge83)
node8.adjacenciesList.append(edge86)

vertexList = {node1, node2, node3, node4, node5, node6, node7, node8}

algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortestPathTo(node7)