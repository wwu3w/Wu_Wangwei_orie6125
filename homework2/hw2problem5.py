

class Node:

    def __init__(self, v):
        self.name = v
        self.adjacent = {}

    def get_name(self):
        return self.name

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_neighbor_weight(self,neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self,nv =0):
        self.n_vertex= nv #number of vertexes
        self.graph= {}

    def add_node(self, nd):
        self.n_vertex = self.n_vertex + 1
        new_node = Node(nd)
        self. graph[nd] = new_node
        return new_node

    def __iter__(self):
        return iter(self.graph.values())

    def add_edge(self,a,b, weight = 0):
        #a: from
        #b: to

        if a not in self.graph:
            self.add_node(a)
        if b not in self.graph:
            self.add_node(b)

        self.graph[a].add_neighbor(self.graph[b],weight)

    def bellman_ford(self, src):
        d = {}                  #distance
        for u in self.graph:
            d[u] = float("Inf") #distance

        d[src] = 0
        # loop for all the |V|-1 edges
        for i in range(self.n_vertex - 1):
            for u in self:
                u_name=u.get_name()
                for v in u.get_neighbors():
                    v_name = v.get_name()
                    wt = u.get_neighbor_weight(v)
                    if d[u_name] != float("Inf") and d[u_name] + wt < d[v_name]:
                        d[v_name] = d[u_name] + wt

        for u in self:
            u_name = u.get_name()
            for v in u.get_neighbors():
                v_name = v.get_name()
                wt = u.get_neighbor_weight(v)
                if d[u_name] != float("Inf") and d[u_name] + wt < d[v_name]:
                    print('Negative cycle!')

            return d
