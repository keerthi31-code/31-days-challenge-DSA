"""
Time Cpmplexity- how many steps does the program takes
space complexity- how much extra memory does the program use

constant time O(1)

linear time O(n) - running time

def total(arr):
    s = 0
    for x in arr:      # runs n times
        s += x
    return s

quadratic time-O(n^2)

def print_pairs(arr):
    for i in arr:          # n times
        for j in arr:      # n times for each i
            print(i, j)

Space complexity - count the extra memory
O(1) space
time is O(n) and space is O(1)
def total(arr):
    s = 0              # one variable, no matter how big arr is
    for x in arr:
        s += x
    return s
    
O(n)Space 
def squares(arr):
    result = []
    for x in arr:
        result.append(x * x)   # new list grows to size n
    return result
Time is O(n) and space is O(n) becoz we built new list --takes extra memory

Quick Gist: Finding Time and Space Complexity
Time complexity: look at the loops
What you see in the code	Time
Just a lookup, math, or assignment	O(1)

One loop over n items	O(n)

Two loops, one inside the other (both over n)	O(n²)

Two loops one after the other (not nested)	O(n + n) = O(n)

Loop where the value is halved or doubled each time (i *= 2, n //= 2)	O(log n)

Loop of n, with a halving step inside	O(n log n)

Recursion that calls itself once with n - 1	O(n)

Recursion that calls itself twice with n - 1 (like naive fibonacci)	O(2ⁿ)

Trick: count how many times the innermost line runs, then express that in terms of n.

Space complexity: look at what you create
What you see in the code	Space
Only a few variables (count, sum, i)	O(1)
New list, set, or dict that grows with the input	O(n)
Recursion going n levels deep	O(n) (call stack)
2D grid or matrix of n × n	O(n²)

Trick: ask "does the extra memory grow when the input grows?" If yes, it's not O(1). Don't count the input itself.

The 3 simplification rules
Drop constants: O(2n) → O(n)
Keep the biggest term: O(n² + n) → O(n²)
Different inputs, different letters: looping over a then b is O(a + b), not O(n)
Growth order, fast to slow

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

Common things people forget
x in list is O(n), but x in set or x in dict is O(1)
list.append() is O(1), but list.insert(0, x) is O(n)
Slicing arr[a:b] is O(k) and creates a new list
sorted() / .sort() is O(n log n)
String concatenation inside a loop (s += x) can cost O(n²)
Recursion always uses stack space, even if you create no list
4-step checklist for any problem
Loops? Count them and check whether they are nested.
Halving or doubling? Then think log n.
Recursion? Count the calls per level and the depth.
New data structure? If its size grows with the input, space is O(n).
One-line memory aid

Loop = n, nested loop = n², halving = log n, new list = O(n) space, recursion depth = O(n) space.

"""
