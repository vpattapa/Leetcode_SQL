class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        arr = ['0']*len(s)
        for (ch, ind) in zip(s, indices):
            arr[ind] = ch
    
        return ''.join(arr)
            