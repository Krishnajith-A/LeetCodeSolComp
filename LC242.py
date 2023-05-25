'''question: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
 word or phrase, typically using all the original letters exactly once.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict={}
        # for i in s:
        #     if i in dict:
        #         dict[i]+=1
        #     else:
        #         dict[i]=1
        # for i in t:
        #     if i in dict:
        #         dict[i]-=1
        #     else:
        #         return False
        # for i in dict.values():
        #     if i!=0:
        #         return False
        # return True

        return all(s.count(i) == t.count(i) )