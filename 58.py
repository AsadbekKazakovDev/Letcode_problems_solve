class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.split()
        return len(b[-1])
        '''
        ans=[]
        for i in range(len(b)):
            ans.append(len(b[i]))
        k = max(ans)
        for i in range(len(b)):
            if k==len(b[i]):
                return (len(b[i]))
                break'''
        