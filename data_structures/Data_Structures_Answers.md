Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n) because visting very single node

2. What is the space complexity of your `depth_first_for_each` function?
O(n) every time you visit a node, its going to grow by that amount

3. What is the runtime complexity of your `breadth_first_for_each` method?
O(n)

4. What is the space complexity of your `breadth_first_for_each` method?
O(n)

5. What is the runtime complexity of your `heapsort` function?
O(1) + O(n) + O(n) * O(log n) + O(n) * O(log n)
O(1) + O(n) + O(n log n) + O(n log n)
O(1) + O(n) + O(2 * n log n)    # 2 is constant. delete the constant
O(1) + O(n) + O(n log n)        # which one is going to grow the most? O(1) --> not going to grow at all.
O(n) + O(n log n)               # O(n)--> grows linear. 
O(n log(n))                     # O(n log n)--> grows the fastest

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?
O(2n)       # O(n) for sorted and O(n) for heap
O(n)