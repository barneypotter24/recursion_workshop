# count_transitions.py

from classes import *

def count_transitions(n, color_handed=None):
    '''From a given node, count all of its descendant color changes
    '''

    if (color_handed == n.color) or (color_handed == None):
        handed_mine = 0
    else:
        handed_mine = 1

    if not (n.left or n.right):
        return handed_mine
    elif (n.left and n.right):
        return handed_mine + count_transitions(n.left, n.color) + count_transitions(n.right, n.color)
    elif n.left:
        return handed_mine + count_transitions(n.left, n.color)
    elif n.right:
        return handed_mine + count_transitions(n.right, n.color)
    else:
        sys.exit(0)


def test():

    small = build_small_tree(c=True)
    med = build_medium_tree(c=True)
    large = build_large_tree(c=True)

    cases = [ (small,1),
              (med,2),
              (large,6)
            ]

    for case in cases:
        res = count_transitions(case[0])
        if res == case[1]:
            print("Nice!")
        else:
            print("Your function took {} and turned it into {}. Expected {}".format(case[0], res, case[1]))

if __name__=="__main__":
    test()
