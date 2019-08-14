# classes.py
import numpy as np


class Point2(object):

    def __init__(self, x, y):

        self.x = float(x)
        self.y = float(y)

    def midpoint(self, other):
        new_x = (self.x + other.x) / 2
        new_y = (self.y + other.y) / 2

        return Point2(new_x, new_y)

class Triangle(object):

    def __init__(self, A, B, C):

        for point in [A, B, C]:
            assert type(point) == Point2, "input points were not of type Point2"
        self.A = A
        self.B = B
        self.C = C

    def print_points(self):
        print('({},{})'.format(self.A.x,self.A.y))
        print('({},{})'.format(self.B.x,self.B.y))
        print('({},{})'.format(self.C.x,self.C.y))

    def to_polygon(self):
        from matplotlib.patches import Polygon
        as_array = np.array([[h.x, h.y] for h in [self.A, self.B, self.C]])
        p = Polygon(as_array, True)
        return p

class Node(object):

    def __init__(self, name, left=None, right=None):

        self.name = name
        self.left = left
        self.right = right

class cNode(object):

    def __init__(self, name, left=None, right=None, color="white"):

        self.name = name
        self.left = left
        self.right = right
        self.color = color

def build_small_tree(c=False):
    if c:
        C = cNode('C')
        B = cNode('B',color='green')
        A = cNode('A',B,C)
    else:
        C = Node('C')
        B = Node('B')
        A = Node('A',B,C)
    return A

def build_medium_tree(c=False):
    if c:
        I = cNode('I')
        G = cNode('G')
        D = cNode('D',None,I,color='green')
        C = cNode('C',None,G)
        B = cNode('B',D,None,color='green')
        A = cNode('A',B,C)
    else:
        I = Node('I')
        G = Node('G')
        D = Node('D',None,I)
        C = Node('C',None,G)
        B = Node('B',D,None)
        A = Node('A',B,C)
    return A

def build_large_tree(c=False):
    if c:
        N = cNode('N',color='green')
        M = cNode('M')
        L = cNode('L',N,None,color='green')
        K = cNode('K')
        J = cNode('J')
        I = cNode('I')
        H = cNode('H',L,M)
        G = cNode('G',color='green')
        F = cNode('F',K,None)
        E = cNode('E',None,J,color='green')
        D = cNode('D',H,I,color='green')
        C = cNode('C',F,G)
        B = cNode('B',D,E,color='green')
        A = cNode('A',B,C)
    else:
        N = Node('N')
        M = Node('M')
        L = Node('L',N,None)
        K = Node('K')
        J = Node('J')
        I = Node('I')
        H = Node('H',L,M)
        G = Node('G')
        F = Node('F',K,None)
        E = Node('E',None,J)
        D = Node('D',H,I)
        C = Node('C',F,G)
        B = Node('B',D,E)
        A = Node('A',B,C)
    return A
