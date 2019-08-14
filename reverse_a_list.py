# reverse_a_list.py
#
# This script defines a function, reverse_a_list, that takes a list
# and returns that list, but reversed. This should behave the same
# as python's list.reverse() method, but our reverse_a_list should use recursion
#
# For this we have two functions to help us out:
#     head(list) returns the first object of the list:
#         head([1,2,3]) -> [1]
#     tail(list) returns the list minus the head:
#         tail([1,2,3]) -> [2,3]
#
# Examples:
#     reverse_a_list([1,2,3]) -> [3,2,1]
#     reverse_a_list([0]) -> [0]
#     reverse_a_list([1,1,1]) -> [1,1,1]
#     reverse_a_list([1,2,3,2,1,]) -> [1,2,3,2,1]
#     reverse_a_list([]) -> []
#


def reverse_a_list(l):
    '''This function takes a list, l, and returns a reversed l
    '''

    return #PUT YOUR RECURSIVE FUNCTION HERE


#### HELPER FUNCTIONS ####

def head(l):
    '''Return the first element of a list (as a list).
    '''
    return [l[0]]

def tail(l):
    '''Return all elements in a list other than the head.
    '''
    return l[1:]

def test():

    cases = [ ([1,2,3],[3,2,1]),
              ([0],[0]),
              ([1,1,1],[1,1,1]),
              ([1,2,3,2,1,],[1,2,3,2,1]),
              ([],[])
            ]

    for case in cases:
        res = reverse_a_list(case[0])
        if res == case[1]:
            print("Nice!")
        else:
            print("Your function took {} and turned it into {}. Expected {}".format(case[0], res, case[1]))

if __name__=="__main__":
    test()
