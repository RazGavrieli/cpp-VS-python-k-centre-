import timeit
import cppyy
import matplotlib.pyplot as plt

from kcentre import *
cppyy.include("kcentre.cpp")

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

def compareCPPvsPython(timeToRun, k,numRangeStart=5000,intervals=500):
    ptimes = []
    ctimes = []
    flag = 1
    i = numRangeStart
    start = timeit.default_timer()
    while flag:
        i += intervals
        end = timeit.default_timer()
        print(end-start)

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

if __name__ == "__main__":
    compareCPPvsPython(5, 5)