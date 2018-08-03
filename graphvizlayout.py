from union_find import union_find
import graphviz
from graphviz import Digraph

class graph:

    def __init__(self,file):
        self.file = file
        self.u = union_find()
        self.compressionu = union_find()
        self.all_nodes = []
        self.all_edges = []
        self.lines = self.file.readlines()
        self.c = Digraph('G', filename = 'chipgraph', format = 'dot')

    def main(self):
        self.find_nodes()
        self.find_edges()
        x=0
        while x<len(self.all_nodes):
            used = False
            for y in self.all_edges:
                if y[0] == self.all_nodes[x] or y[1] == self.all_nodes[x]:
                    used = True
            if used == False:
                self.all_nodes.remove(self.all_nodes[x])
            else:
                x+=1
        print('Total Nodes: '+str(len(self.all_nodes)))
        self.size = input('Number of nodes to compress to: ')
        if int(self.size)<len(self.all_nodes):
            self.compress()
        else:
            self.compressed_nodes=self.all_nodes
            self.compressed_edges=self.all_edges
        self.add_nodes()
        self.add_edges()

    def find_nodes(self):
        for x in self.lines:
            if x[0] == '=':
                self.u.union(x.replace('"','').replace('\n','').split(' ')[1],x.replace('"','').replace('\n','').split(' ')[2])
            elif x[0] != 'm':
                nodes = x.replace('~','').replace('weak','').replace('after','').replace('&','').replace('+\n','').replace('-\n','').replace('(','').replace(')','').replace('|','').replace('"','').split(' ')
                for l in nodes:
                    if len(l.replace('\n',''))>0 and l[0] != ' ' and l[0] != '-' and l[0] != '+':
                        try:
                            int(l)
                        except ValueError:
                            try:
                                self.u.get_roots().index(self.u.find_object(l))
                            except ValueError:
                                self.u.get_roots().append(self.u.find_object(l))
        self.all_nodes.extend(self.u.get_roots())

    def add_nodes(self):
        for x in self.compressed_nodes:
            if len(self.compressionu.get_encompassed_nodes(x)) == 1:
                label = x
            else:
                label = 'CLUSTER ('+str(len(self.compressionu.get_encompassed_nodes(x)))+') '+x
            if len(self.compressed_nodes)==1:
                self.c.node(x,style = 'filled',color = 'white',label = label,labelfontsize = '10.0')
            else:
                for y in self.compressed_edges:
                    if x in y[0] or x in y[1]:
                        self.c.node(x,style = 'filled',color = 'white',label = label,labelfontsize = '10.0')

    def find_edges(self):
        for x in self.lines:
            if len(x.replace('\n',''))>0 and x[0] != '=' and x[0] != 'm':
                edges = x.replace(')','').replace('(','').replace('"','').replace('weak','').replace('after','').replace('~','').replace('&','').replace('|','').replace('+\n','').replace('-\n','').split(' ')
                i = edges.index('->')
                for y in range(0,i):
                    if len(edges[y])>0:
                        try:
                            int(edges[y])
                        except ValueError:
                            try:
                                self.all_edges.index([self.u.find_object(edges[y]),self.u.find_object(edges[i+1])])
                            except ValueError:
                                self.all_edges.append([self.u.find_object(edges[y]),self.u.find_object(edges[i+1])])

    def add_edges(self):
        for x in self.compressed_edges:
            self.c.edge(x[0],x[1],label='x',labelfontsize='10.0')

    def compress(self):
        self.compressed_edges=[]
        self.compressed_edges.extend(self.all_edges)
        while len(self.compressionu.get_roots())!=int(self.size):
            new = [True]*len(self.all_nodes)
            for x in range(0,len(self.all_nodes)):
                if new[x] == True:
                    for y in self.compressed_edges:
                        if y[0] == self.all_nodes[x]:
                            if new[self.all_nodes.index(self.compressionu.find_object(y[1]))] == True:
                                self.compressionu.union(y[1],y[0])
                                new[self.all_nodes.index(y[0])] = False
                                new[self.all_nodes.index(y[1])] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[1]))] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[0]))] = False
                                self.remove_edges(self.compressionu.find_object(y[1]))
                                break
                        elif y[1] == self.all_nodes[x]:
                            if new[self.all_nodes.index(self.compressionu.find_object(y[0]))] == True:
                                self.compressionu.union(y[0],y[1])
                                new[self.all_nodes.index(y[0])] = False
                                new[self.all_nodes.index(y[1])] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[1]))] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[0]))] = False
                                self.remove_edges(self.compressionu.find_object(y[1]))
                                break
                if len(self.compressionu.get_roots()) == int(self.size):
                    break
        self.compressed_nodes = self.compressionu.get_roots()
        self.compressed_edges = self.compress_edges()
 
    def remove_edges(self, root):
        y = 0
        while y<len(self.compressed_edges):
            if self.compressionu.find_object(self.compressed_edges[y][0]) == root and self.compressionu.find_object(self.compressed_edges[y][1]) == root:
                self.compressed_edges.remove(self.compressed_edges[y])
            else:
                y+=1

    def compress_edges(self):
        for x in range(0,len(self.compressed_edges)):
            self.compressed_edges[x] = [self.compressionu.find_object(self.compressed_edges[x][0]),self.compressionu.find_object(self.compressed_edges[x][1])]
        final_compression = []
        for y in self.compressed_edges:
            if not y in final_compression and y[0] != y[1]:
                final_compression.append(y)
        return final_compression

