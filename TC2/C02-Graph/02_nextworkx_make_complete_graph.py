import networkx as nx
import sys
import matplotlib
#matplotlib.use('TkAgg')
matplotlib.interactive(True)


def all_paris(nodes):
    for i, u in enumerate(nodes):
        for j,v in enumerate(nodes):
            if i>j:
                yield(u,v)



def make_complete_graph(n):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(all_paris(nodes))
    return G


if __name__ == '__main__':
    G = make_complete_graph(10)
    print(G.nodes())
    nx.draw_circular(G,
     node_color='green',
     node_size=1000,
     with_labels=True)
    
    a =input()
    

    