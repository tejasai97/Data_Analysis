

import numpy as np



my_list = [1,2,3]
my_list



np.array(my_list)



my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix



np.array(my_matrix)


# ## Built-in Methods
# 
# There are lots of built-in ways to generate Arrays

# ### arange
# 
# Return evenly spaced values within a given interval.

np.arange(0,10)



np.arange(0,11,2)


# ### zeros and ones
# 
# Generate arrays of zeros or ones


np.zeros(3)



np.zeros((5,5))




np.ones(4)



np.ones((3,3))


# ### linspace
# Return evenly spaced numbers over a specified interval.

np.linspace(0,10,3)




np.linspace(0,10,50)


# ## eye
# 
# Creates an identity matrix


np.eye(4)


# ## Random 
# 
# Numpy also has lots of ways to create random number arrays:
# 
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

np.random.rand(2)



np.random.rand(5,5)


# ### randn
# 
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:



np.random.randn(2)



np.random.randn(5,5)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).


np.random.randint(1,100)



np.random.randint(1,100,10)


# ## Array Attributes and Methods

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)



arr



ranarr


# ## Reshape
# Returns an array containing the same data with a new shape.


arr.reshape(5,5)


# ### max,min,argmax,argmin
# 
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax


ranarr



ranarr.max()



ranarr.argmax()



ranarr.min()



ranarr.argmin()


# ## Shape
# 
# Shape is an attribute that arrays have (not a method):



# Vector
arr.shape




# Notice the two sets of brackets
arr.reshape(1,25)




arr.reshape(1,25).shape




arr.reshape(25,1)



arr.reshape(25,1).shape


# ### dtype
# 
# You can also grab the data type of the object in the array:



arr.dtype

