# fib.py
#
# This script defines a function, computes the nth Fobonacci number.
# Note that we will 0-index the Fibonacci sequence: 0,1,1,2,3,5....
#
#
# Examples:
#     reverse_a_list(0) -> 0
#     reverse_a_list(1) -> 1
#     reverse_a_list(4) -> 3
#     reverse_a_list(5) -> 5
#     reverse_a_list(17) -> 1597
#

def fib(n):
    '''A recursive function to calculate the nth Fibonacci number
    '''
    if n > 20:
        n = 20
        print("Input number was too high, resetting to 20 to save computer time.")

    return #PUT YOUR RECURSIVE FIBONACCI FUNCTION HERE



#### HELPER FUNCTIONS ####

def test():
    cases = [ (0,0),
              (1,1),
              (4,3),
              (5,5),
              (17,1597)
            ]

    for case in cases:
        res = fib(case[0])
        if res == case[1]:
            print("Nice!")
        else:
            print("Your function took {} and turned it into {}. Expected {}".format(case[0], res, case[1]))

if __name__=="__main__":
    test()
