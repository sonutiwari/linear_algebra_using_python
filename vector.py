# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:54 2019

@author: sonu.tiwari01
"""
from math import acos, sqrt, pi
from decimal import getcontext

# Setting global Precision
getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Can not Normalize zero Vector'
    
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
    
    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0 / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            
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
    
    def dot_product(self, v):
        """ 
        The function to calculate Dot product of 2 vectors. 
  
        Parameters: 
            v (Vector): The vector to be calculated Dot product with. 
          
        Returns: 
            float: The Dot product of 2 vectors. 
        """        
            
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])
    
    def magnitude(self, vector = None):
        """
        The function calculates magnitude of the Vector.
        
        Parameters : vector if we need to calculate the 
        magnitude of other vector otherwise it will be none.
        
        Returns:
            float: The magnitude of the Vector
        """
        if vector is None:
            return sqrt(sum([i * i for i in self.coordinates]))
        else:
            return sqrt(sum([i * i for i in vector.coordinates]))
    
    def calculate_angle(self, v, degree = False):
        """ 
        The function to calculate angle between 2 Vectors. 
  
        Parameters: 
            v (Vector): The vector to be calculate angle with. 
            degree : The answer format, default in radians
        Returns: 
            float: Angle between 2 Vectors by default in radians. 
        """
        try:
            self.normalize()
            v.normalize()
            base_angle = 180
            dot_prod = self.dot_product(v)
            temp_prod = self.magnitude() * self.magnitude(v)
            if degree:
                return acos(dot_prod / temp_prod) * (base_angle / pi)
            return acos(dot_prod / temp_prod)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Can not calculate angle with zero vector')
            else:
                raise e
#print(Vector([1, 2, 3]) == Vector([1, 2, 3]))
#v = Vector([8.218, -9.341])
#w = Vector([-1.129, 2.111])
#print(v.plus(w))
#
#v = Vector([7.119, 8.215])
#w = Vector([-8.223, 0.878])
#print(v.minus(w))
#
#v = Vector([1.671, -1.012, -0.318])
#c = 7.41
#print(v.times_scalar(c))
v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print(v.calculate_angle(w, True))
