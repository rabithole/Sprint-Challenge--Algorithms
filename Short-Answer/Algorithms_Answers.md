#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) (log n) The number of operations does not increase with a larger input. 

b) O(n) The same number of operations are performed for each input. 

c) O(1) Run time is not affected by the size of the input. 

## Exercise II
- Use a binary search
- The main goal is to minimize the number of broken eggs. 
- The height of the building in unknown but must be determined. 
---
1. Calculate the number of floors. 
2. Divide by two to get the middle floor. 
3. Add one floor if the number of floors is even. 
4. Drop egg.
5. If egg breaks, current floor equals top
6. Repeat steps 1 - 5.  
7. If egg does not break, current floor equals bottom.
8. Repeate steps 1 - 5.

