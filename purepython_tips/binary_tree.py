from binarytree import build


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7]
    binary_tree = build(nodes)
    print('Binary tree from list:\n', binary_tree)
    print('List from binary tree: ', binary_tree.values)
    exit(0)
