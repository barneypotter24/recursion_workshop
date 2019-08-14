import numpy as np
from math import sqrt
from classes import Point2, Triangle

def sierpinski(layers, t):

    assert type(t) == Triangle, "input was not a Triangle"
    if layers > 9:
        print("Too many layers specified, resetting to max of 9")
        layers = 9

    if layers == 0:
        return [t]
    else:
        AB = t.A.midpoint(t.B)
        BC = t.B.midpoint(t.C)
        CA = t.C.midpoint(t.A)

        t1 = Triangle(t.A,AB,CA)
        t2 = Triangle(AB,t.B,BC)
        t3 = Triangle(CA,BC,t.C)

        return sierpinski(layers-1, t1) + sierpinski(layers-1, t2) + sierpinski(layers-1, t3)


def plot_sier(ts):
    from matplotlib.patches import Circle, Wedge, Polygon
    from matplotlib.collections import PatchCollection
    import matplotlib.pyplot as plt


    fig, ax = plt.subplots()

    patches = []
    for t in ts:
        polygon = t.to_polygon()
        patches.append(polygon)

    colors = 100*np.random.rand(len(patches))
    p = PatchCollection(patches, alpha=0.5)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    ax.set_xlim(0,2)
    ax.set_ylim(0,sqrt(3))

    plt.savefig('output/sierpinski.png')

if __name__=="__main__":
    T = Triangle( Point2(0,0),
                              Point2(2,0),
                              Point2(1,sqrt(3)) )

    ts = sierpinski(5, T)
    plot_sier(ts)
