#!/usr/bin/env python

from hashlib import sha512
from random import randint,choice
class BloomFilter(object):
    
  def __init__(self, array_size=(1 * 1024), hashes=7):

    self.filter = bytearray(array_size)     # The filter itself
    self.bitcount = array_size * 8          # Bits in the filter
    self.hashes = hashes                    # The number of hashes to use (different hash function)

  def _hash(self, value):
    # Build an int() around the sha256 digest of int() -> value
    digest = int(sha512(value.__str__()).hexdigest(), 16)
    for i in range(self.hashes):
      yield digest & (self.bitcount - 1) # digest % self.bitcount
      digest >>= (256 / self.hashes)

  def insert(self, value):
    for digest in self._hash(value):
      self.filter[digest>>3] |= (2 ** (digest & 7))
      
  def find(self, value):
    return all(self.filter[digest>>3] & (2 ** (digest & 7))
      for digest in self._hash(value))

if __name__ == "__main__":
  bf = BloomFilter()
  lst = [randint(1,100) for i in range(190)]
  for num in lst:
      bf.insert(num)

  print("Filter size {0} bytes").format(bf.filter.__sizeof__())

  print bf.find(choice(lst))           
  print bf.find(choice(lst))
  print bf.find(0)        
  print bf.find(101)         
