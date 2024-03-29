# MinMax Heap
A MinMax heap is a complete binary tree data structure which combines the usefulness of both a min-heap and a max-heap. A min-max heap contains alternating min (or even) and max (or odd) levels. Even levels are for example 0, 2, 4, etc, and odd levels are respectively 1, 3, 5, etc. The root element is at the first level, i.e., 0 and contains the smallest element of the tree. One of the two elements in the second level, which is a max (or odd) level, is the greatest element in the min-max heap.

<b> The time complexities of a normal MinMax Heap are as follows: </b>
<p> &emsp; &emsp; &emsp; &ensp; Average &emsp; Worst </p>
<p> &emsp; Insert &ensp; O(log n)	&emsp;O(log n) <p>
<p> &ensp; Delete &ensp; O(log n) &emsp;[1]	O(log n) </p>

However this implementation works in 0(n) time by having a seperate function first determine whether the item will be on a min or max level and then calls the appropriate tickle function (Min/Max) which both run on a Min Heap or Max heap in 0(1) time. For more information on this click <a href = "https://stackoverflow.com/questions/47076465/how-to-build-a-min-max-heap-in-on-time-complexity">here</a>

For more information on MinMax Heaps continue reading <a href = "https://en.wikipedia.org/wiki/Min-max_heap">here</a>

## What you will find in minMaxHeap.py
This implementation of a MinMax Heap can perform the following operations:
1. Insert
2. Find Minimum
3. Find Maximum
4. Remove Minimum
5. Remove Maximum

This code also includes a test to ensure the MinMax Heap follows all the conditions of a MinMax Heap. such as:
1. Ensuring the root is the minimum
2. The max can be found on the 2nd level
3. Every level is alternating between Even/Min and Odd/Max
4. And ensuring that every nodes position follows MinMax Heap rules.

This code also includes two functions which print out visualizations of the Heap. One in Array form and one in tree form. 
This looks like the following respectively:

<img src="visualization pictures/heap2.png" alt="Heap Visualization" width="100%" height="100%">

<img src="visualization pictures/heap.png" alt="Heap Visualization" width="40%" height="40%"> 
<p> This Heap is read left to right, in that the top left is the root node (5, 'E'). </p>
<p> The next indented level is the 2nd level of the heap which in this case is (66, 'A') and (92, 'F'). </p>
<p> The next indented level is the 3rd level which has 2 mini trees for (66, 'A') and (92, 'F'). </p>
<p> For (66, 'A') this includes (7, 'I') and (21, 'J'), and for (92,'F') this includes (49,'C') and (59,'G'). And so on. </p>

## What you will find in mmh_test.py
This code uses pytest to test all the functuions used in minMaxHeap.py. It tests normal circumstances as well as extreme ones such as undeflow and overflow situations.
