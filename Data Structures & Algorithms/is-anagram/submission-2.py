class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h1, h2 = {},{}
        c1, c2 =0,0
        for i in range(len(s)):
            if s[i] in h1:
                h1[s[i]]=h1[s[i]]+1
            else:
                h1[s[i]]=c1+1
                c1=0
        for i in range(len(s)):
            if t[i] in h2:
                h2[t[i]]=h2[t[i]]+1
            else:
                h2[t[i]]=c2+1
                c2=0
        return h1==h2

            