class extended_graph:
    
    def __init__(self,root,graph,comp):
        self.root = root
        self.graph = graph
        self.comp = comp
        self.all_nodes = self.comp.compressionu.get_encompassed_nodes(self.root)
        self.all_edges = []
        self.compressionu = union_find()
        self.c = Digraph('G', filename=str(self.root), format='dot')

    def main(self):
        self.find_edges()
        if len(self.all_nodes)>1:
            self.size = input('Number of nodes to compress to: ')
        else:
            self.size=1
        if int(self.size)<len(self.all_nodes):
            self.compress()
        else:
            self.compressed_nodes = self.all_nodes
            self.compressed_edges = self.all_edges
        self.add_nodes()
        self.add_edges()

    def find_edges(self):
        for x in self.graph.all_edges:
            if x[0] in self.all_nodes or x[1] in self.all_nodes:
                self.all_edges.append(x)

    def compress(self):
        self.compressed_edges = []
        self.compressed_edges.extend(self.all_edges)
        for y in self.compressed_edges:
            if y[0] in self.all_nodes:
                self.compressionu.find_object(y[0])
            if y[1] in self.all_nodes:
                self.compressionu.find_object(y[1])
        while len(self.compressionu.get_roots()) != int(self.size):
            new = [True]*len(self.all_nodes)
            for x in range(0,len(self.all_nodes)):
                if new[x] == True:
                    for y in self.compressed_edges:
                        if y[0] == self.all_nodes[x] or (y[0] in self.all_nodes and self.compressionu.find_object(y[0]) == self.all_nodes[x]):
                            if y[1] in self.all_nodes and new[self.all_nodes.index(self.compressionu.find_object(y[1]))] == True:
                                self.compressionu.union(y[1],y[0])
                                new[self.all_nodes.index(y[0])] = False 
                                new[self.all_nodes.index(y[1])] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[1]))]==False
                                new[self.all_nodes.index(self.compressionu.find_object(y[0]))]==False
                                self.remove_edges(self.compressionu.find_object(y[1]))
                                break
                        elif y[1] == self.all_nodes[x] or (y[1] in self.all_nodes and self.compressionu.find_object(y[1]) == self.all_nodes[x]):
                            if y[0] in self.all_nodes and new[self.all_nodes.index(self.compressionu.find_object(y[0]))] == True:
                                self.compressionu.union(y[0],y[1])
                                new[self.all_nodes.index(y[0])] = False
                                new[self.all_nodes.index(y[1])] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[1]))] = False
                                new[self.all_nodes.index(self.compressionu.find_object(y[0]))] = False
                                self.remove_edges(self.compressionu.find_object(y[1]))
                                break
                if len(self.compressionu.get_roots()) == int(self.size):
                    break
        self.compressed_nodes=self.compressionu.get_roots()
        self.compressed_edges=self.compress_edges()

    def compress_edges(self):
        for x in range(0,len(self.compressed_edges)):
            self.compressed_edges[x] = [self.compressionu.find_object(self.compressed_edges[x][0]),self.compressionu.find_object(self.compressed_edges[x][1])]
        final_compression = []
        for y in self.compressed_edges:
            if not y in final_compression and y[0] != y[1]:
                final_compression.append(y)
        return final_compression

    def remove_edges(self, root):
        y = 0
        while y<len(self.compressed_edges):
            if self.compressed_edges[y][0] in self.all_nodes and self.compressed_edges[y][1] in self.all_nodes:
                if self.compressionu.find_object(self.compressed_edges[y][0]) == root and self.compressionu.find_object(self.compressed_edges[y][1]) == root:
                    self.compressed_edges.remove(self.compressed_edges[y])
                else:
                    y+=1
            else:
                y+=1

    def add_nodes(self):
        for x in self.compressed_nodes:
            if len(self.compressionu.get_encompassed_nodes(x)) == 1:
                label = x
            else:
                label = 'CLUSTER ('+str(len(self.compressionu.get_encompassed_nodes(x)))+') '+x
            if len(self.compressed_nodes) == 1:
                self.c.node(x,style = 'filled',color = 'white',label = label,labelfontsize = '10.0')
            else:
                for y in self.compressed_edges:
                    if x in y[0] or x in y[1]:
                        self.c.node(x,style = 'filled',color = 'white',label = label,labelfontsize = '10.0')

    def add_edges(self):
            for x in self.compressed_edges:
                if x[0] in self.compressed_nodes and x[1] in self.compressed_nodes:
                    self.c.edge(x[0],x[1],label = 'x',labelfontsize = '10.0')
                elif x[0] in self.compressed_nodes:
                    self.c.node(x[1],style = 'filled',color = 'purple',label = x[1],labelfontsize = '10.0')
                    self.c.edge(x[0],x[1],label = 'x',labelfontsize = '10.0')
                elif x[1] in self.compressed_nodes:
                    self.c.node(x[0],style = 'filled',color = 'purple',label = x[0],labelfontsize = '10.0')
                    self.c.edge(x[0],x[1],label = 'x',labelfontsize = '10.0')
