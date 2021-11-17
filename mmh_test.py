import pytest
import random
from minMaxHeap import * 

def makeRandomHeap(size): #Make a random Heap
    h = Heap(size) 
    for i in range(size): 
        h.insert(random.randint(0, 100),"a")
    return h

def makeRandomArray(size):
    a = []
    for i in range(size): 
        val = random.randint(0, 100)
        a.append(val)
        a += (chr(ord('A') + i))
    return a

def makeEmptyHeap():
    h = Heap(10)
    return h


def makeHeap(): #Make a Heap
    h = Heap(10) 
    h.insert(5,"a")   # Min 3
    h.insert(11,"b")
    h.insert(2,"c")   # Min 1
    h.insert(9,"d")  
    h.insert(35,"e")  # Max 1
    h.insert(8,"f")   
    h.insert(3,"g")   # Min 2
    h.insert(18,"h")  # Max 3
    h.insert(17,"i")
    h.insert(25,"j")  # Max 2
    
    return h
    
def test_size():
    h = makeRandomHeap(0)
    assert 0 == h.size()
    
    h = makeRandomHeap(10)
    assert 10 == h.size()
    
    h = makeRandomHeap(100)
    assert 100 == h.size()    

def test_minimum(): # findMin and removeMin    
    h = makeHeap()
    assert 2 == h.findMin()
    
    h.removeMin()
    assert 3 == h.findMin()
    
    h.removeMin()
    assert 5 == h.findMin() 

def test_findMin_underflow(): # find Min from empty heap
    h = makeEmptyHeap()
    assert None == h.removeMin()

def test_removeMin_underflow(): # remove Min from heap
    h = makeEmptyHeap()
    assert None == h.removeMin()

def test_maximum(): # findMax and removeMax  
    h = makeHeap()
    assert 35 == h.findMax()
    
    h.removeMax()
    assert 25 == h.findMax()

    h.removeMax() 
    assert 18 == h.findMax()

def test_findMax_underflow(): # find Max from empty heap
    h = makeEmptyHeap()
    assert None == h.findMin() 

def test_removeMax_underflow(): # remove Max from empty heap
    h = makeEmptyHeap()
    assert None == h.removeMax()  

def test_insert_overflow(): # Test insert Overflow 
    h = makeHeap()
    assert None == h.insert(1, "A")
    
    h = makeRandomHeap(100)
    assert None == h.insert(1, "A")
    
    h = makeRandomHeap(0)
    assert None == h.insert(1, "A")


pytest.main(["-v", "-s", "mmh_test.py"])