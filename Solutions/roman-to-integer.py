class Solution:
    def romanToInt(self, s: str) -> int:
        num_list = []
        for letter in s:
            if letter == "I": num_list.append(1)
            if letter == "V": num_list.append(5)
            if letter == "X": num_list.append(10)
            if letter == "L": num_list.append(50)
            if letter == "C": num_list.append(100)
            if letter == "D": num_list.append(500)
            if letter == "M": num_list.append(1000)

        total = 0
        i=0
        while i < len(s)-1:

            if num_list[i]<num_list[i+1]:
                total+=num_list[i+1]-num_list[i]
                i+=2

            else:
                total+=num_list[i]
                i+=1

        if i==len(s)-1:
            total+=num_list[i]
        
        return total
                
