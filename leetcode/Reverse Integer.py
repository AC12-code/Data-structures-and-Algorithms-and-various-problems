class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        sts = ""
        if "-" in x:
            sts = "".join("-")
        for i in x[::-1]:
            
            if i.isnumeric():
                sts += "".join(i)
        if int(sts) > 2**31 or int(sts) < -(2**31):
            return 0
        return int(sts)
