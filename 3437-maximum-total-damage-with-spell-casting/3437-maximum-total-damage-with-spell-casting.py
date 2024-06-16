from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = defaultdict(int)
        for p in power:
            freq[p] += 1
        
        powerset = sorted(freq.keys())
        
        n = len(powerset)
        
        if n==0:
            return 0
        
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            damage = powerset[i-1]
            power = damage * freq[damage]
            
            dp[i]=dp[i-1]
            if i == 1:
                dp[i] = max(dp[i], power)
                
            else:
                j = i-1
                while j>0 and powerset[j-1]>=damage-2:
                    j -= 1
                dp[i] = max(dp[i], power+dp[j])
        return dp[n]