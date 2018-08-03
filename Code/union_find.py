class union_find:
    def __init__(self):
        self.roots = []
        self.stringtoindex = []

    def find_index(self,object):
        try:
            i = self.stringtoindex.index(object)
        except ValueError:
            self.stringtoindex.append(object)
            self.roots.append(len(self.stringtoindex)-1)
            return len(self.stringtoindex)-1
        if i == self.roots[i]:
            return i
        else:
            return self.find_index(self.stringtoindex[self.roots[i]])

    def find_object(self,object):
        try:
            i = self.stringtoindex.index(object)
        except ValueError:
            self.stringtoindex.append(object)
            self.roots.append(len(self.stringtoindex)-1)
            return self.stringtoindex[-1]
        if i == self.roots[i]:
            return self.stringtoindex[i]
        else:
            return self.find_object(self.stringtoindex[self.roots[i]])

    def union(self,one,two):
        firstroot = self.find_index(one)
        secondroot = self.find_index(two)
        self.roots[firstroot] = secondroot

    def get_roots(self):
        simplifiedroots = []
        for r in self.stringtoindex:
            try:
                i = simplifiedroots.index(self.find_index(r))
            except ValueError:
                simplifiedroots.append(self.find_index(r))
        simplifiedrootsstring = []
        for r in simplifiedroots:
            simplifiedrootsstring.append(self.stringtoindex[r])
        return simplifiedrootsstring

    def get_encompassed_nodes(self,object):
        encompassed_nodes = []
        for r in self.stringtoindex:
            if self.find_object(r) == object:
                encompassed_nodes.append(r)
        if not object in encompassed_nodes:
            encompassed_nodes.append(object)
        return encompassed_nodes
