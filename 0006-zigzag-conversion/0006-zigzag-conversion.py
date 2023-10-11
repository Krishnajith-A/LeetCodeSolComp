class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows = [''] * numRows
        currow=0
        direc=1
        for char in s:
            rows[currow]+=char
            if currow==0:
                direc=1
            elif currow==numRows-1:
                direc=-1
            currow+=direc
        res=''.join(rows)
        return res