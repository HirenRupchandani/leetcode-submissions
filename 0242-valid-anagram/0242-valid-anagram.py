class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for c in s:
            if c not in check:
                check[c] = 1
            else:
                check[c] += 1
        for c in t:
            if c not in check:
                return False
            else:
                check[c] -= 1
        print(check)
        for k,v in check.items():
            if v != 0:
                return False
        return True


        check = {}
        if len(s)!=len(t):
            return False
        
        for char in s:
            if char not in check:
                check[char]=1
            else:
                check[char]+=1
        
        for char in t:
            if char in check:
                check[char]-=1
            else:
                return False
        
        for val in check.values():
            if val!=0:
                return False
        
        return True