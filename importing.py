"""Module for investegating importing and namespace""" #docstring

import better_code
from better_code import area_of_square

area = better_code.area_of_square(40)
area = area_of_square(40)
print (area)

print('Global namespace')
namespace = globals().copy()
for name, obj in namespace.items():
    print(name, obj)