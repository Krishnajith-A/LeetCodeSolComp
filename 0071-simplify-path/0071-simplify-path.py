class Solution:
    def simplifyPath(self, path: str) -> str:
        p=[]
        k=path.split('/')
        for i in k:
            if i == '..':
                if p:
                    p.pop()
            elif i and i != '.':
                p.append(i)
        sp = '/' + '/'.join(p)
        return sp