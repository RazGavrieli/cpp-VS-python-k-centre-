import random
import math
import matplotlib.pyplot as plt
MAX_VALUE = 50000
class node:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
class graph:
    def insertNode(self):
        currX = random.randint(0, MAX_VALUE)
        currY = random.randint(0, MAX_VALUE)
        currNode = node()
        currNode.x = currX
        currNode.y = currY
        self.nodes.append(currNode)

    def __init__(self, AMOUNT_OF_NODES) -> None:
        self.nodes = []
        self.centers = []
        for i in range(AMOUNT_OF_NODES):
            self.insertNode()

    def d(self, lhs: node, rhs: node) -> float:
        return math.sqrt((lhs.x-rhs.x)**2 + (lhs.y-rhs.y)**2)

    def distToCenters(self, currNode: node):
        min = 900000000000
        for i in self.centers:
            currentd = self.d(currNode, i)
            if currentd < min:
                min = currentd
        return min
    def insertfarthestnode(self):
        CURRd = 0
        MAXd = 0
        MAXnode = self.nodes[0]
        for i in self.nodes:
            d = self.distToCenters(i)
            if d > MAXd:
                MAXd = d
                MAXnode = i
        self.centers.append(MAXnode)

    def kcentre(self, k):
        self.centers.clear()
        self.centers.append(self.nodes[15]) # start at arbitrary node
        while len(self.centers) != k:
            self.insertfarthestnode()

    def printGraph(self):
        plt.scatter([i.x for i in self.nodes], [i.y for i in self.nodes], color="blue")
        plt.scatter([i.x for i in self.centers], [i.y for i in self.centers], color="red")
        plt.show()


if __name__ == "__main__":
    g = graph(50000)
    g.kcentre(15)
    g.printGraph()

        

