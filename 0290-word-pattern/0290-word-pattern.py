class Solution(object):
    def wordPattern(self, pattern, s):
        w = s.split()

        if len(pattern)!=len(w):
            return False

        ps_t = {}
        wt_s = {}

        for c1,c2 in zip(pattern,w):
            if c1 in ps_t and ps_t[c1]!=c2:
                return False
            if c2 in wt_s and wt_s[c2]!=c1:
                return False

            ps_t[c1] = c2
            wt_s[c2] = c1

        return True
        
        