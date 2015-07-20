# python
#coding=utf8
from  math import floor
import string
class Bitmap(object):
    def __init__(self,num):# init the class
        self.size=int((num+30)/31)# floor function
        self.array=[0 for x in range(self.size)] # the size of the array

    def set(self,num): #  init the number to the bit formart
        byteIndex=num%31
        elemIndex=int(num/31)
        self.array[elemIndex]|=(1<<byteIndex)
        print self.array
    def clr(self,num):
        byteIndex=num%31
        elemIndex=int(num/31)
        self.array[elemIndex]&=(~(1<<byteIndex))
    def test(self,num): # test the number to see it's bit is 1
        byteIndex=num%31
        elemIndex=int(num/31)
        return self.array[elemIndex] &(1<<byteIndex)
if __name__=='__main__':
    number=798
    before_array=[12,34,45,1,3,9,2,0,321,12,798]
    bitmap=Bitmap(number)
    result=[]
    for number in before_array:
        bitmap.set(number)
  
    for i in range(number+1):
        if bitmap.test(i):
            result.append(i)
    print str(before_array)+'\n'
    print result
        
        
        
        
