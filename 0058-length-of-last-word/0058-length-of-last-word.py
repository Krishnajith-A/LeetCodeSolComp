class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p=s.split()
        if not p:
            return 0
        return len(p[-1])
        