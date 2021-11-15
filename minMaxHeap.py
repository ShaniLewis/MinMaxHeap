import random
import math

class Node(object):
    def __init__(self, k, d):
        self.key  = k
        self.data = d
        
    def __str__(self): 
        return "(" + str(self.key) + "," + repr(self.data) + ")"
        
class Heap(object):
    def __init__(self, size):
        self.__arr = [None] * size  # Array
        self.__nElems = 0           # Number of elements in Array     
    
    #function to insert elements into the heap 
    def insert(self, key, data):
        
        # If the Array is full, return Error 
        if self.__nElems >= len(self.__arr):                   
            return print("Error: Array is full. (" + str(key) + ", " + str(data) + ") was not inserted. \n")
        
        # If the Array is not full make a new node, trickleUp and then increment nElems by 1
        else:
            self.__arr[self.__nElems] = Node(key,data) 
            self.__trickleUp(self.__nElems) 
            self.__nElems +=1  
    
    #function to decide which trickDown to use 
    def __trickleDown(self, cur):
        level = math.floor(math.log2(cur+1))
        
        # if the position is even
        if level %2 == 0:        
            #use the min heap                                                                             
            self.__trickleDownMin(cur) 
            
        #if the position is odd
        else:                 
            #use the max heap 
            self.__trickleDownMax(cur)                                            
    
    def __trickleDownMin(self, cur):
        index = None
        
        leftChild = 2*cur + 1
        rightChild = leftChild + 1
        
        leftGrandL = 2*leftChild + 1
        rightGrandL = leftGrandL + 1 
        
        leftGrandR = 2*rightChild + 1
        rightGrandR = leftGrandR + 1 
        
        if leftChild < self.__nElems:                                           # while the current node has children
            min = self.__arr[leftChild].key                                     # set min to be the first left child 
            index = leftChild                                                   # update the index
            
            if leftChild + 1 < self.__nElems:                                   # if there is a right child       
                if self.__arr[rightChild].key < min:                            # if the right child is smaller than the min
                    min = self.__arr[rightChild].key                            # update the min 
                    index = rightChild                                          # update the index 
                    
                if leftGrandL < self.__nElems:                                  # if the left child has a left child  
                    if self.__arr[leftGrandL].key < min:                        # if the leftmost grandchild is smaller than the min 
                        min = self.__arr[leftGrandL].key                        # update the min
                        index = leftGrandL                                      # update the index 
                        
                    if rightGrandL < self.__nElems:                             # if there is a right grandchild of the left child 
                        if self.__arr[rightGrandL].key < min:                   # if that child is smaller than the min
                            min = self.__arr[rightGrandL].key                   # update the min
                            index = rightGrandL                                 # update the index
                            
                        if leftGrandR < self.__nElems:                          # if there is a left grandchild of the right child 
                            if self.__arr[leftGrandR].key < min:                # if that is a child is smaller than the min
                                min = self.__arr[leftGrandR].key                # update the min
                                index = leftGrandR                              # update the index
                                
                            if rightGrandR < self.__nElems:                     # if there is a right grandchild of the right child  
                                if self.__arr[rightGrandR].key < min:           # if that is a child is smaller than the min
                                    min = self.__arr[rightGrandR].key           # update the min
                                    index = rightGrandR                         # update the index
                   
                    #if the index of the smallest is one of the grandchildren 
                    if index == leftGrandL or index == rightGrandL or index == leftGrandR or index == rightGrandR:
                       
                        #if the maximum is greater than cur 
                        if self.__arr[index].key < self.__arr[cur].key:  
                            #swap them 
                            self.__arr[index], self.__arr[cur] = self.__arr[cur], self.__arr[index]                
                            
                             #if the maximum is less than its parent 
                            if self.__arr[index].key > self.__arr[(index-1)//2].key:   
                                #swap them 
                                self.__arr[index], self.__arr[(index-1)//2] = self.__arr[(index-1)//2], self.__arr[index]  
                            
                            #recurse through the heap 
                            self.__trickleDownMin(index)
                        
                        #if it is not a grandchild and the maximum is greater than cur 
                        elif self.__arr[index].key > self.__arr[cur].key:      
                            #swap them 
                            self.__arr[index], self.__arr[cur] = self.__arr[cur], self.__arr[index]                            
    

    def __trickleDownMax(self, cur):
        index = None
        
        leftChild = 2*cur+1 
        rightChild = leftChild + 1
        
        leftGrandL = 2*leftChild + 1
        rightGrandL = leftGrandL + 1 
        
        leftGrandR = 2*rightChild + 1
        rightGrandR = leftGrandR + 1   
        
        if leftChild < self.__nElems:                                           # while the current node has children
            max = self.__arr[leftChild].key                                     # start on the left side and see if there is a greater max
            index = leftChild                                                   # update index
            
            if rightChild < self.__nElems:                                      # if there is a right child     
                if self.__arr[rightChild].key > max:                            # if that child is greater than the max
                    max = self.__arr[rightChild].key                            # set the max to that child
                    index = rightChild                                          # update the index
                    
                if leftGrandL < self.__nElems:                                  # if there is a leftmost grandchild 
                    if self.__arr[leftGrandL].key > max:                        # if that child is greater than the max
                        max = self.__arr[leftGrandL].key                        # set the max to that child
                        index = leftGrandL                                      # update the index
                        
                    if rightGrandL < self.__nElems:                             # if there is a right grandchild to the left child 
                        if self.__arr[rightGrandL].key > max:                   # if that child is greater than the max
                            max = self.__arr[rightGrandL].key                   # set the max to that child
                            index = rightGrandL                                 # update the index
                            
                        if leftGrandR < self.__nElems:                          # if there is a left grandchild to the right child  
                            if self.__arr[leftGrandR].key > max:                # if that child is greater than the max
                                max = self.__arr[leftGrandR].key                # set the max to that child
                                index = leftGrandR                              # Update the index
                                
                            if leftGrandR + 1 < self.__nElems:                  # if there is a rightmost grandchild
                                if self.__arr[rightGrandR].key > max:           # if that child is greater than the max
                                    max = self.__arr[rightGrandR].key           # set the max to that child
                                    index = rightGrandR                         # Update the index
                                    
                    #if the maximum is a grandchild 
                    if index == leftGrandL or index == rightGrandL or index == leftGrandR or index == rightGrandR:
                        #if the maximum is greater than cur 
                        if self.__arr[index].key > self.__arr[cur].key:  
                            #swap them 
                            self.__arr[index], self.__arr[cur] = self.__arr[cur], self.__arr[index]     
                            
                             #if the maximum is less than its parent
                            if self.__arr[index].key < self.__arr[(index-1)//2].key:    
                                #swap them 
                                self.__arr[index], self.__arr[(index-1)//2] = self.__arr[(index-1)//2], self.__arr[index]  
                            
                            #recurse through the heap 
                            self.__trickleDownMax(index)
                            
                    #if it is not a grandchild and the maximum is greater than cur 
                    elif self.__arr[index].key < self.__arr[cur].key:   
                        #swap them 
                        self.__arr[index], self.__arr[cur] = self.__arr[cur], self.__arr[index]                           
    
    def __trickleUp(self, cur):
        parent = (cur-1)//2
        level = math.floor(math.log2(cur+1)) #set the level  
        
        # Min level 
        if level%2 == 0:                                                       
            #if there is a parent and this node is greater than the parent 
            if cur > 0 and (self.__arr[cur].key > self.__arr[parent].key):
                #swap them 
                self.__arr[cur], self.__arr[parent] = self.__arr[parent], self.__arr[cur]                       
                self.__trickleUpMax(parent)                                            
            else: self.__trickleUpMin(cur)
      
        # Max level
        else: 
            #if there is a parent and that parent is greater than this node 
            if cur > 0 and self.__arr[cur].key < self.__arr[parent].key:
                #swap them
                self.__arr[cur], self.__arr[parent] = self.__arr[parent], self.__arr[cur]                        
                self.__trickleUpMin(parent) #if it's less than, trickleupmin
            else: self.__trickleUpMax(cur)  #if its greater, trickleupmax               
        
    def __trickleUpMin(self, cur):
        while cur > 2: 
            parent = (cur-1)//2
            grandparent = (parent-1)//2
            
            #if there is a grandparent and the node is less than that grandparent 
            if self.__arr[cur].key < self.__arr[grandparent].key:   
                
                #swap them 
                self.__arr[cur], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[cur]                          
                cur = grandparent   
            else: return 
    
    def __trickleUpMax(self, cur):
        while cur > 2: 
            parent = (cur-1)//2
            grandparent = (parent-1)//2    
            
            #if there is a grandparent and the node is greater than that grandparent
            if self.__arr[cur].key > self.__arr[grandparent].key:  
                
                #swap them 
                self.__arr[cur], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[cur]                          
                cur = grandparent
            else: return 
    
    #function to find the minimum which should be at the root 
    def findMin(self):
        if self.__nElems > 0: return self.__arr[0].key  
        else: return None     
    
    #function to find the maximum which should be one of the children of the root 
    def findMax(self):
        if self.__nElems == 0: return None
        if self.__nElems > 0: 
            if self.__nElems == 1: return self.__arr[0]
            cur = 0                                                             # This is the root 
            left = 2*cur + 1                                                    # this is the left child
            right = left + 1                                                    # right child
            if left < self.__nElems and right >= self.__nElems:
                return self.__arr[left].key
            if left < self.__nElems and right < self.__nElems:
                if self.__arr[left].key > self.__arr[right].key:                #find the max between the children 
                    return self.__arr[left].key
                else: return self.__arr[right].key
    
    #function to remove a minimum but keep it as a minmaxheap  
    def removeMin(self):
        if self.__nElems > 0:
            root = self.__arr[0].key                     #set the root 
            self.__nElems -= 1                           #subtract from the number of items 
            self.__arr[0] = self.__arr[self.__nElems]    #make the root they last item 
            self.__trickleDown(0)                                               
    
    #removing the maximum node 
    def removeMax(self):      
        if self.__nElems == 0: return None
        cur = 0                                                                 
        left = 2*cur + 1                                                        # this is the left child
        right = left + 1                                                        # this is the right child 
        self.__nElems -=1                                                       # subtract from the number of elements 
      
        if left < self.__nElems and right >= self.__nElems:                     # if there is only a left child 
            self.__arr[left] = self.__arr[self.__nElems]                        # make that child the last item 
            self.__trickleDown(left)                                            # trickledown 
       
        if left < self.__nElems and right < self.__nElems:                      # if there are two children:
            
            if self.__arr[left].key > self.__arr[right].key:                    # the left one is bigger 
                self.__arr[left] = self.__arr[self.__nElems]                    # trickledown 
                self.__trickleDown(left)
            else:                                                               
                self.__arr[right] = self.__arr[self.__nElems]                   # the right one is bigger 
                self.__trickleDown(right)                                       # trickledown 
                                  
    def isMinMaxHeap(self):
        cur = 0
        size = self.__nElems
        
        #while there is a child
        while cur < size // 2: 
            level = math.floor(math.log2(cur+1)) 
            leftChild  = 2 * cur + 1        
            rightChild = leftChild + 1 
            
            #if it is an even level
            if level % 2 == 0: 
                #if there is a right child and the right child is less than its parent 
                #if there is a left child and the left child is less than its parent  
                if (rightChild < size and self.__arr[rightChild].key < \
                    self.__arr[cur].key) or (leftChild < size and self.__arr[leftChild].key \
                    < self.__arr[cur].key):
                    return "No" #False 
            
            #if it is an odd level
            else:   
                #if there is a right child and it is greater than its parent 
                #if there is a left child and it is greater than its parent
                if (rightChild < size and self.__arr[rightChild].key > \
                    self.__arr[cur].key) or (leftChild < size and self.__arr[leftChild].key \
                    > self.__arr[cur].key):
                    return "No" #False  
            cur += 1 
            
        #if you fall out, return true 
        return "Yes" #True                               
    
    def displayHeapArray(self):      
        print("Heap Array: ", end="")
        for m in range(self.__nElems):
            print(str(self.__arr[m]) + " ", end="")
        print()
        

    def __display(self, cur, indent):
        if cur < self.__nElems:
            leftChild  = 2*cur + 1      
            print((" " * indent) + str(self.__arr[cur]))
            if leftChild < self.__nElems:
                self.__display(leftChild,   indent+6)
                self.__display(leftChild+1, indent+6)
        else:
            return
    
    def display(self): 
        self.__display(0, 0)                    
    

def __main():
    h = Heap(10)  # make a new heap with maximum of 10 elements
    for i in range(10):  # insert 30 items
        val = random.randint(0, 100)
        h.insert(val, chr(ord('A') + i))
   
    print("This is the Min: ", h.findMin())
    print("This is the Max: ", h.findMax()) 
    print("Does this satisfy MinMax Heap conditions? ", h.isMinMaxHeap())
    h.displayHeapArray()
    
    print()
    h.display()  
    
    
    

if __name__ == '__main__':
    __main() 