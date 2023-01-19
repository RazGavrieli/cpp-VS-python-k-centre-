import timeit
import random
import cppyy
import math
cppyy.include("k-centre.cpp")
class node:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
class graph:
    def insertNode(self):
        currX = random.randint(0, 50000)
        currY = random.randint(0, 50000)
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


def claculateTime(AMOUNT_OF_NODES, k):
    start = timeit.default_timer()
    g = graph(AMOUNT_OF_NODES)
    g.kcentre(k)
    end = timeit.default_timer()
    pythonTime = end-start

    start = timeit.default_timer()
    cppyy.gbl.driver(k, AMOUNT_OF_NODES)
    end = timeit.default_timer()
    cppTime = end-start
    return cppTime, pythonTime

if __name__ == "__main__":
    import random
    import matplotlib.pyplot as plt
    size = 100000
    ptimes = []
    ctimes = []
    flag = 1
    numRangeStart = 5000
    i = numRangeStart
    timeToRun = 5
    start = timeit.default_timer()
    k = 4 # k-centre
    while flag:
        i+= 500
        end = timeit.default_timer()
        if end-start > timeToRun:
            print(end-start, timeToRun)
            flag = 0
        ct, pt = claculateTime(i,k)
        ptimes.append((i, pt))
        ctimes.append((i, ct))

    plt.plot(*zip(*ptimes), color="purple", label = "python")
    plt.plot(*zip(*ctimes), color="red", label = "cpp")
    plt.title("finding 2-approx for 4 centers with n nodes")
    plt.ylabel('time')
    plt.xlabel('n')
    plt.legend()
    plt.show()

        

