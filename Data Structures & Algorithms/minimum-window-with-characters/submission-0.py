class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # declare countT, window, loop each char in t, add 1 to countT.get(c, 0) basically for each c found add 1.
        # and then declare have, need (0, len countT), and res, resLen ([-1,-1], infinity) and declare l pointer 0
        # then loop r point through the s.length, note that c is s[r]
        # and add every c in window (win[c]) we add 1 to keep count (window.get(c, 0))
        # we then check if c is in countT AND if window[c] is th esame as countT[c], if so add 1 to have
        # finally check while have == need, EVERYTHING BELOW IS INSIDE THIS WHILE
        # if the total window (r - l + 1) < reslen, replace res with [l, r]
        # and reslen with the total window. outside the if, reduce the window by left pointer window[s[l]]-=1
        # then check now if s[l] is in countT and if window[s[l]] < countT[s[l]], then reduce have by 1
        # shrink the l pointer outside the if, move it forward.
        # finally, outside WHILE replace l, r pointers with the res, and return a sliced s[l : r + 1] if the reslen is not infinity, otherwise ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        res, resLen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ""
            
        


