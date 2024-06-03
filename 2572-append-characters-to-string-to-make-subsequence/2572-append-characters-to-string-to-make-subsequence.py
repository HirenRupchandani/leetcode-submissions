class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        trackS = 0
        trackT = 0
        nS = len(s)
        nT = len(t)
        while trackS < nS and trackT < nT:
            if s[trackS] == t[trackT]:
                trackT += 1
                trackS += 1
            else:
                trackS += 1
        return nT - trackT