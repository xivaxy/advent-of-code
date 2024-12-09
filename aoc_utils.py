def intify(a: list|str, output_tuples = False):
    """Parse string into ints. If output_tuples is True, return a list of tuples instead of a list of lists.
    Examples: 
    '1 2 3', '1,2,3', '1;2;3' => [[1, 2, 3]]
    '1 2 3\n4 5 6' => [[1, 2, 3], [4, 5, 6]]
    ['1 2 3', '4 5 6'] => [[1, 2, 3], [4, 5, 6]]
    """
    if isinstance(a, str):
        a = a.splitlines()
    if isinstance(a[0], str):
        a = [l.replace(",", " ").replace(";", " ").split() for l in a]
    return [tuple(int(el) for el in l) if output_tuples else [int(el) for el in l] for l in a]

neigh4 = [(1,0), (0, -1), (-1, 0), (0, 1)]
neigh8 = [(1,0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
neigh6 = [(1,0,0), (0, -1,0), (-1, 0,0), (0, 1,0),(0,0,1), (0,0,-1)]
tuple_add = lambda a,b: tuple(x+y for x,y in zip(a,b))
tuple_sub = lambda a,b: tuple(x-y for x,y in zip(a,b))

import math 

def crt(m: list[int], rem: list[int]) -> int:
    """Chinese Remainder Theorem. Solve x = rem[i] (mod m[i]) for all i.
    """
    assert len(rem)==len(m)
    if len(rem)==0: return 0
    if len(rem)==1: return rem[0]
    P = math.lcm(*m)
    rest = [P//mi for mi in m]
    inv = [pow(rest[i], -1, m[i]) for i in range(len(m))]
    res = sum(rest[i]*inv[i]*rem[i] for i in range(len(m))) % P
    if res==0: res = P
    return res

def first_intersection(a: list[list[int]]) -> int:
    """a[0], a[1] ... are lists of times when a rare event happens, all streams are periodic with different periods. The function finds the first time when all events happen at the same time.
    """
    m = [a[i][-1]-a[i][-2] for i in range(len(a))]
    rem = [a[i][-2] for i in range(len(a))]
    return crt(m, rem)

def egcd(a, b):
    # find solution for ax + by = gcd(a, b)
    # returns (gcd(a, b), x, y)
    if a == 0: return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)
    