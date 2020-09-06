# Project: Creating Vectors and operations on Vectors
# Author: Faizan Tayyab
# License: Copyright 2020
# Python: 2.7
"""Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from decimal import *
from math import pow, sqrt, acos, pi

# Set precision
getcontext().prec = 4

class Vector(object):
    def __init__(self,coordinates):
        self.coordinates = tuple([Decimal(c) for c in coordinates])
        self.dimensions = len(self.coordinates)

    def __str__(self):
        return 'Vector {}'.format(self.coordinates)

    def __eq__(self, w):
        return self.coordinates == w.coordinates
    
    def add(self, w):
        return Vector([x+y for x,y in zip(self.coordinates,w.coordinates)])
    
    def sub(self, w):
        return Vector([x-y for x,y in zip(self.coordinates,w.coordinates)])

    def scalarMul(self, n):
        return Vector([c*Decimal(n) for c in self.coordinates])

    def magnitude(self):
        return round(sqrt(sum([pow(c,2) for c in self.coordinates])),3)

    def normalize(self):
        try:
            return self.scalarMul(Decimal('1.0')/Decimal(self.magnitude()))
        except DivisionByZero:
            raise("Unable to divide by 0")
    
    def product(self, w):
        return round(sum([x*y for x,y in zip(self.coordinates, w.coordinates)]),3)

    def productAngle(self, w, rad = True):
        if rad:
            return acos(self.normalize().product(w.normalize()))
        else:
            return acos(self.normalize().product(w.normalize())) * (180/pi) 
    
    def is_ortogonal(self, w, tolerance = 1e-10):
        return abs(self.product(w))  < tolerance

    def is_parallel(self, w):
        return (self.is_zero() or w.is_zero() or self.productAngle(w) == 0 or self.productAngle(w) == pi)
            
    def is_zero(self):
        return self.magnitude() < 1e-10

    def project(self, b):
        u = b.normalize()
        return u.scalarMul(self.product(b.normalize()))


    