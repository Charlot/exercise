import networkx as nx
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
matplotlib.interactive(True)

def flip(p):
    return np.random.random()<p

def all_paris(nodes):
    for i, u in enumerate(nodes):
        for j,v in enumerate(nodes):
            if i>j:
                yield(u,v)


def random_pairs(nodes, p):
    for edge in all_paris(nodes):
        if flip(p):
            yield edge

def make_random_graph(n, p):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(random_pairs(nodes,p))
    return G

def reachable_node(G, start):
    """
    可到达点
    """
    seen = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))
    return seen

def is_connected(G):
    """
    是否连通图
    任意一点都可以到到全部点
    """
    start = next(iter(G))
    reachable = reachable_node(G, start)
    return len(reachable) == len(G)

def prob_connected(n,p,iters=100):
    tf = [is_connected(make_random_graph(n,p))
    for i in range(iters)
    ]
    return np.mean(tf)

if __name__ == '__main__':
    # G = make_random_graph(10,0.3)
    # print(G.nodes())
    # nx.draw_circular(G,
    #  node_color='green',
    #  node_size=1000,
    #  with_labels=True)

    # a =input()
    

    prob =prob_connected(10,0.23,10000)
    print(prob)
    
    