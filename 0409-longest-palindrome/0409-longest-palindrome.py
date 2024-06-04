class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for i in s:
            # IF c not in set
            if i not in ss: 
                # Push into set
                ss.add(i)
                # print(ss)
            else: 
                # Remove if same character is encountered again, satisfies palindrome condition
                ss.remove(i)
                # print(ss)
        return len(s) - len(ss) + 1 if len(ss) != 0 else len(s)
        # hmap = {}
        # odd = False
        # res = 0
        # for c in s:
        #     hmap[c] = hmap.get(c, 0) + 1

        # for v in hmap.values():
        #     if v%2 == 0:
        #         res += v
        #     if v%2 != 0:
        #         print(v)
        #         odd = True
        #         res += v-1
        # return res + 1 if odd else res
        