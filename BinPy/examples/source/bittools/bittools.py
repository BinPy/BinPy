
# coding: utf-8

# Example to illustrate the usage of bittools

# `BinPyBits` is a class inheriting from the `bitstring.BitArray` class. It will be used for efficient manipulation / handling of Bit vectors.

# In[1]:

from BinPy import *

# Initializing a BinPyBits object

bit_vector = BinPyBits(5)


# In[2]:

# By default all BinPyBits objects are not signed

bit_vector.signed


# In[3]:

# Getting the decimal value

bit_vector.uint


# In[4]:

# Getting the binary string

bit_vector.bin


# In[5]:

# Do not use int with unsigned BinPyBits objects

bit_vector.int


# In[6]:

# This returns -3 since '101' ==> -3 ( 2's Complement representation )

# You could use :

int_value = bit_vector.int if bit_vector.signed else bit_vector.uint

print int_value


# In[7]:

# Creating a BinPyBits object using binary string

bit_vector = BinPyBits('1111', signed=False)

# Converting to decimal

int_value = bit_vector.int if bit_vector.signed else bit_vector.uint

print int_value


# In[8]:

# Creating a signed BinPyBits

bit_vector = BinPyBits('1111', signed=True)

# Converting to decimal

int_value = bit_vector.int if bit_vector.signed else bit_vector.uint

print int_value


# In[9]:

# Converting to hex

bit_vector.hex


# Refer [the documentation of
# bittstring](https://pypi.python.org/pypi/bitstring/3.1.3) to discover
# additional functionality.

# In[10]:

# The speciality of BinPyBits lies in the fact that it can be initialized from various types of inputs
# Except for the initialization, the rest of the functionalities remain
# similar to that of the bitstring.BitArray

# Initializing a signed value using - sign

bit_vector = BinPyBits('-1111', signed=True)

print bit_vector.int
