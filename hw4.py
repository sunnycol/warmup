#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys
import operator
import threading

class AdjacencyListGraph(object):
    """Adjacency list implementation of directed graph. """

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.clock = 0
        self.visited = {}
        self.postvisit = {}
        self.leaders = {}
        self.current_leader = 0

    def add_edge(self, u, v):
        """Add nodes and edges."""
        if u not in self.edges:
            self.edges[u] = []
            self.nodes.append(u)
            self.visited[u] = False
            self.postvisit[u] = 0
            self.leaders[u] = 0
        if v not in self.edges:
            self.edges[v] = []
            self.nodes.append(v)
            self.visited[v] = False
            self.postvisit[v] = 0
            self.leaders[v] = 0
        # Directed edge, no duplicated
        if (v not in set(self.edges[u])):
            self.edges[u].append(v)

def DFS(graph):
    # Decending ordering according to leaving time
    decending_order = sorted(graph.postvisit.iteritems(), key = operator.itemgetter(1))
    decending_order.reverse()
    for node, order in decending_order:
        if not graph.visited[node]:
            graph.current_leader = node
            graph = Explore(graph, node)
    return graph

def Explore(graph, node):
    graph.visited[node] = True
    graph.leaders[node] = graph.current_leader
    for dest in graph.edges[node]:
        if not graph.visited[dest]:
            graph = Explore(graph, dest)
    graph.postvisit[node] = graph.clock
    graph.clock = graph.clock + 1
    return graph

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: inputfile'
        sys.exit(1)

    graph = AdjacencyListGraph()
    rev_graph = AdjacencyListGraph()
    # Using context manager to load file line by line, this will automatically close the file as well
    with open(args[0]) as fileobject:
        for line in fileobject:
            line = line.strip().split()
            graph.add_edge(int(line[0]), int(line[1]))
            rev_graph.add_edge(int(line[1]), int(line[0]))
    # Postprocessing graph
    for node in graph.nodes:
        graph.visited[node] = False
        graph.postvisit[node] = 0
    for node in rev_graph.nodes:
        rev_graph.visited[node] = False
        rev_graph.postvisit[node] = 0
    # Kosaraju's Two-pass algorithm
    rev_graph = DFS(rev_graph)  # first run
    graph.postvisit = rev_graph.postvisit
    graph = DFS(graph)
    scc = {}
    for node, leader in graph.leaders.items():
        if leader in scc:
            scc[leader] = scc[leader] + 1
        else:
            scc[leader] = 1
    scc_list = (sorted(scc.iteritems(), key = operator.itemgetter(1)))
    scc_list.reverse()
    print scc_list

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    # main()


