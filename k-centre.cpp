#include <vector>
#include <iomanip> // time
#include <memory>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>



#define MAX_VALUE 50000


class graph{

class node {
    public:
    float x, y; 

    node() {
        x=0; y=0;
    }
    node(node &other) {
        x=other.x; y=other.y;
    }
    node(std::shared_ptr<graph::node> other) {
        x=other->x; y=other->y;
    }
};

public:
std::vector<std::shared_ptr<node>> nodes;
std::set<std::shared_ptr<node>> centers;
float d(std::shared_ptr<node> lhs, std::shared_ptr<node> rhs) {
    return std::sqrt((lhs->x-rhs->x)*(lhs->x-rhs->x)+(lhs->y-rhs->y)*(lhs->y-rhs->y));
}

void insertNode() {
    float CURRy = (double)(rand()) / (double)(RAND_MAX/MAX_VALUE);
    float CURRx = (double)(rand()) / (double)(RAND_MAX/MAX_VALUE);
    std::shared_ptr<node> currptr(new node());
    currptr->y = CURRy;
    currptr->x = CURRx;

    this->nodes.push_back(currptr);
}
graph(int AMOUNT_OF_NODES) {
std::srand(std::time(nullptr));
    
    for (size_t i = 0; i < AMOUNT_OF_NODES; i++)
        insertNode();            
}

float distToCenters(std::shared_ptr<node> currnode) {
    float min = 900000000000; 
    for (auto i : centers) {
        float currd = d(currnode, i);
        if (currd < min) {
            min = currd; 
        }
    }
    return min;
}

void insertfarthestnode() {
    float CURRd = 0;
    float MAXd = 0;
    std::shared_ptr<node> MAXnode = nodes.at(0);

    // for each node calculate min distance to the center set
    // take the node with the maximum min distance
    for (auto i : nodes)
    {
        float d = distToCenters(i);
        if (d>MAXd) {
            MAXd = d;
            MAXnode = i;
        }
    }
    centers.insert(std::make_shared<node>(MAXnode));
}

void kcentre(int k) {
    centers.clear();
    centers.insert(nodes.at(15));
    while (centers.size()!=k) {
        insertfarthestnode();
    }
}
};

void driver(int k, int AMOUNT_OF_NODES) {
graph G(AMOUNT_OF_NODES); 
std::vector<double> x(AMOUNT_OF_NODES), y(AMOUNT_OF_NODES), xk(k), yk(k);
for (size_t i = 0; i < G.nodes.size(); i++)
{
    x.push_back(G.nodes.at(i)->x);
    y.push_back(G.nodes.at(i)->y);
}
G.kcentre(k);
for (auto i : G.centers)
{
    xk.push_back(i->x);
    yk.push_back(i->y);
}
// Print the graph: vector x, y are nodes, vector xk, xy are centers
}