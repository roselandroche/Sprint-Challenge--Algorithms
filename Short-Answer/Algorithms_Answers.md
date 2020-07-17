#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n^3) <-- final answer
    
    Line 11 is O(1) 
    10 is O(n^3) because it's while a is less than n^3, therefore it runs n^3 times

b)
    O(n - j / 2) * O(n) <-- final answer

    Broken down from the inside out, lines 20, 21, and 18 are O(1) so basically too small to notice. 
    19 is O(n - j / 2) because the while loop only runs while j is less than n, and j is incremented up by multiplying by 2.
    17 is a basic O(n) because it loops over everything

c)
    O(2^n) <-- final answer

    Line 26 and 27 are O(1)
    Line 29 puts another call on the stack and starts the process again, until we are out of bunnies. This is therefore exponential.

## Exercise II

I would use a Binary Search to solve this problem.

Floors are inherently numbered aka sorted, so I would take the middle floor and check if a thrown egg breaks. If broken, I would check if the floor directly below results in an unbroken egg. This would mean the middle floor is the answer I am looking for (floor f). 

If not, I would automatically stop considering the higher floors and only check the lower floors. I would recalculate the middle of the lower floors and repeat this process until I found the lowest floor the breaks the egg and the highest floor that does not break the egg.

This would be O(log n)