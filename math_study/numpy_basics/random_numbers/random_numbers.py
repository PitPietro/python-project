import numpy as np
from numpy.random import *


if __name__ == '__main__':
    print('Numpy - Random numbers')

    # Return a sample (or samples) from the "standard normal" distribution.
    # This is a convenience function for users porting code from Matlab, which wraps `standard_normal`.
    print('-----\nrand function:')
    print(np.random.randn())
    print(randn(10))  # by using 'from numpy.random import *' this call is equal to the one above
    print(np.random.randn(2, 5))
