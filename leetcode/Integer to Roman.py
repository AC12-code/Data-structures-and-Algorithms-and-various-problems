class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",2:"II",3:"III",4:"IV",
               6:"VI",7:"VII",8:"VIII",9:"IX",90:"XC",900:"CM",40:"XL",400:"CD",60:"LX",
               70:"LXX",80:"LXXX",600:"DC",700:"DCC",800:"DCCC"}
       
        c = str(num)
        count = 1
        result = 0
        lis = []
        strs = ""
        if len(c) == 1:
            return dict[num]
        for i in c[::-1]:
            
            result = int(i) * count
            quo = result//count
            if result in dict:
                lis.append(dict[result])
            else:
                lis.append(dict[count]*quo)
       
            count*=10
     
        for j in lis[::-1]:
            strs += "".join(j)
        
        return strs
