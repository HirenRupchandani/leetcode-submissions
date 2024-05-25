class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        return self.wordBreakHelper(s,0,wordset)
    
    def wordBreakHelper(self,s,start,wordset):
        valid = []
        if start==len(s):
            valid.append("")
        for end in range(start+1,len(s)+1):
            prefix=s[start:end]
            if prefix in wordset:
                suffixes = self.wordBreakHelper(s,end,wordset)
                for suffix in suffixes:
                    valid.append(prefix+("" if suffix == "" else " ") + suffix)
        return valid
        