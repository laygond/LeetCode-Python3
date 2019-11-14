class Solution:
    def reverse(self, x: int) -> int:
                
        if x<0:
            sign = -1
            abs_x = sign*x
        else:
            sign = 1
            abs_x = x
        
        if x <pow(2,31)-1 and x>-pow(2,31):
            str_x = str(abs_x)
            result = sign*int(str_x[::-1])
            
            if result <pow(2,31)-1 and result>-pow(2,31):
                return result
            else:
                return 0
        else:
            return 0
