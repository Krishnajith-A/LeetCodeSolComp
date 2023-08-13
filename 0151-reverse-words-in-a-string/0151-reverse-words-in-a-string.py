class Solution:
    def reverseWords(self, s: str) -> str:
        p=s.split()
        r=' '.join(p[::-1])
        return r
            