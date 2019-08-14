# count_terminal_nodes.py

from classes import *

def count_terminal_nodes(n):
    '''From a given node, count all of its descendant terminals
    '''

    if not (n.left or n.right):
        return 1
    elif (n.left and n.right):
        return count_terminal_nodes(n.left) + count_terminal_nodes(n.right)
    elif n.left:
        return count_terminal_nodes(n.left)
    elif n.right:
        return count_terminal_nodes(n.right)



#### HELPER FUNCTIONS ####

def test():
    small = build_small_tree()
    med = build_medium_tree()
    large = build_large_tree()

    cases = [ (small,2),
              (med,2),
              (large,6)
            ]

    for case in cases:
        res = count_terminal_nodes(case[0])
        if res == case[1]:
            print("Nice!")
        else:
            print("Your function took {} and turned it into {}. Expected {}".format(case[0], res, case[1]))

if __name__=="__main__":
    test()
