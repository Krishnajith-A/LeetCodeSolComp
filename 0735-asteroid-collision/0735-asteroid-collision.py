class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in asteroids:
            if i>0 or not s:
                s.append(i)
            else:
                while s and s[-1]>0:
                    if i==-(s[-1]):
                        s.pop()
                        break
                    elif -i>s[-1]:
                        s.pop()
                    else:
                        break
                else:
                    s.append(i)
        return s