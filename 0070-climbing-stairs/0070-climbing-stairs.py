class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        s1 = 1
        s2 = 2
        
        if  n <= 2:
            return n
        for i in range(3, n+1):
            res = s2+s1
            s1 = s2
            s2 = res
        return res