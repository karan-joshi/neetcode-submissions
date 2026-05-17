class Solution:
    def sumOfSquare(self, n: int) -> int:
        output = 0

        while n:
            digit = n%10
            output += digit**2
            n = n//10
        
        return output
    
    def isHappy(self, n: int) -> bool:
        
        sums = set()

        while n not in sums:
            sums.add(n)
            n = self.sumOfSquare(n)
            if n==1:
                return True

        return False