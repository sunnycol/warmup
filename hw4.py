#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys

class AdjacencyListGraph(object):
    """Adjacency list implementation based on the slides of
    Social Network Analysis in Python on Europython 2012"""

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.num_edges = 0

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.edges[node] = []
        else:   # do nothing if node already exists
            pass

    def add_edge(self, u, v):
        """Add nodes and edges. Note that no duplicated edge
        is allowed in this method"""
        if u not in self.edges:
            self.edges[u] = []
            self.nodes.append(u)
        if v not in self.edges:
            self.edges[v] = []
            self.nodes.append(v)
        if (u not in set(self.edges[v])) and (v not in set(self.edges[u])):
            self.edges[v].append(u)
            self.edges[u].append(v)
            self.num_edges += 1

    # def del_edge(self, u, v):
    #     if u not in self.edges.keys():
    #         print '%s is not in edge dict!' % u
    #         return
    #     if v not in self.edges.keys():
    #         print '%s is not in edge dict!' % v
    #         return
    #     if (self.edges[u].count(v) > 0) and (self.edges[v].count(u) > 0):
    #         self.edges[u].remove(v)
    #         self.edges[v].remove(u)
    #         # print 'del_edge here!'
    #         self.num_edges -= 1
    #     else:
    #         print 'unmatched edge between node %s and %s' % (u, v)

    def merge_node(self, u, v):
        """ Assume u and v to be distinct. """
        # merge two edge lists
        self.edges[u] = self.edges[u] + self.edges[v]
        # empty v
        self.edges[v] = []
        # remove v in node list
        self.nodes.remove(v)
        # remove self-loop
        while (v in self.edges[u]) and (u in self.edges[u]):
            self.edges[u].remove(v)
            self.edges[u].remove(u)
            # print 'merge_node here!'
            self.num_edges -= 1
        # replace v with u for all nodes
        for key in self.edges.keys():
            while v in self.edges[key]:
                self.edges[key].remove(v)
                self.edges[key].append(u)
