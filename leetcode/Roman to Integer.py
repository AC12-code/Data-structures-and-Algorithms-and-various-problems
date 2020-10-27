class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",2:"II",3:"III",4:"IV",
               6:"VI",7:"VII",8:"VIII",9:"IX",90:"XC",900:"CM",40:"XL",400:"CD",60:"LX",
               70:"LXX",80:"LXXX",600:"DC",700:"DCC",800:"DCCC",0:"0"}
        lis1  = list(dict.keys())
        lis2  = list(dict.values())
        result = 0
        c=0
        lol = []
        gbr = list(s)
        if s in lis2:
            return lis1[lis2.index(s)]
        
        for i in range(len(s) - 1):

            if lis1[lis2.index(s[i])] < lis1[lis2.index(s[i + 1])]:
                d = "".join(s[i] + s[i + 1])
                c = lis1[lis2.index(d)]
                lol.append(c)
                gbr[i] = "0"
                gbr[i+1] = "0"
                i += 2

        
        for i in gbr:
            if i.isalpha():
                c = lis1[lis2.index(i)]
                result += c
        for i in lol:
            result += i
            
    
        return result
