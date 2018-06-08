def test(test_name, func, cases):
    print('###   {}   ###'.format(test_name))
    for name, case in cases.items():
        print('{}: {}'.format(name, func(*case)))


def create_node(v, children=None):
    children = children if children is not None else []
    return {'v': v, 'children': children}
