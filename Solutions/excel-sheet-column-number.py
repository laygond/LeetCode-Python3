class Solution:
    def titleToNumber(self, s: str) -> int:
        s_num = [ord(letter)-65+1 for letter in s]
        
        for i in range(1,len(s_num)+1):
            s_num[-i] = s_num[-i] * (26**(i-1))
                
        return sum(s_num)
