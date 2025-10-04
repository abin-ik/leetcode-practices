#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#  The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#Additionally, if the number is negative, return 0.

#Note: If a number is a multiple of both 3 and 5, only count it once.

#Courtesy of projecteuler.net (Problem 1)
import numpy as np
def solution(n):
    if n < 0:
        return 0
    else:
        l = [i for i in range(n) if i%3 ==0 or i%5 ==0]
        print(l)
        c=np.sum(l)
        return c

print(solution(16))