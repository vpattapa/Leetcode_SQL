class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        dic = {}
        j = 0
        for i in s:
            dic[indices[j]] = i
            j += 1
        
        sorted_dic = sorted(dic.items(), key=lambda x:x[0])
        res = ''
        for i in sorted_dic:
            res += i[1]
        return res
            