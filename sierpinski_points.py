import numpy as np
from math import sqrt
from classes import Point2, Triangle

def sierpinski(layers, t):

    assert type(t) == Triangle, "input was not a Triangle"
    if layers > 9:
        print("Too many layers specified, resetting to max of 9")
        layers = 9

    return #PUT YOUR RECURSIVE FUNCTION HERE


#### HELPER FUNCTIONS ####

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
