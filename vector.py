# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:54 2019

@author: sonu.tiwari01
"""

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def plus(self, v):
        """ 
        The function to add two Vectors. 
  
        Parameters: 
            v (Vector): The vector to be added. 
          
        Returns: 
            Vector: A Vector which contains the sum. 
        """
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])
    
    def minus(self, v):
        """ 
        The function to subtract two vectors. 
  
        Parameters: 
            v (Vector): The vector to be subtracted. 
          
        Returns: 
            Vector: A Vector which contains the Difference. 
        """
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])
    
    def times_scalar(self, c):
        """ 
        The function to add multiply vector by a scalar . 
  
        Parameters: 
            c (float): The multiplier constant. 
          
        Returns: 
            Vector: A Vector which contains the scalar multiplication. 
        """
        return Vector([c * i for i in self.coordinates])
#print(Vector([1, 2, 3]) == Vector([1, 2, 3]))
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print(v.plus(w))

v = Vector([7.119, 8.215])
w = Vector([-8.223, 0.878])
print(v.minus(w))

v = Vector([1.671, -1.012, -0.318])
c = 7.41
print(v.times_scalar(c))