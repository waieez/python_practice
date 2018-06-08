import math


# BINARY SEARCH
def bin_search(vals, v, s=None, e=None):
    s = s if s is not None else 0
    e = e if e is not None else len(vals)
    if s > e or s >= len(vals):
        return -1
    m = (e - s) / 2 + s
    mv = vals[m]
    if v == mv:
        return m
    elif v < mv:
        return bin_search(vals, v, s, m - 1)
    else:
        return bin_search(vals, v, m + 1, e)


# DFS
def dfs(node, visit, result):
    result = visit(node, result)
    for c in node.get('children'):
        result = dfs(c, visit, result)
    return result


# BFS
def bfs(node, visit, result):
    h = 0
    q = [node]

    while h < len(q):
        n = q[h]
        h = h + 1
        result = visit(n, result)
        for c in n.get('children'):
            q.append(c)
    return result


# MERGESORT
def mergesort(vals):
    if len(vals) <= 1:
        return vals
    m = len(vals) / 2

    left = mergesort(vals[:m])
    right = mergesort(vals[m:])
    return merge(left, right)


def merge(left, right):
    i, j, result = 0, 0, []

    while i < len(left) or j < len(right):
        if j >= len(right) or i < len(left) and left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


# QUICKSORT
def quicksort(vals, s=None, e=None, p=None):
    s = 0 if s is None else s
    e = len(vals) - 1 if e is None else e
    p = e if p is None else p

    # base case
    if s >= e or s > len(vals):
        return vals

    # get pivot
    m = (e - s) / 2 + s
    p = vals[m]
    swap(vals, m, e)

    i, j = s, e
    while i < j:
        while vals[i] < p:
            i += 1
        while vals[j] >= p and j > i:
            j -= 1
        swap(vals, i, j)

    # move pivot in place
    swap(vals, i, e)

    quicksort(vals, s, i - 1)
    quicksort(vals, i + 1, e)
    return vals


def swap(vals, s, e):
    sv, ev = vals[s], vals[e]
    # print('swap', sv, ev)
    vals[s] = ev
    vals[e] = sv
