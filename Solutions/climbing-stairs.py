class Solution:
    def factorial(self, a):
        fact = 1
        for i in range(1,a+1): 
            fact = fact * i 
        return fact
    
    def climbStairs(self, n: int) -> int:
        if n<1: return 0
       
        steps_1 = n%2    
        steps_2 = n//2
        
        count_ways=1
        while (steps_2>0):
            count_ways += self.factorial(steps_2+steps_1)/(self.factorial(steps_2)*self.factorial(steps_1))
            steps_2 -= 1
            steps_1 += 2
            
        return int(count_ways)
