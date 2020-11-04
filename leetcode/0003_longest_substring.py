class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0
        for i in range(len(s)):
            for ii in range(len(sub)):
                if sub[ii] == s[i]:
                    sub = sub[ii+1:]
                    break
            sub += s[i]
            if len(sub)>max_len:
                max_len =  len(sub)
        return max_len