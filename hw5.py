#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys

class AdjacencyListGraph(object):
    """Adjacency list implementation of undirected weighted graph. """

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_edge(self, u, v, weight):
        """Add nodes and edges."""
        if u not in self.edges:
            self.edges[u] = {}
            self.nodes.append(u)
        if v not in self.edges:
            self.edges[v] = {}
            self.nodes.append(v)
        # undirected weighted edge, no duplicated
        if (u not in self.edges[v].keys()) and (v not in self.edges[u].keys()):
            self.edges[u][v] = weight
            self.edges[v][u] = weight

def Dijkstra(graph, start):
    # Initialization
    n = len(graph.nodes)
    dist_vector = n * [1000000]
    intree = n * [False]
    parent = n * [-1]
    dist_min = 1000000
    # Starting from given vertex (tranform to 0-based)
    dist_vector[start-1] = 0
    u = start
    while intree[u-1] == False:
        intree[u-1] = True
        edges_u = graph.edges[u]
        for v in edges_u.keys():
            if dist_vector[v-1] > dist_vector[u-1] + graph.edges[u][v]:
                dist_vector[v-1] = dist_vector[u-1] + graph.edges[u][v]
                parent[v-1] = u-1
        u = start
        dist_min = 1000000
        for x in graph.nodes:
            if intree[x-1] == False and dist_min > dist_vector[x-1]:
                dist_min = dist_vector[x-1]
                u = x
    # print dist_vector
    return dist_vector

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: inputfile'
        sys.exit(1)

    graph = AdjacencyListGraph()
    with open(args[0]) as fileobject:
        for line in fileobject:
            line = line.strip().split()
            start = line[0]
            for x in xrange(1, len(line)):
                edge = tuple(line[x].split(','))
                # print int(start), int(edge[0]), int(edge[-1])
                graph.add_edge(int(start), int(edge[0]), int(edge[-1]))
    # Test output
    # print graph.nodes
    # for u in graph.edges.keys():
    #     for v, weight in graph.edges[u].items():
    #         print u, v, weight
    dist_dict = Dijkstra(graph, 1)
    # Print result
    # print '7', dist_dict[7-1]
    # print '37', dist_dict[37-1]
    # print '59', dist_dict[59-1]
    # print '82', dist_dict[82-1]
    # print '99', dist_dict[99-1]
    # print '115', dist_dict[115-1]
    # print '133', dist_dict[133-1]
    # print '165', dist_dict[165-1]
    # print '188', dist_dict[188-1]
    # print '197', dist_dict[197-1]
    # print dist_dict[7-1],',',dist_dict[37-1],',',dist_dict[59-1],',',dist_dict[82-1],',',dist_dict[99-1],',',dist_dict[115-1],',',dist_dict[133-1],',',dist_dict[165-1],',',dist_dict[188-1],',',dist_dict[197-1]

if __name__ == '__main__':
    main()