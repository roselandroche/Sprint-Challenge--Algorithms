#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n)
    
    When thinking about "How many times will this loop run as n gets bigger?", the first thing students should do is look at the condition & increment operations used by the while loop.
    The whole thing is similar to for loop:
    for (a = 0; a < n * n * n; a += n * n)We loop as long as a is smaller than n^3. Each iteration, we add n^2 to a. n^3 / n^2 = n --> the loop will run n times.

b)
    O(n log n) 

    Broken down from the inside out, lines 20, 21, and 18 are O(1) so basically too small to notice. 
    19 - the while loop only runs while j is less than n, and j is incremented up by multiplying by 2.
    17 - O(n) because it loops over everything

c)
    O(n)

    When thinking about "How many times will recursively call bunnyEars() as bunnies gets bigger?", the first thing students should do is look at how the parameters change in the recursive call. Since we are only decrementing bunnies by 1 every time, the function will be called n times. Equivalent to a loop from 0 to bunnies. We call recursively with bunnies-1each time.
    Answer: O(n)

## Exercise II

I would use a Binary Search to solve this problem.

Floors are inherently numbered aka sorted, so I would take the middle floor and check if a thrown egg breaks. If broken, I would check if the floor directly below results in an unbroken egg. This would mean the middle floor is the answer I am looking for (floor f). 

If not, I would automatically stop considering the higher floors and only check the lower floors. I would recalculate the middle of the lower floors and repeat this process until I found the lowest floor the breaks the egg and the highest floor that does not break the egg.

This would be O(log n)