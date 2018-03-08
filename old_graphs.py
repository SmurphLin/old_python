""" Creating a Graph class """

class Graph(object):

    def __init__(self,num_verts):
        """set the number of verticies to
           create the empty adjacency matrix.
        """
        self.num_verts = num_verts
        self.adjacency_mtx = [[] for i in range(num_verts)]
    """create an empty adjacency matrix
       the is initialized to the necessary size.
    """

    def createAdjMtx(self):
        #rows = self.num_verts
        cols = self.num_verts
        default_value = False
        #adj_mtx = [[] for i in range(cols)]
        iter = 0
        for i in range(cols):
            hold = self.adjacency_mtx[i]
            while iter < self.num_verts:
                hold.append(default_value)
                iter += 1
            iter = 0
            self.adjacency_mtx[i] = hold
        #self.adjacency_matrix = adj_mtx
        return self.adjacency_mtx


    def setEdge(self,vertex,position):
        try:
            the_vertex = self.adjacency_mtx[vertex]
        except IndexError:
            print "the vertex does not exist"

        try:
            the_vertex[position] = True
        except IndexError:
            print "the column is out of range"

    def bredthFirstSearch(self,begin,end):
        paths_to_end = []

        try:
            begin_vertex = self.adjacency_mtx[begin]
        except IndexError:
            print "the vertex does not exist"
        try:
            end_vertx = self.adjacency_mtx[end]
        except IndexError:
            print "the vertex does not exist"
        i = begin
        j = 0
        count_end = 0
        vtx = self.adjacency_mtx[i][j]
        while True:
            if vtx == True and j == end and j < len(self.adjacency_mtx[i]):
                count_end += 1    # increment counter
                paths_to_end.append((i, j, count_end)) # add path to paths list
                j += 1
                count_end = 0
                #i = j
                #j = 0
                #vtx = self.adjacency_mtx[i][j]
            elif vtx == True and j != end:
                k = j
                l = i
                hold_vtx = self.adjacency_mtx
                vtx = self.adjacency_mtx[i][j]
                count_end += 1
            elif vtx == False and j < len(vtx):
                j += 1
            elif vtx == False and j == len(vtx):
                i += 1
                j = 0
            elif i == len(vtx):
                break
        return




g = Graph(8)
g.createAdjMtx()
print g.adjacency_mtx, "\n"
g.setEdge(0,1)
g.setEdge(0,2)
g.setEdge(1,5)
g.setEdge(1,3)
g.setEdge(2,3)
g.setEdge(3,6)
g.setEdge(4,7)
g.setEdge(5,3)
g.setEdge(5,4)
g.setEdge(5,7)
g.setEdge(6,2)
g.setEdge(6,4)
g.setEdge(6,7)


print g.adjacency_mtx, "\n"
