#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(log n) 
The amount of operations is dependant the size of the input, but the run time and space complexity decreases as the size of the input increases. The size of the input in this case is only numeric. Calculations of this sort barely affect run time complexity.  

b)
O(n^2)
The number of operations increases exponentially as the size of the input increases. Small inputs are ok, but scalability is a problem.

c)
O(n)
Even with a factorial, the number of operations are still the same as the size of the input. 

## Exercise II
O(log n)
Use a binary search
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
