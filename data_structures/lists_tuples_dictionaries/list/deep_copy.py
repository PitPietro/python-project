import copy

if __name__ == '__main__':
    a = ['a', 'b', 'c']
    b = a
    c = copy.deepcopy(a)
    print('a: {}\nb: {}\nc: {}'.format(a, b, c), end='\n\n')
    b.append('b_d')
    c.append('CCC')
    print('a: {}\nb: {}\nc: {}'.format(a, b, c), end='\n\n')
    print('\nBoth the lists a and b reference to the same list, since when you modify b, even a gets modified.\n'
          'While c reference to another list, initially copied by a.')
