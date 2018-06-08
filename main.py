import util
import algo

bin_search_cases = {
    'odds not found -1': ([0, 1, 2, 3, 4], -1),
    'odds found 0': ([0, 1, 2, 3, 4], 0),
    'odds found 1': ([0, 1, 2, 3, 4], 1),
    'odds found 2': ([0, 1, 2, 3, 4], 2),
    'odds found 3': ([0, 1, 2, 3, 4], 3),
    'odds found 4': ([0, 1, 2, 3, 4], 4),
    'evens not found -1': ([0, 1, 2, 3], -1),
    'evens found 0': ([0, 1, 2, 3], 0),
    'evens found 1': ([0, 1, 2, 3], 1),
    'evens found 2': ([0, 1, 2, 3], 2),
    'evens found 3': ([0, 1, 2, 3], 3),
    'evens not found 4': ([0, 1, 2, 3], 4),
}

util.test('BINARY SEARCH', algo.bin_search, bin_search_cases)

n7 = util.create_node(7)
n6 = util.create_node(6)
n3 = util.create_node(3, [n6, n7])

n5 = util.create_node(5)
n4 = util.create_node(4)
n2 = util.create_node(2, [n4, n5])

n1 = util.create_node(1, [n2, n3])

dfs_bfs_cases = {
    'map-dfs': (n1, lambda x, r: r + [x.get('v')], []),
    'filter-dfs': (n1, lambda x, r: r + [x.get('v')] if x.get('v') > 1 else r, [])
}

util.test('DFS', algo.dfs, dfs_bfs_cases)
util.test('BFS', algo.bfs, dfs_bfs_cases)


merge_sort_cases = {
    'sorted-odd': ([0, 1, 2, 3, 4, 5, 6],),
    'sorted-even': ([0, 1, 2, 3, 4, 5],),
    'reverse-sorted-even': ([5, 4, 3, 2, 1, 0],),
    'reverse-sorted-odd': ([6, 5, 4, 3, 2, 1, 0],),
    'random': ([16, 5, 34, 23, 12, 41, 0],)
}


quick_sort_cases = {
    'sorted-odd': ([0, 1, 2, 3, 4, 5, 6],),
    'sorted-even': ([0, 1, 2, 3, 4, 5],),
    'reverse-sorted-even': ([5, 4, 3, 2, 1, 0],),
    'reverse-sorted-odd': ([6, 5, 4, 3, 2, 1, 0],),
    'random': ([16, 5, 34, 23, 12, 41, 0],)
}

util.test('MERGESORT', algo.mergesort, merge_sort_cases)
util.test('QUICKSORT', algo.quicksort, quick_sort_cases)
