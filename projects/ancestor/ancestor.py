# def helper_add_vertices():
    
def helper_add_edges(pair, vertices):
    if pair[0] in vertices and pair[1] in vertices:
        vertices[f'{pair[0]}'].add(f'{pair[1]}')


def earliest_ancestor(ancestors, starting_node):
    # put all the ancestor pairs in a dictionary with all the parents in the value set()
    vertices = {}
    for pair in ancestors:
        print('initial pair', pair)
        if vertices.get(f'{pair[1]}') == None:
            # print('pair[0]',pair)
            vertices[f'{pair[1]}'] = set(f'{pair[0]}')
            # print('vertices after adding a new key and value pair',vertices)
        if vertices.get(f'{pair[0]}') == None:
            # print('pair[1]',pair)
            vertices[f'{pair[0]}'] = set()
            # print('vertices after adding a new key',vertices)
        if vertices.get(f'{pair[1]}') != None and vertices.get(f'{pair[0]}') != None:
            # print('pair[0][1]',pair)
            vertices[f'{pair[1]}'].add(f'{pair[0]}')
            # print('vertices after adding new value',vertices)
    print('final vertices', vertices)
    pass

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)